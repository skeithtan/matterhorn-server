import rest_framework
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from graphene_django.views import GraphQLView
from institutions.models import *
from students.models import *


class PrivateGraphQLView(GraphQLView):
    def parse_body(self, request):
        if isinstance(request, rest_framework.request.Request):
            return request.data
        return super(PrivateGraphQLView, self).parse_body(request)

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(PrivateGraphQLView, cls).as_view(*args, **kwargs)
        view = permission_classes((IsAuthenticated,))(view)
        view = authentication_classes((TokenAuthentication,))(view)
        view = api_view(['POST', 'GET'])(view)
        return view


class SignInView(APIView):
    @staticmethod
    def post(request):
        if "username" not in request.data or "password" not in request.data:
            return Response(data={
                "error": "Missing username or password"
            }, status=400)

        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(username=username, password=password)

        if user is None:
            return Response(data={
                "error": "Invalid credentials"
            }, status=401)

        if Token.objects.filter(user=user).count() == 1:
            token = Token.objects.get(user=user)
        else:
            token = Token.objects.create(user=user)

        print(token.user, user)
        try:
            user_type = user.groups.all()[0].name
        except:
            user_type = 'Not Set'

        return Response(data={
            "token": token.key,
            "username": username,
            "user_type": user_type
        }, status=200)


class ModelRestoreView(APIView):
    def get_model(self):
        return None

    def get_serializer_class(self):
        return None

    def put(self, request, pk):
        model = get_object_or_404(self.get_model().archived.all(), pk=pk)
        model.undelete()
        serializer = self.get_serializer_class()(model)
        return Response(serializer.data)


class UnitReportView(APIView):
    @staticmethod
    def get(request):
        if "academic-year" not in request.GET or "term" not in request.GET:
            return Response(data={
                "error": "Please specify AY and Term"
            }, status=400)
        data = []
        academic_year = get_object_or_404(AcademicYear, pk=request.GET.get('academic-year'))
        term = get_object_or_404(Term, pk=request.GET.get('term'))

        # get all inbound and outbounds with AY and Term
        report_data = ReportItem.get_data(academic_year, term)
        deployed_outbounds = report_data.get('deployed_outbounds')
        accepted_inbounds = report_data.get('accepted_inbounds')

        # process data to get all report items
        report_items = ReportItem.process_data(deployed_outbounds,
                                               accepted_inbounds,
                                               "unit")
        # transform report items into json
        for item in report_items:
            deficit = item.outbound_units_enrolled - item.inbound_units_enrolled
            data.append({
                "institution": item.institution,
                "outbound_units_enrolled": item.outbound_units_enrolled,
                "inbound_units_enrolled": item.inbound_units_enrolled,
                "+/-": deficit
            })

        return Response(data=data, status=200)


class StudentDistributionReportView(APIView):
    @staticmethod
    def get(request):
        if "academic-year" not in request.GET or "term" not in request.GET:
            return Response(data={
                "error": "Please specify AY and Term"
            }, status=400)
        data = []
        academic_year = get_object_or_404(AcademicYear, pk=request.GET.get('academic-year'))
        term = get_object_or_404(Term, pk=request.GET.get('term'))

        report_data = ReportItem.get_data(academic_year, term)
        deployed_outbounds = report_data.get('deployed_outbounds')
        accepted_inbounds = report_data.get('accepted_inbounds')

        report_items = ReportItem.process_data(deployed_outbounds,
                                               accepted_inbounds,
                                               "student_distribution")

        for item in report_items:
            deficit = item.outbound_students_count - item.inbound_students_count
            data.append({
                "institution": item.institution,
                "outbound_students_count": item.outbound_students_count,
                "inbound_students_count": item.inbound_students_count,
                "+/-": deficit
            })

        return Response(data=data, status=200)


class GeneralStatisticsReportView(APIView):
    @staticmethod
    def get(request):
        if "academic-year" not in request.GET \
                or "term" not in request.GET \
                or "filter" not in request.GET:
            return Response(data={
                "error": "Please specify AY, Term, and filter method"
            }, status=400)
        data = []
        academic_year = get_object_or_404(AcademicYear, pk=request.GET.get('academic-year'))
        term = get_object_or_404(Term, pk=request.GET.get('term'))
        report_data = ReportItem.get_data(academic_year, term)
        accepted_inbounds = report_data.get('accepted_inbounds')
        deployed_outbounds = report_data.get('deployed_outbounds')

        if request.GET.get('filter') == "college":
            for key, college in COLLEGES:
                data.append({
                    'abbreviation': key,
                    'college': college,
                    'inbound_undergrad_students': 0,
                    'inbound_graduate_students': 0,
                    'outbound_undergrad_students': 0,
                    'outbound_graduate_students': 0,
                })

            for program in accepted_inbounds:
                for key, college in COLLEGES:
                    if program.student_program.student.college == key:
                        report_item = [item for item in data if item["college"] == college][0]
                        if not program.student_program.student.is_graduate:
                            report_item["inbound_undergrad_students"] += 1
                        else:
                            report_item["inbound_graduate_students"] += 1
            for program in deployed_outbounds:
                for key, college in COLLEGES:
                    if program.student_program.student.college == key:
                        report_item = [item for item in data if item["college"] == college][0]
                        if not program.student_program.student.is_graduate:
                            report_item["outbound_undergrad_students"] += 1
                        else:
                            report_item["outbound_graduate_students"] += 1

        elif request.GET.get('filter') == "country":
            for program in accepted_inbounds:
                for country in Country.objects.all():
                    if program.student_program.student.institution.country.name == country.name:
                        # if country doesnt exist in data
                        if not [item for item in data if item["country"] == country.name]:
                            if not program.student_program.student.is_graduate:
                                data.append({
                                    "country": country.name,
                                    'inbound_undergrad_students': 1,
                                    'inbound_graduate_students': 0,
                                    'outbound_undergrad_students': 0,
                                    'outbound_graduate_students': 0,
                                })
                            else:
                                data.append({
                                    "country": country.name,
                                    'inbound_undergrad_students': 0,
                                    'inbound_graduate_students': 1,
                                    'outbound_undergrad_students': 0,
                                    'outbound_graduate_students': 0,
                                })
                        else:
                            item = [item for item in data if item["country"] == country.name][0]
                            if not program.student_program.student.is_graduate:
                                item["inbound_undergrad_students"] += 1
                            else:
                                item["inbound_graduate_students"] += 1

                                # outbound
            for program in deployed_outbounds:
                for country in Country.objects.all():
                    if program.student_program.student.institution.country.name == country.name:
                        # if country doesnt exist in data
                        if not [item for item in data if item["country"] == country.name]:
                            if not program.student_program.student.is_graduate:
                                data.append({
                                    "country": country.name,
                                    'inbound_undergrad_students': 0,
                                    'inbound_graduate_students': 0,
                                    'outbound_undergrad_students': 1,
                                    'outbound_graduate_students': 0,
                                })
                            else:
                                data.append({
                                    "country": country.name,
                                    'inbound_undergrad_students': 0,
                                    'inbound_graduate_students': 0,
                                    'outbound_undergrad_students': 0,
                                    'outbound_graduate_students': 1,
                                })
                        else:
                            item = [item for item in data if item["country"] == country.name][0]
                            if not program.student_program.student.is_graduate:
                                item["outbound_undergrad_students"] += 1
                            else:
                                item["outbound_graduate_students"] += 1


        else:
            return Response(data={
                "error": "Please choose between 'college' or 'country'"
            }, status=400)

        return Response(data=data, status=200)


class OutboundUnitsReportView(APIView):
    @staticmethod
    def get(request):
        if "academic-year" not in request.GET or "term" not in request.GET:
            return Response(data={
                "error": "Please specify AY and Term"
            }, status=400)
        data = []
        academic_year = get_object_or_404(AcademicYear, pk=request.GET.get('academic-year'))
        term = get_object_or_404(Term, pk=request.GET.get('term'))
        report_data = ReportItem.get_data(academic_year, term)
        deployed_outbounds = report_data.get('deployed_outbounds')

        for program in deployed_outbounds:
            for institution in Institution.objects.all():
                if program.student_program.student.institution == institution:
                    # if country doesnt exist in data
                    if not [item for item in data if item["institution"] == institution.name]:
                        data.append({
                            "institution": institution.name,
                            "students": 1,
                            "default_units": program.default_units,
                            "total_units": program.total_units_enrolled
                        })
                    else:
                        item = [item for item in data if item["institution"] == institution.name][0]
                        item["default_units"] += program.default_units
                        item["total_units"] += program.total_units_enrolled
                        item["students"] += 1

        return Response(data=data, status=200)


class ReportItem(object):
    institution = None
    outbound_units_enrolled = 0
    inbound_units_enrolled = 0
    outbound_students_count = 0
    inbound_students_count = 0

    def __init__(self,
                 outbound_students_count=0,
                 inbound_students_count=0,
                 inbound_units_enrolled=0,
                 outbound_units_enrolled=0,
                 institution=None):
        self.institution_name = institution
        self.outbound_units_enrolled = outbound_units_enrolled
        self.inbound_units_enrolled = inbound_units_enrolled
        self.outbound_students_count = outbound_students_count
        self.inbound_students_count = inbound_students_count

    @staticmethod
    def exist(institution, list):
        for item in list:
            if item.institution == institution:
                return item
        return False

    @staticmethod
    def get_data(academic_year, term):
        # Outbound programs with AY and term
        outbound_programs = [outbound_program for outbound_program
                             in OutboundProgram.objects.all()
                             if outbound_program.program.academic_year == academic_year
                             and term in outbound_program.program.terms_available.all()]

        inbound_programs = [inbound_program for inbound_program
                            in InboundProgram.objects.all()
                            if inbound_program.program.academic_year == academic_year
                            and term in inbound_program.program.terms_available.all()]

        # get all deployed programs with specific AY and Term
        deployed_outbounds = [program for program
                              in DeployedStudentProgram.objects.all()
                              if program.student_program.program in outbound_programs]
        accepted_inbounds = [program for program
                             in AcceptedStudentProgram.objects.all()
                             if program.student_program.program in inbound_programs]

        return {
            'accepted_inbounds': accepted_inbounds,
            'deployed_outbounds': deployed_outbounds,
            'inbound_programs': inbound_programs,
            'outbound_programs': outbound_programs
        }

    @staticmethod
    def process_data(deployed_outbounds, accepted_inbounds, report_type):
        # summarize per institution and append outbound
        report_items = []
        for item in deployed_outbounds:
            report_item = ReportItem()
            for institution in Institution.objects.all():
                program_institution = item.student_program.program.institution
                if program_institution == institution:
                    report_item.institution = institution.name
                    if report_type == "unit":
                        report_item.outbound_units_enrolled += item.total_units_enrolled
                    elif report_type == "student_distribution":
                        report_item.outbound_students_count += 1
                    existing_report = ReportItem.exist(institution.name, report_items)
                    if not existing_report:
                        report_items.append(report_item)
                    else:
                        if report_type == "unit":
                            existing_report.outbound_units_enrolled += item.total_units_enrolled
                        elif report_type == "student_distribution":
                            existing_report.outbound_students_count += 1
                else:
                    continue
        # append inbound
        for inbound in accepted_inbounds:
            existing_report_items = [item.institution for item in report_items]
            institution = inbound.student_program.student.institution.name
            # with inbound units but doesnt exist in report_items
            if institution not in existing_report_items:
                # create empty report
                report_item = ReportItem()
                report_item.institution = institution
                report_items.append(report_item)
            report_item = ReportItem()
            for item in report_items:
                if str(inbound.student_program.student.institution) == item.institution:
                    existing_report = ReportItem.exist(item.institution, report_items)
                    if report_type == "unit":
                        report_item.inbound_units_enrolled += inbound.total_units_enrolled
                    elif report_type == "student_distribution":
                        report_item.inbound_students_count += 1
                    if not existing_report:
                        report_items.append(report_item)
                    else:
                        if report_type == "unit":
                            existing_report.inbound_units_enrolled += inbound.total_units_enrolled
                        elif report_type == "student_distribution":
                            existing_report.inbound_students_count += 1

        return report_items

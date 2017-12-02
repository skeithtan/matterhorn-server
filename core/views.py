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

        return Response(data={
            "token": token.key,
            "username": username
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
        if "academic_year" not in request.GET or "term" not in request.GET:
            return Response(data={
                "error": "Please specify AY and Term"
            }, status=400)
        data = []
        academic_year = get_object_or_404(AcademicYear, pk=request.GET.get('academic_year'))
        term = get_object_or_404(Term, pk=request.GET.get('term'))

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

        # summarize per institution
        for institution in Institution.objects.all():
            units_sum = 0
            for item in deployed_outbounds:
                program_institution = item.student_program.program.institution
                if program_institution == institution:
                    units_sum += item.total_units_enrolled  # add all units of programs in institution
                    data.append({
                        "institution": institution.name,
                        "outbound_units_enrolled": units_sum
                    })
        return Response(data=data, status=200)
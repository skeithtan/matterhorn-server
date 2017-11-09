from braces.views import UserPassesTestMixin
from django.conf.urls import handler403
from django.contrib.auth.models import *
from django.http import Http404
from django.http import HttpResponseForbidden
from rest_framework.generics import *

from rest_framework.permissions import BasePermission
from rest_framework.response import Response



class MemorandumAdminMixin(ListCreateAPIView,RetrieveUpdateDestroyAPIView):
    permission = Permission.objects.get(codename="crud_memorandum")

    def post(self, request, *args, **kwargs):
        if self.permission not in request.user.user_permissions.all():
            return Response(status=403, data={
                "error": "not authorized to add"
            })

        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if self.permission not in request.user.user_permissions.all():
            return Response(status=403, data={
                "error": "not authorized to edit"
            })
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if self.permission not in request.user.user_permissions.all():
            return Response(status=403, data={
                "error": "not authorized to delete"
            })
        return self.destroy(request, *args, **kwargs)

class StudentAdminMixin(UserPassesTestMixin):
    def test_func(self,user):
        permission = Permission.objects.get(name="Can CRUD Students")
        try:
            return permission in user_logged_in.user_permissions.all()
        except:
            return False

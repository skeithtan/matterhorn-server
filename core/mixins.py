from braces.views import UserPassesTestMixin
from django.conf.urls import handler403
from django.contrib.auth.models import *
from django.http import Http404
from django.http import HttpResponseForbidden

from rest_framework.permissions import BasePermission
from rest_framework.response import Response



class MemorandumAdminMixin(UserPassesTestMixin):
    def test_func(self,user):
        permission = Permission.objects.get(name="Can CRUD Memorandums")
        return permission in user.user_permissions.all()

    def handle_no_permission(self,request):
        raise PermissionDenied("user is not memorandum admin")

class StudentAdminMixin(UserPassesTestMixin):
    def test_func(self,user):
        permission = Permission.objects.get(name="Can CRUD Students")
        try:
            return permission in user_logged_in.user_permissions.all()
        except:
            return False

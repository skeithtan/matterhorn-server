from braces.views import UserPassesTestMixin
from django.conf.urls import handler403
from django.contrib.auth.models import *
from django.http import Http404
from django.http import HttpResponseForbidden
from rest_framework.generics import *

from rest_framework.permissions import BasePermission
from rest_framework.response import Response



class MasterGenericAPIViewMixin(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    codename = None

    def post(self, request, *args, **kwargs):
        permission = Permission.objects.get(codename=self.codename)
        if permission not in request.user.user_permissions.all():
            return Response(status=403, data={
                "error": "not authorized to add"
            })

        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        permission = Permission.objects.get(codename=self.codename)
        if permission not in request.user.user_permissions.all():
            return Response(status=403, data={
                "error": "not authorized to edit"
            })
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        permission = Permission.objects.get(codename=self.codename)
        print(permission)
        print(request.user)
        if permission not in request.user.user_permissions.all():
            return Response(status=403, data={
                "error": "not authorized to delete"
            })
        return self.destroy(request, *args, **kwargs)




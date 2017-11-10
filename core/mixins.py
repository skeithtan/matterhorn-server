from braces.views import UserPassesTestMixin
from django.conf.urls import handler403
from django.contrib.auth.models import *
from django.http import Http404
from django.http import HttpResponseForbidden
from rest_framework import status
from rest_framework.generics import *

from rest_framework.permissions import BasePermission
from rest_framework.response import Response



class MasterGenericAPIViewMixin(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    codename = None

    def get(self, request, *args, **kwargs):
        permission = Permission.objects.get(codename=self.codename)
        if permission not in request.user.user_permissions.all():
            return Response(status=403, data={
                "error": "not authorized to add"
            })

        return self.create(request, *args, **kwargs)

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

        if permission not in request.user.user_permissions.all():
            return Response(status=403, data={
                "error": "not authorized to delete"
            })

        instance = self.get_object()
        instance.delete(user=request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    class ViewOnlyMixin(MasterGenericAPIViewMixin):
        




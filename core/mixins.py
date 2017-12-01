from django.contrib.auth.models import *
from rest_framework import status
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


class MasterGenericAPIViewMixin(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    codename = None

    def get(self, request, *args, **kwargs):
        group = request.user.groups.first()
        permission = Permission.objects.get(codename=self.codename)

        if group is None:
            return Response(status=403, data={
                "error": "user does not belong to any permitted groups"
            })

        if permission not in group.permissions.all():
            return Response(status=403, data={
                "error": "not authorized to view"
            })

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        group = request.user.groups.first()
        permission = Permission.objects.get(codename=self.codename)

        if group is None:
            return Response(status=403, data={
                "error": "user does not belong to any permitted groups"
            })

        if permission not in group.permissions.all():
            return Response(status=403, data={
                "error": "not authorized to view"
            })

        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        group = request.user.groups.first()
        permission = Permission.objects.get(codename=self.codename)

        if group is None:
            return Response(status=403, data={
                "error": "user does not belong to any permitted groups"
            })

        if permission not in group.permissions.all():
            return Response(status=403, data={
                "error": "not authorized to view"
            })
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        group = request.user.groups.first()
        permission = Permission.objects.get(codename=self.codename)

        if group is None:
            return Response(status=403, data={
                "error": "user does not belong to any permitted groups"
            })

        if permission not in group.permissions.all():
            return Response(status=403, data={
                "error": "not authorized to view"
            })

        instance = self.get_object()
        instance.delete(user=request.user.username)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SharedReadOnlyMixin(MasterGenericAPIViewMixin):
    def get(self, request, *args, **kwargs):
        # override to allow users to get without crud permission
        group = request.user.groups.first()
        permission = Permission.objects.get(codename='get_memorandum')

        if group is None:
            return Response(status=403, data={
                "error": "user does not belong to any permitted groups"
            })

        if permission not in group.permissions.all():
            return Response(status=403, data={
                "error": "not authorized to view"
            })

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # only users with crud permissions may post
        group = request.user.groups.first()

        permission = Permission.objects.get(codename='crud_memorandum')
        if group is None:
            return Response(status=403, data={
                "error": "user does not belong to any permitted groups"
            })
        if permission not in group.permissions.all() or group is None:
            return Response(status=403, data={
                "error": "not authorized to view"
            })

        return self.create(request, *args, **kwargs)

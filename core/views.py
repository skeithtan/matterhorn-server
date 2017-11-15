import rest_framework
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from graphene_django.views import GraphQLView


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

        token = Token.objects.get_or_create(defaults={
            "user": user
        })[0]

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
        model = get_object_or_404(self.get_model().current, pk=pk)
        model.undelete()
        serializer = self.get_serializer_class()(model)
        return Response(serializer.data)

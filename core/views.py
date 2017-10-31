from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from graphene_django.views import GraphQLView


@api_view(['GET'])
def private_graph_ql_view(request):
    if request.user.is_authenticated:
        return GraphQLView.as_view(graphiql=True)(request)
    else:
        return Response(data={"error": "You are not signed in."}, status=403)


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
            "token": token.key
        }, status=200)

from django.conf.urls import url
from .views import *


urls = [
    url(r'^sign-in/', SignInView.as_view()),
]
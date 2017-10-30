from django.conf.urls import url
from .views import *


urls = [
    url(r'^institutions/$', InstitutionOverview.as_view()),
    url(r'^institutions/create', InstitutionView.as_view()),
]
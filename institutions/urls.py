from django.conf.urls import url
from .views import *


urls = [
    url(r'^institutions/$', InstitutionView.as_view()),
    url(r'^institutions/(?P<institution_id>(\d+))/$', InstitutionDetail.as_view()),
]
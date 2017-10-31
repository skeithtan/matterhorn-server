from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', InstitutionView.as_view()),
    url(r'^(?P<institution_id>(\d+))/$', InstitutionDetail.as_view()),
]

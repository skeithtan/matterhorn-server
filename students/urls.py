from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', StudentView.as_view())
    # url(r'^(?P<student_id>(\d+))/$', StudentDetail.as_view()),
]
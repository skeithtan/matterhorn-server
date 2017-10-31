from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', ProgramView.as_view()),
    # url(r'^(?P<program_id>(\d+))/$', ProgramView.as_view()),
]
from django.conf.urls import url
from .views import *


report_urls = [
    url(r'unit-reports/$', UnitReportView.as_view()),
]
from django.conf.urls import url
from .views import *


report_urls = [
    url(r'unit_reports/$', UnitReportView.as_view()),
]
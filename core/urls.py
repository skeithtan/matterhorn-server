from django.conf.urls import url
from .views import *


report_urls = [
    url(r'unit-reports/$', UnitReportView.as_view()),
    url(r'student-distribution-reports$', StudentDistributionReportView.as_view()),
    url(r'general-statistics-reports$', GeneralStatisticsReportView.as_view()),
    url(r'outbound-units-reports$', OutboundUnitsReportView.as_view()),
]
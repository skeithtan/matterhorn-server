from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', StudentListCreateView.as_view()),
    url(r'^(?P<pk>(\d+))/$', StudentUpdateDestroyRetrieveView.as_view()),
    url(r'^(?P<pk>(\d+))/residency$', ResidencyAddressHistoryListCreateView.as_view()),
    url(r'^(?P<student_id>(\d+))/residency/(?P<residencyaddresshistory_id>(\d+))$', ResidencyAddressHistoryListCreateView.as_view()),

]
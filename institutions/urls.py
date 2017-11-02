from django.conf.urls import url
from .views import *

institution_urls = [
    url(r'institutions/$', InstitutionListCreateView.as_view()),
    url(r'institutions/(?P<pk>(\d+))/$', InstitutionUpdateDestroyRetrieveView.as_view()),
    url(r'institutions/(?P<institution_id>(\d+))/memorandums/$', MemorandumListCreateView.as_view()),
    url(r'institutions/(?P<institution_id>(\d+))/programs/$', ProgramListCreateView.as_view()),
]

memorandum_urls = [
    url(r'memorandums/(?P<pk>(\d+))/$', MemorandumUpdateDestroyRetrieveView.as_view()),
]

program_urls = [
    url(r'programs/(?P<pk>(\d+))/$', ProgramUpdateDestroyRetrieveView.as_view()),
    url(r'programs/(?P<program_id>(\d+))/offerings/$', ProgramOfferingListCreateView.as_view()),
    url(r'program-offerings/(?P<pk>(\d+))/$', ProgramOfferingRetrieveUpdateDestroyView.as_view()),
]

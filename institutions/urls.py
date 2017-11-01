from django.conf.urls import url
from .views import *

institution_urls = [
    url(r'institution/^$', InstitutionListCreateView.as_view()),
    url(r'institution/^(?P<pk>(\d+))/$', InstitutionUpdateDestroyRetrieveView.as_view()),
    url(r'institution/^(?P<institution_id>(\d+))/memorandums/$', MemorandumListCreateView.as_view()),
    url(r'institution/^(?P<institution_id>(\d+))/programs/$', ProgramListCreateView.as_view()),
]

memorandum_urls = [
    url(r'memorandums/^(?P<pk>(\d+))/$', MemorandumUpdateDestroyRetrieveView.as_view()),
]

program_urls = [
    url(r'programs/^(?P<pk>(\d+))/$', ProgramUpdateDestroyRetrieveView.as_view()),
    url(r'programs/^(?P<program_id>(\d+))/offerings/^(?P<pk>(\d+))/$', ProgramOfferingListCreateView.as_view()),
    url(r'program-offerings/^(?P<pk>(\d+))/$', ProgramOfferingRetrieveUpdateDestroyView.as_view()),
]

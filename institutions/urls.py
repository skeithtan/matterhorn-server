from django.conf.urls import url, include
from .views import *
from .deletions import *

institution_urls = [
    url(r'(?P<pk>(\d+))/$', InstitutionUpdateDestroyRetrieveView.as_view()),
    url(r'$', InstitutionListCreateView.as_view()),
    url(r'(?P<institution_id>(\d+))/memorandums/$', MemorandumListCreateView.as_view()),
    url(r'(?P<institution_id>(\d+))/programs/$', ProgramListCreateView.as_view()),
]

deleted_urls = [
    url(r'institutions/$', DeletedInstitutionsView.as_view()),
    url(r'institutions/(?P<pk>(\d+))/$', DeletedInstitutionUpdateDeletedView.as_view()),
    url(r'institutions/(?P<pk>(\d+))/restore/$', InstitutionRestoreView.as_view()),
    url(r'memorandums/$', DeletedMemorandumsView.as_view()),
    url(r'memorandums/(?P<pk>(\d+))/$', DeletedMemorandumUpdateDeletedView.as_view()),
    url(r'programs/$', DeletedProgramsView.as_view()),
    url(r'programs/(?P<pk>(\d+))/$', DeletedProgramUpdateView.as_view()),
]

memorandum_urls = [
    url(r'(?P<pk>(\d+))/$', MemorandumUpdateDestroyRetrieveView.as_view()),
]

program_urls = [
    url(r'$', ProgramListCreateView.as_view()),
    url(r'(?P<pk>(\d+))/$', ProgramRetrieveUpdateDestroyView.as_view()),
]

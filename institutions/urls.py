from django.conf.urls import url, include
from .views import *
from .archives import *
from .restorations import *

institution_urls = [
    url(r'(?P<pk>(\d+))/$', InstitutionUpdateDestroyRetrieveView.as_view()),
    url(r'(?P<institution_id>(\d+))/memorandums/$', MemorandumListCreateView.as_view()),
    url(r'(?P<institution_id>(\d+))/programs/$', ProgramListCreateView.as_view()),
    url(r'$', InstitutionListCreateView.as_view()),
]

deleted_urls = [
    url(r'institutions/$', ArchivedInstitutionsView.as_view()),
    url(r'institutions/(?P<pk>(\d+))/$', ArchivedInstitutionUpdateDeletedView.as_view()),
    url(r'institutions/(?P<pk>(\d+))/restore/$', InstitutionRestoreView.as_view()),
    url(r'memorandums/$', ArchivedMemorandumsView.as_view()),
    url(r'memorandums/(?P<pk>(\d+))/$', ArchivedMemorandumUpdateDeletedView.as_view()),
    url(r'memorandums/(?P<pk>(\d+))/restore/$', MemorandumRestoreView.as_view()),
    url(r'programs/$', ArchivedProgramsView.as_view()),
    url(r'programs/(?P<pk>(\d+))/$', ArchivedProgramUpdateView.as_view()),
    url(r'programs/(?P<pk>(\d+))/restore/$', ProgramRestoreView.as_view()),
]

memorandum_urls = [
    url(r'(?P<pk>(\d+))/$', MemorandumUpdateDestroyRetrieveView.as_view()),
]

program_urls = [
    url(r'$', ProgramListCreateView.as_view()),
    url(r'(?P<pk>(\d+))/$', ProgramRetrieveUpdateDestroyView.as_view()),
]

academic_year_urls = [
    url(r'terms/$', TermListCreateView.as_view()),
    url(r'$', AcademicYearListCreateView.as_view()),
]

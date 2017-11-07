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
    url(r'programs/$', ProgramListCreateView.as_view()),
    url(r'programs/(?P<pk>(\d+))/$', ProgramRetrieveUpdateDestroyView.as_view()),
]

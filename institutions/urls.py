from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', InstitutionListCreateView.as_view()),
    url(r'^(?P<pk>(\d+))/$', InstitutionUpdateDestroyRetrieveView.as_view()),
    url(r'^(?P<institution_id>(\d+))/memorandums/$', MemorandumCreateView),
    url(r'^(?P<institution_id>(\d+))/memorandums/(?P<pk>(\d+))', MemorandumUpdateDestroyRetrieveView),
]

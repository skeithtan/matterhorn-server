from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', InstitutionView.as_view()),
    url(r'^(?P<institution_id>(\d+))/$', InstitutionDetail.as_view()),
    url(r'^(?P<institution_id>(\d+))/memorandums', MemorandumView.as_view()),
    url(r'^(?P<institution_id>(\d+))/memorandums/(?P<memorandum_id>(\d+))', MemorandumDetail.as_view()),
]

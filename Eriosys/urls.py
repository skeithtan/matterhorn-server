"""Eriosys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from institutions.urls import institution_urls, memorandum_urls, program_urls, deleted_urls as institution_deleted_urls
from core.views import SignInView, PrivateGraphQLView
from students.urls import student_urls, deleted_urls as students_deleted_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sign-in/', SignInView.as_view()),
    url(r'^graphql', PrivateGraphQLView.as_view()),
    url(r'^institutions/', include(institution_urls)),
    url(r'^deleted/', include(institution_deleted_urls + students_deleted_urls)),
    url(r'^students/', include(student_urls)),
    url(r'^memorandums/', include(memorandum_urls)),
    url(r'^programs', include(program_urls))
]

#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from . import views


app_name = 'blog'


urlpatterns = [
    url(r'^indexmaschine/$', views.indexmaschine),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^index/', views.index, name='index'),
    url(r'^$', views.dashboard),
    url(r'^search_results/', views.search_results),
    url(r'^requirement/', views.requirement),
]

# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', view=views.LinkList.as_view(), name='list'),
    url(r'^create/$', view=views.LinkCreate.as_view(), name='create'),
    url(r'^delete/(?P<pk>[\w.@+-]+)$', view=views.LinkDelete.as_view(),
        name='delete'),
    url(r'^update/(?P<pk>[\w.@+-]+)$', view=views.LinkUpdate.as_view(),
        name='update'),
    url(r'^(?P<link_key>[\w.@+-]+)/$', view=views.LinkRedirect.as_view(),
        name='shorten'),
]

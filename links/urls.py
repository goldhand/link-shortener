# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', view=views.LinkList.as_view(), name='list'),
    url(r'^create/$', view=views.LinkCreate.as_view(), name='create'),
    url(r'^(?P<pk>[\w.@+-]+)/$', view=views.LinkRedirect.as_view(),
        name='shorten')
]

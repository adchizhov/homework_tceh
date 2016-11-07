# -*- coding: utf-8 -*-
__author__ = 'adchizhov'

from django.conf.urls import url

from order_form.views import index, MyView, hello

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^form/', MyView.as_view(), name='form'),
    url(r'^hello/', hello)
]
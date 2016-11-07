# -*- coding: utf-8 -*-
__author__ = 'adchizhov'

from django import forms
from django.forms.extras.widgets import SelectDateWidget # какого черта не работает

class MyForm(forms.Form):
    goods = ['socks', 'balls', 'boots']
    amount = forms.IntegerField(min_value=1, max_value=15)
    name_of_product = forms.ChoiceField(choices=(('socks', 'socks'),
                                                 ('balls', 'balls'),
                                                 ('boots', 'boots')))
    name_of_person = forms.RegexField(label='Your first and last name', regex=r"[A-z]{3,15}\s[A-z]{3,20}", # TODO
                                      error_message='Please, input your name and surname!')
    date_of_delivery = forms.DateField(widget=SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),),) # TODO
    adress_of_delivery = forms.CharField(min_length=10, max_length=100)


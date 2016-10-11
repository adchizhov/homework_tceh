# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError
import re

__author__ = 'adchizhov'


class NumberModelForm(FlaskForm):
    number = StringField(label='Input a number', validators=[
        validators.Regexp(r'^^([1-9]|[1-9]\d|100)$', flags=re.IGNORECASE,
                          message='There must be a number between 1 and 100')])

# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError
import re

__author__ = 'sobolevn'


class BlogPostForm(FlaskForm):
    title = StringField(label='Title', validators=[
        validators.Length(min=4, max=140),
    ])
    text = StringField(label='Article Text', validators=[
        validators.Length(min=10, max=3500),
    ])
    author = StringField(label='Author', validators=[
        validators.Regexp(r"[A-z]{3,}\s[A-z]{3,}", flags=re.IGNORECASE,
                          message='There must be a space between name and surname'),
    ])

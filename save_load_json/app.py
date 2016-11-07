# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, json

import config
from forms import BlogPostForm
from models import Storage, BlogPostModel

import logging

logger = logging.getLogger(__name__)

__author__ = 'sobolevn'

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)


@app.route('/', methods=['GET', 'POST'])
def home():
    storage = Storage()

    if request.method == 'POST':
        form = BlogPostForm(request.form)
        if form.validate():
            model = BlogPostModel(form.data)
            storage.adding(model.model_to_dict())
        else:
            logger.error('Someone have submitted an incorrect form!')
    else:
        form = BlogPostForm()

    return render_template(
        'home.html',
        form=form,
        items=storage.items,
    )


if __name__ == '__main__':
    app.run()

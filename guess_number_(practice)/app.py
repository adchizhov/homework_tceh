# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash

import config
from forms import NumberModelForm
from random import randint

import logging

logger = logging.getLogger(__name__)

__author__ = 'adchizhov'

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

sec_number = randint(1, 101)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form = NumberModelForm(request.form)
        if form.validate():
            num = int(form.data['number'])
            if num == sec_number:
                flash('YES! You did it well!', 'info')
            elif num > sec_number:
                flash('Nope, my number is less!', 'info')
            elif num < sec_number:
                flash('NO, my number is greater!', 'info')
        else:
            logger.error('Someone have submitted an incorrect form!')
    else:
        form = NumberModelForm()

    return render_template(
        'home.html',
        form=form)

if __name__ == '__main__':
    app.run()

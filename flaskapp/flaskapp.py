# This is the Peak front-end.

from flask import Flask, render_template, flash, redirect, request

from flaskapp.forms import QuestionForm

import requests
import os

application = Flask(__name__)

@application.route('/healthz')
def healthz():
    """
    Check the health of this peakweb instance. OCP will hit this endpoint to verify the readiness
    of the peakweb pod.
    """
    return 'OK'

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/new_question/', methods=('GET', 'POST'))
def new_question():
    form = QuestionForm()
    if form.validate_on_submit():
        flash("Successfully submitted question \"%s\"" % (form.summary.data))
        return redirect('/new_question/')

    return render_template('newquestion.html', form=form)

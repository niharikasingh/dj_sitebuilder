# app/site/views.py

from flask import g, jsonify, render_template, request
from flask_login import current_user, login_required
import ast
import json
import os

from . import site
from ..models import Site

from ..static.python import format_data, print_docs, email_attachments, zip_docs, delete_folder, make_cardlist
from ..static.python.check_admin import check_admin
from ..static.python.check_permission import check_permission



# get requested site

@site.url_value_preprocessor
def get_site_name(endpoint, values):
    site_url_slug = values.pop('site_url_slug')
    query = Site.query.filter_by(site_url_slug=site_url_slug)
    g.site = query.first_or_404()


@site.route('/')
@login_required
def site_home():
    check_permission(g.site)

    site_url_slug = g.site.site_url_slug

    # calibrate site-specific paths: static, upload folder

    app_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    path2model = os.path.join(app_root, 'static/custom_site_data', site_url_slug, 'static/tmp/model.txt')

    cardlist = make_cardlist.make_cardlist(path2model)
    return render_template('site/layout.html', cardlist=cardlist)


@site.route('/admin')
@login_required
def admin():
    check_admin()

    site_url_slug = g.site.site_url_slug

    currModel = {}

    # calibrate site-specific paths: static, upload folder

    app_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    path2model = os.path.join(app_root, 'static/custom_site_data', site_url_slug, 'static/tmp/model.txt')

    with open(path2model) as model:
        currModel = json.load(model)

    return render_template('site/index.html', currModel=json.dumps(currModel))


@site.route('/submitdata/', methods=['GET', 'POST'])
def submit():
    site_url_slug = g.site.site_url_slug

    # calibrate site-specific paths: static, upload folder

    app_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    path2static = os.path.join(app_root, 'static/custom_site_data', site_url_slug, 'static')
    path2documents = os.path.join(path2static, 'documents')

    # Store posted_data in variable card_dictionary

    card_dictionary = ast.literal_eval(request.form['submit_data'])

    if 'STUDENT_EMAIL' in card_dictionary:

        # Format data in card_dictionary
        card_dictionary = format_data.format_data(card_dictionary, path2documents)

        # Create draft documents from templates:
        print_docs.print2docs(card_dictionary, path2documents)

        # Zip folder containing draft documents
        zip_docs.zip2folder(card_dictionary, path2documents)

        # Email attachment to user
        email_attachments.send_emails(card_dictionary, path2documents)

        # Delete zip folder from documents
        delete_folder.delete_folder(card_dictionary, path2documents)

        # # Email a calendar invite to student and clinical instructor regarding client's next court date.
        # email_calendar.email_calendar(card_dictionary)

    return jsonify({})


@site.route('/savecurrmodel', methods=['GET', 'POST'])
def post_data():
    site_url_slug = g.site.site_url_slug

    currModel = {}
    currModel = json.loads(request.args.get("payload"))

    # calibrate site-specific paths: static, upload folder

    app_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    path2static = os.path.join(app_root, 'static/custom_site_data', site_url_slug, 'static')

    with open(os.path.join(path2static, 'tmp/model.txt'), 'w') as write_file:
        json.dump(currModel, write_file, indent=4, sort_keys=True)
    return "OK"

@site.route('/loadtemplate', methods = ['GET'])
def loadtemplate():
    loadFileName = request.args.get("payload")
    loadTemplate = {}
    with open("/templates/jstemplates/" + loadFileName) as loadFile:
        loadTemplate = loadFile.readlines()
    return " ".join(loadTemplate), 200

def splititup(i):
    j = i.split('<div class="container">',1)[1]
    jj = j.split('<div class="col s12"')
    nlist = []
    for x in jj:
        nlist.append('<div class="col s12"'+x)
    for n in nlist:
        if n.find('VET_ID') != -1:
            import re
            n = re.sub('None', '', n)
            # print n
            return n

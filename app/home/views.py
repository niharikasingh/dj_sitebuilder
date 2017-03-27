# app/home/views.py

from flask import abort, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import home
from ..models import Site, SitePermission


@home.route('/')
def homepage():
    """
    Render homepage
    """

    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render dashboard template
    """

    return render_template('home/dashboard.html', title="Dashboard")


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title='Dashboard')


@home.route('/sitedashboard')
@login_required
def site_dashboard():
    # for regular users only
    if current_user.is_admin:
        return redirect(url_for(admin_dashboard))

    # note - consider use of inner join below instead of for loop. i'm not sure how to implement with sqlalchemy though.

    auth_sites = SitePermission.query.filter_by(user_id=current_user.id).all()
    sites = []
    for auth_site in auth_sites:
        site = Site.query.filter_by(id=auth_site.site_id).first()
        sites.append(site)

    return render_template('admin/sites/user_sites.html', sites=sites, title='User Sites')
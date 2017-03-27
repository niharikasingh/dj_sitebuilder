# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from shutil import rmtree
from werkzeug.utils import secure_filename
import os

from . import admin
from forms import CreateSiteForm, DepartmentForm, FileUploadForm, RoleForm, UserAssignForm
from .. import db
from ..models import Department, Role, Site, SitePermission, User
from ..static.python.build_site_dirs import build_site_dirs
from ..static.python.check_admin import check_admin


@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    check_admin()

    departments = Department.query.all()

    return render_template('admin/departments/departments.html',
                           departments=departments, title='Departments')


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    check_admin()

    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data,
                                description=form.description.data)
        try:
            # add department to the database
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department.')
        except:
            # in case department name already exists
            flash('Error: department name already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_departments'))

    # load department template
    return render_template('admin/departments/department.html', action="Add",
                           add_department=add_department, form=form,
                           title="Add Department")


@admin.route('/departments/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit_department(id):
    check_admin()

    add_department=False

    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash('Department edited successfully.')

        return redirect(url_for('admin.list_departments'))

    form.description.data = department.description
    form.name.data = department.name
    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")


@admin.route('departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    check_admin()

    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('Department deleted.')

    return redirect(url_for('admin.list_departments'))


@admin.route('/roles')
@login_required
def list_roles():
    check_admin()
    """
    List all roles
    """
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """
    Add a role to the database
    """
    check_admin()

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)

        try:
            # add role to the database
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except:
            # in case role name already exists
            flash('Error: role name already exists.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    # load role template
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title='Add Role')


@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """
    Edit a role
    """
    check_admin()

    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    form.description.data = role.description
    form.name.data = role.name
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title="Edit Role")


@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from the database
    """
    check_admin()

    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')

    # redirect to the roles page
    return redirect(url_for('admin.list_roles'))


@admin.route('/sites')
@login_required
def list_sites():
    check_admin()
    """
    List all sites
    """
    sites = Site.query.all()
    return render_template('admin/sites/sites.html',
                           sites=sites, title='Sites')


@admin.route('/sites/add', methods=['GET', 'POST'])
@login_required
def add_site():
    '''
    Includes main logic for creating new site, including custom site data directory
    '''

    check_admin()

    add_site = True

    form = CreateSiteForm()
    if form.validate_on_submit():
        site_url_slug = form.name.data.replace(' ', '')
        site = Site(name=form.name.data,
                    description=form.description.data,
                    site_url_slug=site_url_slug)
        try:
            # add site to the database
            db.session.add(site)
            db.session.commit()

            # create site directory
            build_site_dirs(site_url_slug)

            flash('You have successfully added a new site.')
        except:
            # in case department name already exists
            flash('Error')

        # redirect to departments page
        return redirect(url_for('admin.list_sites'))

    # load department template
    return render_template('admin/sites/site.html', action="Add",
                           add_site=add_site, form=form,
                           title="Add Site")


@admin.route('/sites/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_site(id):
    check_admin()

    '''
    IMPORTANT: add functionality to change name of custom site directories
    '''

    add_site=False

    site = Site.query.get_or_404(id)
    form = CreateSiteForm(obj=site)
    if form.validate_on_submit():
        old_folder_name = site.site_url_slug
        # modify database information

        site.name = form.name.data
        site.site_url_slug = form.name.data.replace(' ', '')
        site.description = form.description.data
        db.session.commit()

        # modify site directory information

        root_site_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                      'static/custom_site_data'))
        os.rename(os.path.join(root_site_path, old_folder_name), os.path.join(root_site_path, site.site_url_slug))

        flash('Site edited successfully.')

        return redirect(url_for('admin.list_sites'))

    form.description.data = site.description
    form.name.data = site.name
    return render_template('admin/sites/site.html', action="Edit",
                           add_site=add_site, form=form,
                           site=site, title="Edit Site")


@admin.route('sites/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_site(id):
    check_admin()

    site = Site.query.get_or_404(id)
    site_permissions = SitePermission.query.all()

    # remove database entries
    for entry in site_permissions:
        db.session.delete(entry)
    db.session.delete(site)
    db.session.commit()

    # remove site-specific file directories

    site_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                             'static/custom_site_data',
                                             site.site_url_slug))
    rmtree(site_path, ignore_errors=True)

    flash('Site deleted.')

    return redirect(url_for('admin.list_sites'))

@admin.route('/sites/fileupload', methods=['GET','POST'])
@login_required
def upload_file():
    check_admin()

    form = FileUploadForm()

    root_site_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                  'static/custom_site_data'))

    if form.validate_on_submit():
        file = form.file.data
        site_path = form.site.data.site_url_slug
        upload_path = os.path.join(root_site_path, site_path, 'static\\documents\\doc_templates')
        filename = secure_filename(file.filename)
        file.save(os.path.join(upload_path, filename))
        return redirect(url_for('home.admin_dashboard'))

    flash('File Upload Successful.')

    return render_template('admin/sites/uploadfile.html',
                           form=form, title='File Upload')


@admin.route('/users')
@login_required
def list_users():
    check_admin()

    users = User.query.all()
    return render_template('admin/users/users.html',
                           users=users, title='Users')


@admin.route('/users/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_user(id):
    check_admin()

    user = User.query.get_or_404(id)

    if user.is_admin:
        abort(403)

    form = UserAssignForm(obj=user)
    if form.validate_on_submit():
        # add assignment to users table

        try:
            old_permission = SitePermission.query.filter_by(user_id=user.id).first()
            db.session.delete(old_permission)
        except:
            pass

        user.department = form.department.data
        user.role = form.role.data
        user.site = form.site.data

        # add assignment to site_permissions table

        site_query_obj = form.site.data
        permission = SitePermission(user_id=user.id, site_id=site_query_obj.id)

        db.session.add(permission)
        db.session.add(user)
        db.session.commit()
        flash('Request successful.')

        return redirect(url_for('admin.list_users'))

    return render_template('admin/users/user.html',
                           user=user, form=form, title='Assign User')

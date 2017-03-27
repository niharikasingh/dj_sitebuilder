# app/admin/forms.py

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_login import current_user
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Department, Role, User, Site

class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """

    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UserAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to users
    """

    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label='name')
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label='name')
    site = QuerySelectField(query_factory=lambda: Site.query.all(),
                            get_label='name')
    submit = SubmitField('Submit')

class CreateSiteForm(FlaskForm):
    """
    Form for users to create a new site
    """

    name = StringField('Site Name', validators=[DataRequired()])
    description = StringField('Site Description', validators=[DataRequired()])
    submit = SubmitField('Submit', validators=[DataRequired()])

    def validate_name(self, field):
        if Site.query.filter_by(name=field.data).first():
            raise ValidationError('Sorry, that site name is already in use. Choose another name.')

    def validate_admin(self, field):
        user = User.query.filter_by(username=current_user())
        if not user.is_admin:
            raise ValidationError('Sorry, this account is not authorized to create new sites.')

class FileUploadForm(FlaskForm):
    """
    Form to upload files to a site (admin only)
    """

    site = QuerySelectField('Choose a site', query_factory=lambda: Site.query.all(),
                            get_label='name')
    file = FileField('Choose a file', validators=[FileRequired(),
                                                  FileAllowed(['docx'], 'Word documents in .docx format.')])
    submit = SubmitField('Submit')
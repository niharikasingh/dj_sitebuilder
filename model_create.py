from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dj_admin:dj2017@localhost/dj_v2'
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    """
    Create a default user table
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    site_id = db.Column(db.Integer, db.ForeignKey('sites.id'))
    is_admin = db.Column(db.Boolean, default=False)
    sites = db.relationship('SitePermission', backref='user', lazy='dynamic')

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        """
         Set password to hashed password
         """
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256:50000', salt_length=8)

    def verify_password(self, password):
         """
        Check password
         """
         return check_password_hash(self.password_hash, password)

    # def __repr__(self):
    #     return '<User: {}>'.format(self.name)


@login_manager.user_loader
def load_user(user_id):
     return User.query.get(int(user_id))


class Department(db.Model):
    """
    Create Department table
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(264))
    users = db.relationship('User', backref='department', lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)


class Role(db.Model):
    """
    Create Role table
    """
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(264))
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)

class Site(db.Model):
    """
    Create Sites table
    """

    __tablename__ = 'sites'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(264))
    site_url_slug = db.Column(db.String(60), unique=True)
    json_config = db.Column(db.String(10000))
    users = db.relationship('User', backref='site', lazy='dynamic')

    def __repr__(self):
        return '<Site: {}>'.format(self.name)


class SitePermission(db.Model):
    """
    Create site permissions table
    """

    __tablename__ = 'site_permissions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    site_id = db.Column(db.Integer, db.ForeignKey('sites.id'))
    can_edit = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<SitePermission: {}>'.format(self.id)






db.create_all()
db.session.commit()



# from sqlalchemy import create_engine
# engine = create_engine("mysql://dj_admin:dj2017@localhost/dj_v2")
#
# # from sqlalchemy import inspect
# # inspector = inspect(engine)
#
# # for table_name in inspector.get_table_names():
# #    for column in inspector.get_columns(table_name):
# # #        print("Column: %s" % column['name'])
#
#
# x = User.query.filter_by(email='wpalin@gmail.com').first()
# print x.email
# print x.first_name
# print x.last_name

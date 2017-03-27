'''
Helper function to check whether a given user has permission to access a given site.
'''

from flask import abort
from flask_login import current_user

from ...models import Site, SitePermission


def check_permission(site):
    site_query_obj = Site.query.filter_by(name=site.name).first()
    site_id = site_query_obj.id

    if current_user.is_admin:
        return True

    elif SitePermission.query.filter_by(user_id=current_user.id, site_id=site_id).first() is not None:
        return True
    else:
        abort(403)
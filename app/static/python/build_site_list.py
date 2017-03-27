# app/static/python/build_site_list.py

"""
Helper function used in app/__init__.py to build site list to import.
"""

from ...models import Site


def build_site_list():
    sites = Site.query()
    sites_to_register = []

    for site in sites:
        sites_to_register.append(site.name)

    return sites_to_register
# app/static/python/site_builder.py

"""
Helper function to create new site directories.
"""

import os
from shutil import copytree


def build_site_dirs(sitename):
    # copies template directory into new directory named 'sitename' from site creation form

    app_root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    source = os.path.join(app_root_dir, 'new_site_dirs_template')
    destination = os.path.join(app_root_dir, 'custom_site_data', str(sitename))

    copytree(source, destination)
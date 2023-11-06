# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)

from pelicanconf import *

import py_code.urls_publish as urls_publish
relative_url, absolute_url = urls_publish.make_functions()

JINJA_FILTERS = {
                'relative_url': relative_url, 
                'absolute_url': absolute_url,
                'bust_file_cache': bust_file_cache,
                'slugify': slugify,
                'filter_projects': filter_projects
                }

MARKDOWN = {
    'extensions': ['codehilite', 'extra', 'meta', 'admonition', 'toc',
                   TemplateBlockExtension(filters=JINJA_FILTERS)],
    'extension_configs': {
        'codehilite': {'css_class': 'highlight'},
        'extra': {'attr_list': {}},
        'meta': {},
        'admonition': {},
        'toc': {}
    },
    'output_format': 'html5',
}

# TODO: Modify this whole file so that relative and absolute
# URLs work correctly.

# If your site is available via HTTPS, make sure SITEURL begins with https://
if SITE["baseurl"] is not None:
    SITEURL = SITE["url"] + "/" + SITE["baseurl"] 
else:
    SITEURL = SITE["url"] 
RELATIVE_URLS = True 

DELETE_OUTPUT_DIRECTORY = True

#GOOGLE_ANALYTICS = ""
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
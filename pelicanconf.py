#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'DotPodcast Inc'
SITENAME = u'DotPodcast'
SITEURL = 'http://localhost:8000'

PATH = 'content'
TIMEZONE = 'EST'
DEFAULT_LANG = u'en'
THEME = 'themes/attila'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {}
    },
    'output_format': 'html5',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10
RELATIVE_URLS = False
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}/index.html'

# Theme-specific settings
HEADER_COVER = 'images/header.jpg'
MENUITEMS = (
    ('Home', '/'),
    ('Feed spec v1', '/spec-v1'),
    ('Taxonomies', '/taxonomies'),
    ('Building a hosting service', '/guides/hosting'),
    ('Building a directory', '/guides/directories'),
    ('Building a podcast app', '/guides/apps'),
    ('Blog', '/blog.html')
)

DIRECT_TEMPLATES = ['blog']
PAGINATED_DIRECT_TEMPLATES = ['blog']

# Authors
AUTHORS_BIO = {
    'mark': {
        'name': "Mark Steadman",
        'cover': 'images/mark-cover.jpg',
        'image': 'images/mark-avatar.jpg',
        'website': 'https://steadman.io/',
        'location': 'Birmingham, UK',
        'bio': 'Mark runs the Podiant podcast hosting service, and co-authors the feed spec at DotPodcast',
        'twitter': 'iamsteadman',
        'github': 'iamsteadman'
    }
}

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
    ('Home', ''),
    ('Blog', 'blog.html')
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
        'bio': 'Mark runs the Podiant podcast hosting service, and handles the JSON Feed spec extension at DotPodcast',
        'twitter': 'iamsteadman',
        'github': 'iamsteadman'
    }
}

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Julian Daeumer'
SITENAME = u'Binary Research'
SITESUBTITLE = u'reverse engineering, binary analysis, data analysis'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('devttys0', 'http://www.devttys0.com'),
        ('Bitlackeys Research', 'http://www.bitlackeys.org/'),)
#         (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('@_SYS_V', 'https://twitter.com/_SYS_V'),)
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ['md']
PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = [
    'summary',       # auto-summarizing articles
    'feed_summary',  # use summaries for RSS, not full articles
    'ipynb.liquid',  # for embedding notebooks
    'liquid_tags.img',  # embedding images
    'liquid_tags.video',  # embedding videos
    'liquid_tags.include_code',  # including code blocks
    'liquid_tags.literal'
]
IGNORE_FILES = ['.ipynb_checkpoints']

# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

ENABLE_MATHJAX = True

THEME = 'themes/pelican-themes/bootstrap'

TWITTER_USERNAME = '_SYS_V'
GITHUB_USERNAME = 'daeumerj'
STACKOVERFLOW_ADDRESS = 'https://reverseengineering.stackexchange.com/users/18317/sys-v'

# Footer info
LICENSE_URL = "https://github.com/daeumerj/daeumerj.github.io-source/blob/master/LICENSE"
LICENSE = "MIT"

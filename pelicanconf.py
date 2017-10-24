#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mariatta'
AUTHORS = {
    'Mariatta': 'http://mariatta.ca'
}
SITENAME = 'mariatta.ca'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/mariatta'),
          ('GitHub', 'https://github.com/Mariatta'),
          ('IMDb', 'http://www.imdb.com/name/nm7641957/'),
          ('LinkedIn', 'https://linkedin.com/in/mariatta'),
          ('Paypal.me', 'https://www.paypal.me/mariatta'),
          ('Instagram', 'https://www.instagram.com/mariatta81/'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DEFAULT_DATE = 'fs'

THEME = 'aboutwilson'
DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ['img']

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'Flex'

AUTHOR = 'Cleveland PyLadies'
SITENAME = 'Cleveland PyLadies'
SITEURL = 'https://clepyladies.github.io/pyladies-official'
SITESUBTITLE = 'A community for PyLadies, PyNonbinaries, the PyCurious'
SITELOGO = SITEURL + '/content/images/pylady_geek_full_dark_green.png'

BROWSER_COLOR = '#810016'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2018

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

MAIN_MENU = True

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Contribute to our Medium publication', 'https://medium.com/cleveland-pyladies'),
         ('PyLadies Global', 'https://www.pyladies.com'),
         ('First Time Open-Source Contributors', 'https://www.firsttimersonly.com/'),)

# Social widget
SOCIAL = (('Meetup', 'https://www.meetup.com/cle-pyladies'),
          ('Twitter', 'https://www.twitter.com/clepyladies'),
          ('Facebook', 'https://www.facebook.com/clepyladies'),
          ('Instagram', 'https://www.instagram.com/clepyladies'),
          ('Cleveland Tech Slack', 'https://cleveland-tech.slack.com'),
          ('PyLadies Global Slack', 'https://slackin.pyladies.com'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

LINKS_WIDGET_NAME = 'Contribute to Open-Source'
SOCIAL_WIDGET_NAME = 'Connect'

DISPLAY_PAGES_ON_MENU = True

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sun Zhennian'
SITENAME = u"""<span style="color:#AA1032;">SUN ZHENNIAN'S BLOG</span>"""
SITEURL = ''
PATH="content"
# Regional Settings
TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {'en': '%a, %d %b %Y'}
LOCALE = ('usa', 'jpn',  # On Windows
    'en_US', 'ja_JP'     # On Unix/Linux
    )
DEFAULT_LANG = u'en'

# Plugins and extensions
PLUGIN_PATHS = ["plugins", "plugins"]
PLUGINS = ['org_emacs_reader','pelican-toc','sitemap']
THEME = 'themes/elegant'
# Appearance
TYPOGRIFY = True
DEFAULT_PAGINATION = False
DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = True
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
STATIC_PATHS = ['theme/images', 'images']
DUOSHUO_SHORTNAME = "sunzhennian"
########################################################################################################################
### Sitemap configuration###################
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

### Elegant configurations###################
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'Stay in Touch'
RELATED_POSTS_LABEL = 'Keep Reading'
SHARE_POST_INTRO = 'Like this post? Share on:'
COMMENTS_INTRO = u'<h3>Comments</h3>'

# SMO
TWITTER_USERNAME = u'talham_'
FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'
RECENT_ARTICLES_COUNT=15

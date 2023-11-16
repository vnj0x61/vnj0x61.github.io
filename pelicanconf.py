AUTHOR = 'vnj0x61'
SITENAME = 'vnj0x61 - write-ups'
SITEURL = 'https://vnj0x61.github.io'

THEME = 'themes/storm'

PATH = './content'
OUTPUT_PATH = './static'
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".hg", ".git", ".bzr"]

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_RSS = 'feeds.xml'


# Blogroll
LINKS = (('packet storm', 'https://packetstormsecurity.com/'),
         ('trinler', 'https://www.trinler.net/service/tools/ipcalc/'),
         ('deepl', 'https://www.deepl.com/'),
         )

# Social widget
SOCIAL = (('Home', 'https://vnj0x61.github.io/'),
          ('Github', 'https://github.com/vnj0x61'),
          ('packetstorm', 'https://packetstormsecurity.com/'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

import re, logging
from os import environ
from Script import script

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Auto_Filters_Bot')
API_ID = environ.get('API_ID', '23081466')
if len(API_ID) == 0:
    print('Error - API_ID is missing, exiting now')
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get('API_HASH', 'dbc665db1489f9d3cfd8de4a52f1ad4b')
if len(API_HASH) == 0:
    print('Error - API_HASH is missing, exiting now')
    exit()
BOT_TOKEN = environ.get('BOT_TOKEN', '')
if len(BOT_TOKEN) == 0:
    print('Error - BOT_TOKEN is missing, exiting now')
    exit()
PORT = int(environ.get('PORT', '8080'))

# Bot pics
PICS = (environ.get('PICS', '')).split()

# Bot Admins
ADMINS = environ.get('ADMINS', '1764208280')
if len(ADMINS) == 0:
    print('Error - ADMINS is missing, exiting now')
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS', '-1001934552402 -1002010605912 -1002031195023 -1001462998715').split()]
AUTH_CHANNEL = [int(auth_channels) for auth_channels in environ.get('AUTH_CHANNEL', '-1001982864590').split()]
LOG_CHANNEL = environ.get('LOG_CHANNEL', '-1001867416281')
if len(LOG_CHANNEL) == 0:
    print('Error - LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)
    
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '-1002076397304')
if len(SUPPORT_GROUP) == 0:
    print('Error - SUPPORT_GROUP is missing, exiting now')
    exit()
else:
    SUPPORT_GROUP = int(SUPPORT_GROUP)
    
OPENAI_API = environ.get('OPENAI_API', '')
if len(OPENAI_API) == 0:
    print('Warning - OPENAI_API is empty')

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "")
if len(DATABASE_URL) == 0:
    print('Error - DATABASE_URL is missing, exiting now')
    exit()
DATABASE_NAME = environ.get('DATABASE_NAME', "")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/FilmySpotSupport_bot')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/filmyspotupdate')

# Bot settings
AUTO_FILTER = is_enabled((environ.get('AUTO_FILTER', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SPELL_CHECK = is_enabled(environ.get("SPELL_CHECK", "True"), True)
SHORTLINK = is_enabled((environ.get('SHORTLINK', "False")), False)
DELETE_TIME = int(environ.get('DELETE_TIME', 300)) # Add time in seconds
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
WELCOME = is_enabled((environ.get('WELCOME', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
LINK_MODE = is_enabled(environ.get("LINK_MODE", "True"), True)
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_BTN = int(environ.get('MAX_BTN', 10))
LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]

# Other
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "ziplinker.net")
SHORTLINK_API = environ.get("SHORTLINK_API", "37752ccfafb8030f3614dd384405293d5a629203")
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 43200)) # Add time in seconds
IS_VERIFY = is_enabled(environ.get("IS_VERIFY", "True"), True)
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
TUTORIAL = environ.get("TUTORIAL", "https://t.me/filmyspotupdate")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/filmyspotupdate")
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
PM_SEARCH = is_enabled('PM_SEARCH', True)
PM_FSUB = is_enabled('PM_FSUB', False)


# stream features vars
FILE_TO_LINK_APPURL = environ.get("DIRECT_GEN_URL", "https://filmyspotmovie-16c4510caa97.herokuapp.com") 
FILE_TO_LINK_LOG = int(environ.get("DIRECT_GEN_DB", "-1002041057749"))


# Log
LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("AUTO_FILTER is enabled.\n" if AUTO_FILTER else "AUTO_FILTER is disabled.\n")
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += (f"FILE_CAPTION enabled with value {FILE_CAPTION}, your files will be send along with this customized caption.\n" if FILE_CAPTION else "No FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("LONG_IMDB_DESCRIPTION enabled.\n" if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled, Plot will be shorter.\n")
LOG_STR += ("SPELL_CHECK Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK else "SPELL_CHECK Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in IMDB_TEMPLATE, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB_TEMPLATE is {IMDB_TEMPLATE}"

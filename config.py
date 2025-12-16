# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "20831812"))
API_HASH = getenv("API_HASH", "9af7c0491f6f09017c3f491f571da3fe")
BOT_TOKEN = getenv("BOT_TOKEN", "8580296884:AAFtnm2lHYtwJnnc1Lc9DIheJ5ZH_EGUC3k")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6288683814").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://aryanktr92:pBw41GcqtlnpFjwq@cluster0.nqsufox.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002891775044")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002974156344"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "gplinks.com")
AD_API = getenv("AD_API", "5da82a1b7c115deb5cf927446ec67ab5ef01bf17")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)

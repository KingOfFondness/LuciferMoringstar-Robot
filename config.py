# MIT License
# Copyright (c) 2022 Muhammed
import os, re
search = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Creator
CREATOR_NAME = os.environ.get("CREATOR_NAME", "KingOfFondness")
CREATOR_USERNAME = os.environ.get("CREATOR_USERNAME", "KingOfFondness")

# Account
API_HASH = os.environ.get("API_HASH", "da59e4e56ec4fe35af603bd30208ecc5")
API_ID = os.environ.get("API_ID", "12635510")
# About Bot
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5458262263:AAE-nncwSdmSLJ2HwU0E3qJKa8Zb69n5iAE")
PICS = os.environ.get("PICS", "https://telegra.ph/file/034d53b5ed1d920ecab8b.jpg")
# Database
DATABASE_NAME = os.environ.get("DATABASE_NAME", "LuciferMoringstar-Robot")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://{Username}:{Passs}@cluster0.{clusterID}.mongodb.net/myFirstDatabase?retryWrites=true{iD}=majority")
# Chats & Users
ADMINS = os.environ.get("ADMINS", "1130215726 ")
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "fondness MoviesHD")
AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "--1001703747432")
CHANNELS = [int(ch) if search.search(ch) else ch for ch in os.environ.get("CHANNELS", "--1001293479644").split()]
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001703747432")
GET_FILECHANNEL = os.environ.get("GET_FILECHANNEL", "-1001739141872")
FILTER_DEL_SECOND = int(os.environ.get("FILTER_DEL_SECOND", "600"))

# AutoFilter
AUTH_GROUPS = os.environ.get("AUTH_GROUPS", "")
AUTH_USERS = [int(user) if search.search(user) else user for user in os.environ.get('AUTH_USERS', '').split()]
FILTER_BUTTONS = os.environ.get("FILTER_BUTTONS", "10")
PROTECT_FILES = is_enabled((os.environ.get('PROTECT_FILES', "True")), True) 

import os
import time

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("6484301475:AAHh1svu7-ZzVNgpXQmf8nHQbocLEMlGboI", "")


    # Get from my.telegram.org (or @UseTGXBot)
    API_ID = int(os.environ.get("API_ID", 29849415)


    # Get from my.telegram.org (or @UseTGXBot)
    API_HASH = os.environ.get("0dd6c10897b85d7f10a8dcdeb74f8b8a", "")
    
    
    # Database URL from https://cloud.mongodb.com/
    DATABASE_URI = os.environ.get("mongodb+srv://Hacker:<sudipsaha2006>@cluster0.mcdrruk.mongodb.net/?retryWrites=true&w=majority", "")


    # Your database name from mongoDB
    DATABASE_NAME = str(os.environ.get("Hacker", "Cluster0"))


    # ID of users that can use the bot commands
    AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())


    # To save user details (Usefull for getting userinfo and total user counts)
    # May reduce filter capacity :(
    # Give yes or no
    SAVE_USER = os.environ.get("SAVE_USER", "no").lower()


    # Go to https://dashboard.heroku.com/account, scroll down and press Reveal API
    # To check dyno status
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")


    # OPTIONAL - To set alternate BOT COMMANDS
    ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "add")
    DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMDD", "del")
    DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMDD", "delall")
    CONNECT_COMMAND = os.environ.get("CONNECT_COMMANDD", "connect")
    DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMANDD", "disconnect")


    # To record start time of bot
    BOT_START_TIME = time.time()

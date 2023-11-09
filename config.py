#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6691873935:AAFVmR4imCzJZAC6Gxv_A98m0H0YFlvmn7g")
    API_ID = int(os.environ.get("API_ID", "22609670"))
    API_HASH = os.environ.get("API_HASH", "3506d8474ad1f4f5e79b7c52a5c3e88d")
    AUTH_USERS = "6981453498"



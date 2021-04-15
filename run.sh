#!/bin/bash
cd $BOTDIR
/usr/local/bin/python -m pip install --upgrade pip
pip3 install --no-cache-dir -r requirements.txt
python3 /python/DiscordBot/DiscordBot.py
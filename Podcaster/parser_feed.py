"""
    My Feed Parser for Podcaster module
"""

import feedparser
from Podcaster import *
from colorize import colorize
from Helper import dash

def get_feed(feed_url):
    return feedparser.parse(feed_url)

def get_podcast(key, old=False):
    if old:
        return OLD_PODCASTS[key]

    return PODCASTS[key]

def list_podcast():
    print(colorize("Feeds With New Podcasts", bold=True))
    for key in PODCASTS.keys():
        podcast = PODCASTS[key]
        name = podcast["name"]
        day = podcast["day"]
        url = podcast["url"]
        color_key = colorize(key, color="red", bold=True)
        color_name = colorize(name, color="green", bright=True)
        color_day = colorize(day, color="cyan", bright=True)
        print(f"Key: {color_key} Podcast: {color_name} Available: {color_day} ")

    print(colorize("No Longer New Podcasts", bright=True))
    for key in OLD_PODCASTS.keys():
        podcast = OLD_PODCASTS[key]
        name = podcast["name"]
        day = podcast["day"]
        url = podcast["url"]
        color_key = colorize(key, color="red", bold=True)
        color_name = colorize(name, color="green", bright=True)
        color_day = colorize(day, color="magenta", bright=True)
        print(f"Key: {color_key} Podcast: {color_name} Available: {color_day} ")


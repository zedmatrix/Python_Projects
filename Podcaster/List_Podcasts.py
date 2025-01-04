#!/usr/bin/env python3
from Podcaster import *
from Parser import parse_arguments
from parser_feed import get_feed, get_podcast, list_podcast
from dictionary import Create_Dictionary
from Helper import dash, Display, WritePodcast

if __name__ == "__main__":
    my_dict = Create_Dictionary()
    args = parse_arguments()
    if args.list:
        print(f" Pretty Date: {my_dict["fulldate"]}")
        list_podcast()
        exit(0)

    elif args.podcast:
        print(f"Selected Podcast: {args.podcast}")
        podkey = args.podcast
        podcast = get_podcast(podkey, old=False)

    elif args.oldcast:
        print(f"Selected Podcast: {args.oldcast}")
        podkey = args.oldcast
        podcast = get_podcast(podkey, old=True)

    else:
        print(f"{Usage['message']} .Exiting.")
        exit(1)

    print(f" Pretty Date: {my_dict["fulldate"]}")
    Feed_URL = podcast["url"]

    print(f"Downloading Podcast: {podcast["name"]}")
    print(f"Feed URL: {Feed_URL}")
    print(dash(symbol="*", count=40))

    print(f" Writing To Directory: {my_dict["outdir"]}")

    my_feed = get_feed(Feed_URL)
    max_podcasts = len(my_feed.entries) - 1
    if args.index > max_podcasts:
        index = max_podcasts
    else:
        index = args.index
    print(f"Total Podcasts: {max_podcasts} Downloading Index: {index}")

    latest = my_feed["entries"][index]
    Display(latest)
    WritePodcast(podkey.upper(), podcast["name"], my_dict["outdir"], latest)

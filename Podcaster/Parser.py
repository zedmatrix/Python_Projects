"""
    My Argument Parser for Podcaster module

"""

import argparse
from Podcaster import *

def parse_arguments():
    parser = argparse.ArgumentParser(description="Podcaster Argument Parser")
    parser.add_argument(
        '-p', '--podcast',
        choices=PODCASTS.keys(),
        help="New Episodes Available On Specific Days."
    )
    parser.add_argument(
        '-o', '--oldcast',
        choices=OLD_PODCASTS.keys(),
        help="No New Episodes Available from These Podcasts."
    )
    parser.add_argument(
        '-l', '--list',
        action='store_true',
        help="List all available podcasts and their URLs."
    )
    parser.add_argument(
        '-i','--index',
        type=int, default=0,
        help="Optional Index Number. Default=0 latest."
    )
    return parser.parse_args()

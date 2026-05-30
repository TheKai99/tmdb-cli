import argparse
from api import get_popular
from api import get_now_playing
from api import get_top_rated
from api import get_upcoming


parser = argparse.ArgumentParser()

parser.add_argument("--popular",action='store_true')
parser.add_argument("--now_playing",action='store_true')
parser.add_argument("--top_rated",action='store_true')
parser.add_argument("--upcoming",action='store_true')

args = parser.parse_args()

if args.popular:
 get_popular()

if args.now_playing:
 get_now_playing()

if args.top_rated:
 get_top_rated()

if args.upcoming:
 get_upcoming()

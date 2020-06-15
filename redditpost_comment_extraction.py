import praw
import pandas as pd
import datetime as dt
from praw.models import MoreComments
import pprint
#import regex


print('Enter your password')
pwd = input()
reddit = praw.Reddit(client_id = 'nx51nnxrrSpAAQ',
                      client_secret ='xTAWCFCjolv2owQilIKnsd_ZU-A',
                      user_agent = 'RedditPraw1',
                      username = 'tdurdenftw',
                      password = pwd
                      )
ucl_mt ='https://www.reddit.com/r/LiverpoolFC/comments/blumuu/match_thread_liverpool_vs_barcelona_uefa/'
sub = reddit.submission(url=ucl_mt)
pprint.pprint(vars(sub))

#sub.comments.replace_more(limit=0)
#for top_level_comment in sub.comments.list():
#    print(top_level_comment.body)
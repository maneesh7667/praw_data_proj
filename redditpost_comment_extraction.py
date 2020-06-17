import praw
import pandas as pd
import datetime as dt
from praw.models import MoreComments
import pprint
#import regex


print('Enter your password')
pwd = input()

reddit = praw.Reddit(client_id = '<client_id>',
                      client_secret ='<client_secret>',
                      user_agent = '<user_agent>',
                      username = '<username>',
                      password = pwd
                      )
ucl_mt ='<url>'
sub = reddit.submission(url=ucl_mt)
#pprint.pprint(vars(sub))

comment_dict = {"post_id": [],
                "username": [],
                "comment_id": [],
                "comment_text": [],
                "created_at_utc": [],
                "score": []
                }

#test_dict = {"body": []}

sub.comments.replace_more(limit=None)


for top_level_comment in sub.comments.list():
    comment_dict["post_id"].append(top_level_comment.link_id)
    comment_dict["username"].append(top_level_comment.author)
    comment_dict["comment_id"].append(top_level_comment.id)
    comment_dict["comment_text"].append(top_level_comment.body)
    comment_dict["created_at_utc"].append(top_level_comment.created_utc)
    comment_dict["score"].append(top_level_comment.score)
comment_df = pd.DataFrame(comment_dict)


def get_date(created):
    return dt.datetime.fromtimestamp(created)


created_date = comment_df["created_at_utc"].apply(get_date)
comment_df = comment_df.assign(timestamp=created_date)

comment_df.to_csv('file.csv', index=False)

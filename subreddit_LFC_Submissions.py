import pandas as pd
import praw
import datetime as dt

print('Enter your Reddit password')
pwd = input()
try:
    reddit = praw.Reddit(client_id = '<client_id>',
                     client_secret='<client_secret>',
                     user_agent='<user_agent>',
                     username = '<username>',
                     password = pwd
                     )




    #print(dir(reddit))

    subreddit = reddit.subreddit('LiverpoolFC')
    top_subreddit = subreddit.top(limit=200)

    #for submission in subreddit.top(limit=1):
     #   print(submission.title, submission.id)

    topics_dict = { "title": [],
                    "score": [],
                    "id":    [],
                    "url":  [],
                    "comments_num": [],
                    "created": [],
                    "body": []
                    }
    for submission in top_subreddit:
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comments_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)

    topic_df = pd.DataFrame(topics_dict)
    def get_date(created):
        return dt.datetime.fromtimestamp(created)

    created_date = topic_df["created"].apply(get_date)
    topic_df = topic_df.assign(timestamp = created_date)
    print(topic_df)


except:
    print('Incorrect Reddit Connection')
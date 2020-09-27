import sentiment as s

import tweepy
import time

CONSUMER_KEY = '********************'
CONSUMER_SECRET = '********************************************************'
ACCESS_KEY = '****************************************************'
ACCESS_SECRET = '*******************************************'

try:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    print("Success")
except:
    print("Error: Authentication Failed")


FILE = 'last_seen_id.txt'


def retrieve_last_seen_id(file_name = FILE):
    f_read = open(file_name, 'r')
    last_seen = int(f_read.read().strip())
    f_read.close()
    return last_seen


def store_last_seen_id(last_seen_id, file_name = FILE):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

# store_last_seen_id(api.mentions_timeline()[-1].id)
def drive():
    mentions = api.mentions_timeline(retrieve_last_seen_id(FILE))

    for mention in reversed(mentions):
        if mention.in_reply_to_status_id is not None:
            print('@mention used replying to a tweet')
            print(mention.id)
            print(mention.text)

            test = api.get_status(mention.in_reply_to_status_id)

            print(test.text)
            senti = s.sentiment(test.text)
            review = 'positive' if senti[0] == 'pos' else 'negative'
            api.update_status('@'+mention.author.screen_name+' analysis:'+review+"\nand variability: "+str(senti[1]),
                              in_reply_to_status_id=mention.id)

        else:
            print('@Mention used without replying to any tweet.')
            print(mention.id)
            print(mention.text)
            api.update_status('@'+mention.author.screen_name+" please tweet in reply to some another tweet.",
                              in_reply_to_status_id=mention.id)

        time.sleep(5)
        store_last_seen_id(mention.id, FILE)

# print(api.get_status(retrieve_last_seen_id(FILE)).text)
# print("Hello World")

while(True):
    drive()
    time.sleep(60)
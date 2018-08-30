import tweepy
import get_auth
import text
import time

# TLをどこまで読んだか
last = int(time.time()*1000)

# ツイートIDからツイートしたunixtimeに変換
def id2date(id):
    return (id >> 22) + 1288834974657

def tweet(api, status, last):
    tweet_Text = status.text

    if (not status.retweeted) and ("RT @" not in tweet_Text):
        # いいねする
        if ("おさしみ" in tweet_Text or "お刺身" in tweet_Text) and not(str(status.user.screen_name) == "osashimi43"):
            api.create_favorite(status.id)
            print(status.user.name + " @" + str(status.user.screen_name))
            print(tweet_Text)
            print("- - - - - - - - - - - ")

        if (("おさしみ" in tweet_Text or "お刺身" in tweet_Text) and "ガチャ" in status.text) and "【おさしみ10連】" not in status.text:
            tweet = "@" + str(status.user.screen_name) + " "

            if "@" in tweet_Text and " " in tweet_Text[tweet_Text.index("@"):tweet_Text.index("@")+17]:
                for i in range(tweet_Text.index("@"),len(tweet_Text)):
                    tweet += tweet_Text[i]
                    if tweet_Text[i] == " " and not(tweet_Text[i+1] == "@"): break

            if "10連" in tweet_Text:
                sashimi = text.Sashimi(10)
            else:
                sashimi = text.Sashimi(1)

            tweet += sashimi.make_tweet()

            try:
                api.update_status(tweet, status.id)  # ツイート！
                print("-> " + tweet)
                print("-------------------")
            except:
                api.update_status("おさしみガチャ失敗…", status.id) 
                print("エラーが発生しました…")
    return True

def tl_check(list_id: int):
    global last
    auth = get_auth.auth()
    api = tweepy.API(auth)
    ts = api.list_timeline(count=100, list_id=list_id)
    for status in ts:
        try:
            tweet(api, status, last)
        except tweepy.TweepError as e:
            print(e.reason)
    if len(ts) != 0:
        last = id2date(ts[0].id)




import tweepy
import get_auth
import main
from sync import sync, find_list
from apscheduler.schedulers.blocking import BlockingScheduler

# スケジューラー
sched = BlockingScheduler()

auth = get_auth.auth()
api = tweepy.API(auth)
list_id = find_list(api)

# 2秒に1回TL取得
@sched.scheduled_job("interval", seconds=2)
def tl_tweet():
    main.tl_check(list_id)

# 30分に1回リスト同期
@sched.scheduled_job("cron", minute="0,30")
def timed_sync():
    print("同期")
    sync(api, list_id)

if __name__ == "__main__":
    print("osashimi bot start!")
    # スケジューラ開始
    sched.start()
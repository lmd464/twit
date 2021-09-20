import tweepy
import datetime
import sys

# 인증

# 인증을 위한 메소드를 포함하는 OAuthHandler 인스턴스
consumer_key = ""
consumer_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)


# 인증 url을 통해 PIN 획득
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print("Failed to get request token")
    sys.exit()
print(redirect_url)


# PIN 입력 : access token 획득 후 설정
try:
    verifier = input("Verifier : ")
    access_token = auth.get_access_token(verifier)
except tweepy.TweepError:
    print("Failed to get access token")
    sys.exit()
auth.set_access_token(access_token[0], access_token[1])


# 인증 완료 - API() 사용 가능

api = tweepy.API(auth)

# 트윗
tweet = str(datetime.datetime.now()) + " test"
api.update_status(tweet)

print("Succeessfully Posted!")
print()

# 타임라인 읽어옴
timeline = api.home_timeline()
for tweet in timeline:
    print(tweet.text)

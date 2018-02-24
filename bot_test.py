import tweepy
import datetime
import sys

# 인증
# consumer key, secret 설정하여 OAuthHandler 인스턴스 생성
# OAuthHandler 인스턴스를 이용하여, 액세스 토큰 획득

consumer_key = "TtOggJ9XSfza8fT2M3feTJxNC"
consumer_secret = "iRQakh5SEkbGhQ8OxmnRa29ikC4tzltoYdbLmApjXKrXT8fyzp"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

"""
# 1. 직접 얻은 access token 사용 (api.twitter.com에서 액세스 토큰 제공)

access_token = "3025488679-AUwzqnEem9a7VRXcvobrfxzOW8ANjIMlZTRWpEN"
access_token_secret = "ikIiWd99IqLBjd4D9xUbgLWzEyMgWz71PZN3mUjWDghad"
auth.set_access_token(access_token, access_token_secret)

"""

# 2. redirection을 통한 인증으로 access token 획득

# (1) 인증 url 설정 : 인증 완료 시 PIN 획득
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print("Failed to get request token")
print(redirect_url)


# (2) PIN 입력하여 access token 획득 (tuple)
try:
    verifier = input("Verifier : ")
    access_token = auth.get_access_token(verifier)
except tweepy.TweepError:
    print("Failed to get access token")
    sys.exit()


# (3) access token 설정
auth.set_access_token(access_token[0], access_token[1])



# 인증 성공 후 API() 사용 가능

# 기능 인스턴스 API()
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

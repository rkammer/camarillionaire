import os
import tweepy

def get_api() :
    auth = tweepy.OAuthHandler (
        os.getenv('TWITTER_CUSTOMER_KEY'),
        os.getenv('TWITTER_CUSTOMER_SECRET')
    )
    auth.set_access_token (
        os.getenv('TWITTER_ACCESS_KEY'),
        os.getenv('TWITTER_ACCESS_SECRET')
    )

    return tweepy.API(auth)

def update_status(message : str) :
    api = get_api()
    api.update_status(
        status = message,
        lat    = os.getenv('WEATHER_CAM_LAT'),
        long   = os.getenv('WEATHER_CAM_LON'),
        source = "CamarilloBot"
    )
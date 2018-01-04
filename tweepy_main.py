from __future__ import absolute_import, print_function
import zmq, json, time, tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Binds the ZMQ socket to the local port :4321
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:4321")

# Consumer key and secret ID to link Tweepy and the Twitter Application
consumer_key = "QpkTPmn14usqZPZk7cIsVzKQd"
consumer_secret = "kWj8r8gzit64CuohZ05fowuMs4dYhZFvT1tNUYmz7o1grfYMql"

# Access token and token secret ID to connect from Tweepy to the Twitter Application
access_token = "488884935-2Q1enFFqXbja4df9qdeclqiPVIFR3y6hoQ6sGaEO"
access_token_secret = "AlTMqycAf8I6L84AQwgmpQqFIFaRNuemcFUuHcHznwhmS"

# Authorizes this file to interact with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# class inherited from the Steam Listener superclass that faciliates continous Twitter streaming
class StdOutListener(StreamListener):
    def on_data(self, data):
        time.sleep(1) # Tweet metadata are streamed on the terminal with one second intervals
        socket.send_string("stream %s" % data) # sends type string to the ZMQ subscriber
        print(data) # Prints the tweet metadata
        return True # This function is continued forever, as there is no condition to make this boolean false
    
    def on_error(self, status):
        print(status) # Prints a status if there is an error

if __name__ == '__main__': # Python "main" method
    listener = StdOutListener() # calls the StdOutListener class and assigns the class to variable listener
	auth = OAuthHandler(consumer_key, consumer_secret) # Calls the OAuthHandler class to initiate Twitter streaming
    auth.set_access_token(access_token, access_token_secret) # authenticates the OAuthHandler access by furishing API access tokens
	
    stream = Stream(auth, listener) # Calls the Stream class and inputs the authentication and StdOutListener as the class parameters
	stream.filter(track = ['giants'])  # john_sokol1 Twitter ID: 488884935; # Filters for tweets regarding 'giants'

import zmq, json

# Connects to the ZMQ publisher
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt_string(zmq.SUBSCRIBE, "stream")
socket.connect("tcp://127.0.0.1:4321")

while True:
    tweet_stream  = " ".join(socket.recv_string().split()[1:]) # splits the entire string excluding the first value into a list,
                                                               # then rejoins into single string
    tweet       = json.loads(tweet_stream)                     # Reads tweet_stream string and creates the tweet object
    
    if "user" in tweet and "text" in tweet:
        output_tweet = tweet["user"]
        output_tweet["the_tweet"] = tweet["text"]
        
        print(json.dumps(output_tweet)) # Inputs the output_tweet object and .dumps converts the object back into a string
          

#  python tweepy_subscriber.py | ~/Desktop/logstash/bin/logstash -f ~/Desktop/logstash/bin/logstash-simple.conf

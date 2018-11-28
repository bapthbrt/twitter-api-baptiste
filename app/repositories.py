class TweetRepository:
    def __init__(self):
        self.sequence = 0
        self.tweets = []

    def add(self, tweet):
        self.sequence += 1
        tweet.id = self.sequence
        self.tweets.append(tweet)
        return self.sequence

    def get(self, id):
        for tweet in self.tweets:
            if tweet.id == id:
                return tweet
        return None

    def clear(self):
        self.tweets = []
        self.sequence = 0

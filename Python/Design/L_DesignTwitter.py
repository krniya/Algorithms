
import heapq

class Twitter(object):

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.followee = {}
        
    def postTweet(self, user, tweet):
        self.time += 1
        self.tweets[user] = self.tweets.get(user, []) + [(-self.time,  tweet)]
        
    def getNewsFeed(self, user):
        h, tweets = [], self.tweets
        people = self.followee.get(user, set()) | set([user])
        for person in people:
            if person in tweets and tweets[person]:
                time, tweet = tweets[person][-1]
                h.append((time, tweet, person, len(tweets[person]) - 1))
        heapq.heapify(h)
        news = []
        for _ in range(10):
            if h:
                time, tweet, person, idx = heapq.heappop(h)
                news.append(tweet)
                if idx:
                    new_time, new_tweet = tweets[person][idx-1]
                    heapq.heappush(h, (new_time, new_tweet, person, idx - 1))
        return news
        
    def follow(self, follower, other):
        self.followee[follower] = self.followee.get(follower, set()) | set([other])
        
    def unfollow(self, follower, other):
        if follower in self.followee:
            self.followee[follower].discard(other)

obj = Twitter()
obj.postTweet(1,5)
param_2 = obj.getNewsFeed(1)
obj.follow(1,2)
obj.postTweet(2,6)
param_3 = obj.getNewsFeed(1)
obj.unfollow(1,2)
param_4 = obj.getNewsFeed(1)
print(param_2, param_3, param_4)
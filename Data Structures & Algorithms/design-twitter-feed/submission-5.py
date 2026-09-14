from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.tweet = defaultdict(list)
        self.followees = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users_id = self.followees[userId] | {userId}
        tweets = []
        for user_id in users_id:
            tweets += self.tweet[user_id]
        return [tweetId for time, tweetId in heapq.nlargest(10, tweets)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)        

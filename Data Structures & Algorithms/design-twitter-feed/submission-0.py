class Twitter:

    def __init__(self):
        self.relationship_map = defaultdict(set) # Store {user_id: follow_id}
        self.tweets = defaultdict(list) # Store {user_id: [(timestamp, tweet_id)]}
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Get own tweets and tweets of followed users
        all_relevant_tweets = []
        ids_to_fetch = self.relationship_map[userId] | {userId}
        for u_id in ids_to_fetch:
            all_relevant_tweets.extend(self.tweets[u_id])
        
        # Sort by timestamp descending and take top 10
        top_tweets = sorted(all_relevant_tweets, key=lambda x: x[0], reverse=True)[:10]
        return [t[1] for t in top_tweets]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.relationship_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.relationship_map[followerId]:
            self.relationship_map[followerId].remove(followeeId)
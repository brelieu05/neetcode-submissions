class Twitter:

    def __init__(self):
        # user bank {user: set(following)}
        # post bank {user: heap_max(posts, id) <- by most recent}
        # static time

        self.userBank = defaultdict(set)
        self.postBank = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # create key to user bank and post bank if doesn't exist
        # add to post bank (id, time)
        self.time += 1

        self.postBank[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        # User should see their own tweets
        self.userBank[userId].add(userId)

        # Go through everyone the user follows
        for followeeId in self.userBank[userId]:

            if followeeId in self.postBank:
                index = len(self.postBank[followeeId]) - 1

                if index >= 0:
                    time, tweetId = self.postBank[followeeId][index]

                    heap.append([
                        time,
                        tweetId,
                        followeeId,
                        index - 1
                    ])

        heapq.heapify_max(heap)

        while heap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop_max(heap)

            res.append(tweetId)

            # Get this user's next-most-recent tweet
            if index >= 0:
                time, tweetId = self.postBank[followeeId][index]

                heapq.heappush_max(heap, [
                    time,
                    tweetId,
                    followeeId,
                    index - 1
                ])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userBank[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followeeId in self.userBank[followerId]:
            self.userBank[followerId].remove(followeeId)
        

    # 1: [10], 2: [20]

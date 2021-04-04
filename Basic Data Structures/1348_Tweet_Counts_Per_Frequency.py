from collections import defaultdict
class TweetCounts:

    def __init__(self):
        self.a = collections.defaultdict(list)
        self.dic = { 'minute': 60, 'hour':60*60, 'day':60*60*24}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.a[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        cur = 0
        N = ((end -start)//self.dic[freq])+1
        lst = [0] * N
        for i in self.a[tweetName]:
            if i < start or i > end: continue
            lst[(i - start) // self.dic[freq]] += 1
        return lst


class TweetCounts_bin_search:

    def __init__(self):
        self.tweets = collections.defaultdict(list)
        self.delta = {"minute" : 60, "hour" : 3600, "day" : 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort_left(self.tweets[tweetName], time)
        
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        tweets = self.tweets[tweetName]
        result = []
        d = self.delta[freq] - 1
        beginTime = startTime
        searchFromIdx = 0
        while beginTime <= endTime:
            finishTime = min(beginTime + d, endTime)
            startIdx = bisect.bisect_left(self.tweets[tweetName], beginTime, searchFromIdx)
            endIdx = bisect.bisect_right(self.tweets[tweetName], finishTime, startIdx)
            result.append(endIdx - startIdx)
            beginTime = finishTime + 1
            searchFromIdx = endIdx
        return result
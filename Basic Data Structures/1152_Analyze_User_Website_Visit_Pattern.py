from collections import defaultdict
import heapq
from itertools import combinations
def mostVisitedPattern(username, timestamp, website):  # O(nlogn) b/c of sorting and O(n)
    webInfo = []
    for time, usr, web in zip(timestamp, username, website):
        webInfo.append((time, usr, web))
    webInfo.sort(key = lambda x : x[0])
    # FIND THE WEBSITES VISITED BY PARTICULAR USERS
    websiteVisit = defaultdict(list)
    for _, usr, web in webInfo:
        websiteVisit[usr].append(web)
    # FIND THE ROUTES IN THE FORM OF TUPLES OF LENGTH 3
    possibleTuples = defaultdict(int)
    for usr in websiteVisit:
        webRoutes = set(combinations(websiteVisit[usr], 3))
        for webRoute in webRoutes:
            possibleTuples[webRoute] += 1
    # FIND MAX VALUE OF USERS VISITED
    maxVal, routes = max(possibleTuples.values()), []
    for r, val in possibleTuples.items():
        if val == maxVal:
            routes.append(r)
    if len(routes) > 1:
        # SORTS LEXICOGRAPHICALLY
        routes.sort()
    return routes[0]


def mostVisitedPattern_brute_force(username, timestamp, website):
    """
    Get (time, website) records per user
    Find & count all 3-sequences for each user
    Find the one appeared most
    """
    d = collections.defaultdict(list)    # store website records for each user
    c = collections.Counter()            # count how many websites a user visited
    for u, t, w in zip(username, timestamp, website): 
        d[u].append((t, w))
        c[u] += 1
    three_seq_cnt = collections.defaultdict(int)  # counter for three-sequences
    for u, records in d.items():            
        records.sort()                            # sort the record by time
        visited = set()                           # if some 3-sequence appears multiple times for one person, it only counts once
        for i in range(c[u]):                     # brutal force generate all 3-sequences
            for j in range(i+1, c[u]):
                for k in range(j+1, c[u]):
                    three_seq = (records[i][1], records[j][1], records[k][1])
                    if three_seq in visited: continue  # avoid count multiple times
                    three_seq_cnt[three_seq] += 1
                    visited.add(three_seq)
    # sort all 3-sequence count and return                         
    ans = sorted(three_seq_cnt.items(), reverse=True, key=lambda x: (-x[1], x[0]))
    return ans[-1][0]


def mostVisitedPattern_heap(username, timestamp, website):
    """
    Make Tuples of all 3 lists and sort them according to timestamp using a heap
    Pop the sorted items from heap and add all websites of a username in a dictionary with user as key and list of websites visited by them as a value
    Make all possible 3 set combinations of websites visited by a user . As user can visited multiple websites at the same time to avoid duplicate
    combinations store all combinations in a set
    Make a counter dictionary to store occurances of website combinations for different different users
    Calculate maximum for every iteration and store the sequence and keep on updating it
    Return stored sequence.(Parse it to list)
    """
    heap = []
    for i in range(len(timestamp)):
        heapq.heappush(heap, (timestamp[i], website[i], username[i]))
    users = defaultdict(list)
    while heap:
        timeStamp, webSite, userName = heapq.heappop(heap)
        users[userName].append(webSite)
    count = defaultdict(int)
    maximum = 0
    result = tuple()
    for key in users:
        combos = combinations(users[key],3)
        for sequence in set(combos):
            count[sequence] += 1
            if count[sequence]>maximum:
                maximum = count[sequence]
                result = sequence              
            elif count[sequence] == maximum:
                if sequence < result:
                    result = sequence
    return list(result)  
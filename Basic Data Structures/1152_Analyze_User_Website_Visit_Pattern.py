from collections import defaultdict
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
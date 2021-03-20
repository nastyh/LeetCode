class UndergroundSystem:  # O(1) for everything. Space is O(P + S^2) where P the number of pax travelling at the same time, S is the number of stations 
    """
    store the details of a rider in a hashmap with format similar to - {id: [stationName, t]}
    maintain another hashmap that maps every pair of stations for the time of travel and number of times those pairs have been travelled.
    When a checkout happens, we can update that hashmap whose structure is like - {(startStation, endStation): (timeOfTravel, numberOfTimes travelled)}
    to check if that pair had been visited earlier. If not, then update it to have a value like - {(startStation, endStation): ((t in checkOut method) - (t in checkIn method), 1)}.
    Otherwise, update it to increase the frequency and add a value of (t in checkOut method) - (t in checkIn method) to the value[0] in the hashmap.
    """
    def __init__(self):
        self.travelDetails = dict()
        self.avgDetails = dict()
    def checkIn(self, id, stationName, t):
        if id not in self.travelDetails:
            self.travelDetails[id] = [stationName, t]

    def checkOut(self, id, stationName, t):
        p = self.travelDetails.get(id)
        self.travelDetails.pop(id)
        key = (p[0], stationName)
        if key in self.avgDetails:
            self.avgDetails[key] = (self.avgDetails[key][0] + t - p[1], self.avgDetails[key][1] + 1)
        else:
            self.avgDetails[key] = (t - p[1], 1)

    def getAverageTime(self, startStation, endStation):
        key = (startStation, endStation)
        s, n = self.avgDetails[key]
        return s / (n * 1.0)
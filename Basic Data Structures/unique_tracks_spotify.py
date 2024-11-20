from collections import defaultdict
import heapq
"""
There are lists of tracks for each country(not sorted).
Each track has unique id, but they can have duplicates for different countries(with same id).
Track class these fields;
id (unique for track)
country (String)
count(number of times track has been listened in the country),
genre (unique for track, does not change from country to country)
Implement these: getBestNTracksinACountry(String country, int n),
getBestNTracksGlobally(int n) -> for this one, you need to sum up the counts for each track.
I suggested using quick select to get best N tracks, instead of sorting, but they asked me to not waste my time and go with just sorting.
as a follow up, i was asked what happens if we got these requests too often. I basically prepared all possible lists before hand.
I suggest studying HashMaps, and custom sorting for this question
"""
class Track :
    def __init__(self, id, country, genre) :
        self.id = id
        self.country = defaultdict(lambda : 0) # Stores CountryCount
        self.genre = genre
        self.count = 0
    
    def increaseListenCount(self, country) :
        self.count += 1
        self.country[country] += 1
        
    
    def getCount(self) :
        return self.count
    
    def __lt__(self, nxt) :
        return self.count < nxt.count
    
    def getCountryCount(self, country) :
        if country in self.country :
            return self.country[country]
        else :
            raise Exception("Track doesn't exist in the Country")

class Country :
    def __init__(self, countryName, n) :
        self.countryName = countryName
        self.bestNTracks = [] [#Min](https://leetcode.com/problems/minimum-path-sum) Heap to contain top N tracks
        self.n = n
        heapq.heapify(self.bestNTracks)
        
    
    def updateBestNTracks(self, track) :
        if len(self.bestNTracks) == self.n :
            if track.getCountryCount(self.country) > self.bestNTracks[0][0] :
                heapq.heappop(self.bestNTracks)
                heapq.heappush(self.bestNTracks, (track.getCountryCount(self.country), track))
        else :
            heapq.heappush(self.bestNTracks, (track.getCountryCount(self.country), track))
        
        return
    
    def getBestNTracks(self) :
        return self.bestNTracks
    

class MusicService :
    def __init__(self, n) :
        self.globalNTracks = []
        self.tracks = {}
        self.bestNtrackCountryMap = {}
        self.n = n
        heapq.heapify(self.globalNTracks)
        
    
    def recordSongCount(self, song, country, genre) :
        if song not in self.tracks :
            track = Track(song, country, genre)
            self.tracks[song] = track
            if country not in self.bestNtrackCountryMap :
                self.bestNtrackCountryMap[country] = Country(country, self.n)
        track = self.tracks[song]
        track.increaseListenCount(country)
        self.bestNtrackCountryMap[country].updateBestNTracks(track)
        self._updateBestNGlobalTracks(track)
    
    def _updateBestNGlobalTracks(self, track) :
        if len(self.globalNTracks) == self.n :
            if track.getCount() > self.globalNTracks[0].getCount() :
                heapq.heappop(self.globalNTracks)
                heapq.heappush(self.globalNTracks, track)
        else :
            heapq.heappush(self.globalNTracks, track)
        return
    
    def getBestNTracksGlobally(self) :
        return self.globalNTracks
    
    def getBestNTracksInACountry(self, country) :
        if country not in self.bestNtrackCountryMap :
            raise Exception("Country doesn't exist")
        else :
            return self.bestNtrackCountryMap[country].getBestNTracks()
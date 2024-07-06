"""
the historical data
User 1 has liked A, B, C, D
User 2 has liked A, C, D
User 3 has liked B, C, E

Now we have a user that liked C, D
As user1 and user 2 both like C and D, so their liked song will be recommend.
The system should recommend the user song A, B
( A should appear first, as user1 and user2 both liked A)
"""
def find_recommendations(other_users, songs, likes_of_a_user):
    # O(n) both
    # frozenset creates an immutable set. Cannot edit it later
    songs_as_sets = [frozenset(song) for song in songs]
    likes_as_set = frozenset(likes_of_a_user)
    recommeded_set = frozenset()
    for user_songs in songs_as_sets:
        if likes_as_set & user_songs == likes_as_set:
            recommeded_set = (user_songs - likes_as_set) | recommeded_set
    return list(recommeded_set)

def find_recommendations_another(self, inputs: List[List[str]], preferences: List[str]) -> List[str]:
    """
    assume that inputs is 
    [[A, B, C, D], [A, C, D], [B, C, E]]
    """
    dict_songs = {}
    dict_pri = {} 
    res = []
    
    for i in range(len(inputs)):
        songs = inputs[i]
        for song in songs:
            """
            build a dict that is name_of_the_song: [number of times it was liked]
            number of times it was liked is the index + 1
            """
            if song in dict_songs:
                dict_songs[song].append(i + 1)
            else:
                dict_songs[song] = [i + 1]
    for pref in preferences:
        similar_users = dict_songs.get(pref, [])
        for user in similar_users:
            for song in inputs[user - 1]:
                if song != pref:
                    dict_pri[song] = 1 + dict_pri.get(song, 0)
    
    sorted_dict_pri = sorted(dict_pri.items(), key=lambda x: -x[1]) # from least liked to most
    
    max_count = sorted_dict_pri[0][1] if sorted_dict_pri else 0 # the max count of likes 
    for song, count in sorted_dict_pri:
        if count == max_count:  # Only consider songs with maximum count
            res.append(song)
    return res
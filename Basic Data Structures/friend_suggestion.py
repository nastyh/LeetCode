"""
Suppose you have a small, in-memory, social network and each person registered in it is modelled as follow:

Person: {int id, Set<Integer> friends}

Now code a method public Person friendSuggestion(Person p) which will return the person that has most in friends in common with the input 'p'.
In case multiple people have the same number of friends in common, return any one of them. And in case there is no person to return, then NULL should be the answer.

Suppose the following scenario:

Person A: [B, C]
Person B: [A, D, E]
Person C: [A, D, F]
Person D: [B, C, E]
Person E: [B, D, F]
Person F: [C, E]

When we call friendSuggestion(A) it will return Person D.
"""

def friends_brute_force(friends, idx):
    set1 = friends[idx]
    tot =  0
    res = None
    for each in friends:
        if each in set1 or each == idx: continue
        cnt = 0
        for p in friends[each]:
            if p in set1: cnt += 1
        if cnt > tot:
            tot = cnt
            res = each
    return res if res != None else -1
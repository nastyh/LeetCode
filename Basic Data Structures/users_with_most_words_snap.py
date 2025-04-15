"""
https://leetcode.com/discuss/post/4422658/snap-santa-monica-ca-phone-screen-by-ano-v1t4/
you are parsing posts and messages sent each day on a popular online community. Each day you get a report like this:

2021-01-01 12:00:23 [user2] a very long message a very long message a very long message a very long message a very long message a very long message a very long message a very long message a very long message a very long message a very long message a very long message a very long message a very long message a very long message a very long message 
2021-01-01 12:00:23 [user3] blah blah blah blah blah blah blah blah blah blah 
2021-01-01 12:00:23 [user4] blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah 
2021-01-01 12:00:23 [user1] blah blah blah blah 
2021-01-01 12:00:23 [user2] blah blah 
2021-01-01 12:00:23 [user5] blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah 
2021-01-01 12:00:23 [user6] blah blah blah blah blah blah blah blah blah blah 
2021-01-01 12:00:23 [user2] blah blah blah blah blah blah blah blah 
2021-01-01 12:00:23 [user7] blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah 
2021-01-01 12:00:23 [user8] blah blah blah blah blah blah blah blah blah blah blah blah blah 

Write a function that, given a number K, returns the K users who said the most words in the community.
"""

from collections import defaultdict
import heapq
import random
import re
from typing import Counter


def users_with_most_words(report, k):
    """
    build a dict
    {user: [word1: its count], [word2: its count]...}
    do some extraction of the data to create this dict
    then we will just throw into a heap the tuples (-total word count for this user, user)
    we can either build a heap fully or maintain only the top-k users by word count
    """
    d = defaultdict(Counter)
    h = []
    for line in report.splitlines():
        match = re.search(r'\[([^\]]+)\]', line)
        if match:
            user = match.group(1)
            # Get the message portion (trim any leading/trailing spaces)
            message = line[match.end():].strip()
            # Update the counter for this user with words in the message
            d[user].update(message.split())

    for user, counts in d.items():
        all_words_counts = sum(counts.values())
        if len(h) < k:
            heapq.heappush(h, (all_words_counts, user))
        else: 
            # If current user has more words than the smallest in the heap, replace it.
            if all_words_counts > h[0][0]:
                heapq.heapreplace(h, (all_words_counts, user))
    top_users = sorted(h, key=lambda x: x[0], reverse=True)
    return top_users 


# QUICK SELECT SOLUTION
def users_with_most_words_quick_select(report, k):
    # Build the nested dictionary: user -> Counter(word -> count)
    user_word_counts = defaultdict(Counter)
    for line in report.splitlines():
        # Extract the username from the line
        match = re.search(r'\[([^\]]+)\]', line)
        if match:
            user = match.group(1)
            # The rest of the line is the message
            message = line[match.end():].strip()
            # Update the user's word count
            user_word_counts[user].update(message.split())
            
    # Create a list with tuples: (user, total_word_count)
    users = [(user, sum(counter.values())) for user, counter in user_word_counts.items()]
    
    # Quickselect helper functions
    def partition(left, right, pivot_index):
        pivot_value = users[pivot_index][1]
        # Move pivot to end
        users[pivot_index], users[right] = users[right], users[pivot_index]
        store_index = left
        # We want to keep users with greater total word count on the left side
        for i in range(left, right):
            if users[i][1] > pivot_value:
                users[store_index], users[i] = users[i], users[store_index]
                store_index += 1
        # Move pivot to its final place
        users[right], users[store_index] = users[store_index], users[right]
        return store_index

    def quickselect(left, right, k_index):
        """
        Places the kth largest element in its correct position (index k_index)
        such that all elements before it have a larger word count.
        """
        if left == right:
            return
        
        # Choose a random pivot index between left and right
        pivot_index = random.randint(left, right)
        # Partition the list around the pivot
        pivot_index = partition(left, right, pivot_index)
        
        # If pivot_index is the k_index we are targeting, we're done.
        if k_index == pivot_index:
            return
        elif k_index < pivot_index:
            quickselect(left, pivot_index - 1, k_index)
        else:
            quickselect(pivot_index + 1, right, k_index)

    n = len(users)
    if k >= n:
        # If k is greater than or equal to the number of users, simply sort all.
        users.sort(key=lambda x: x[1], reverse=True)
        return users, user_word_counts

    # We want the top k users. The kth largest item should be at index k-1.
    quickselect(0, n - 1, k - 1)
    
    # Now, the first k entries in the list are the top k users,
    # though not necessarily sorted in descending order.
    top_k = users[:k]
    top_k.sort(key=lambda x: x[1], reverse=True)
    
    return top_k
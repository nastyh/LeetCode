from collections import defaultdict, Counter, deque
def alienOrder(words):  # O(C) where C the total length of all the words together,
     space O(1) or O(U + min(U^2, N)), U total # of letters in the alphabet, N -- edges
     # Step 0: create data structures + the in_degree of each unique letter to 0.
    adj_list = defaultdict(set)
    in_degree = Counter({c : 0 for word in words for c in word}) # each letter: 0
    # Step 1: We need to populate adj_list and in_degree.
    # For each pair of adjacent words...
    for first_word, second_word in zip(words, words[1:]):
        for c, d in zip(first_word, second_word): # for first letter first word, first letter second word; second letter second word, second letter third word
            if c != d:
                 """
                 processing
                 right letter: (set of letters that can go before it)
                 """
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    in_degree[d] += 1
                break
        else: # Check that second word isn't a prefix of first word.
            if len(second_word) < len(first_word): return ""

    # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
    output = []
    queue = deque([c for c in in_degree if in_degree[c] == 0]) # letters that for sure are the first ones (nothing before them)
    while queue:
        c = queue.popleft()
        output.append(c)
        for d in adj_list[c]:
            in_degree[d] -= 1
            if in_degree[d] == 0:
                queue.append(d)

    # If not all letters are in output, that means there was a cycle and so
    # no valid ordering. Return "" as per the problem description.
    if len(output) < len(in_degree):
        return ""
    # Otherwise, convert the ordering we found into a string and return it.
    return "".join(output)



def alienOrder_alt(words):
    # Step 0: Put all unique letters into the adj list.
    reverse_adj_list = {c : [] for word in words for c in word}

    # Step 1: Find all edges and put them in reverse_adj_list.
    for first_word, second_word in zip(words, words[1:]):
        for c, d in zip(first_word, second_word):
            if c != d:
                reverse_adj_list[d].append(c)
                break
        else: # Check that second word isn't a prefix of first word.
            if len(second_word) < len(first_word):
                return ""

    # Step 2: Depth-first search.
    seen = {} # False = grey, True = black.
    output = []
    def visit(node):  # Return True iff there are no cycles.
        if node in seen:
            return seen[node] # If this node was grey (False), a cycle was detected.
        seen[node] = False # Mark node as grey.
        for next_node in reverse_adj_list[node]:
            result = visit(next_node)
            if not result:
                return False # Cycle was detected lower down.
        seen[node] = True # Mark node as black.
        output.append(node)
        return True

    if not all(visit(node) for node in reverse_adj_list):
        return ""

    return "".join(output)

    """
Getting as much information about the alphabet order as we can out of the input word list.
Representing that information in a meaningful way.
Assembling a valid alphabet ordering.

Where two words are adjacent, we need to look for the first difference between them. That difference tells us the relative order between two letters. Let's have a look at all the relations we can find by comparing adjacent words.

    """


"""
Implement Insertion Sort and return intermediate states.

Insertion Sort is a simple sorting algorithm that builds the sorted list one element at a time, from left to right. It works by repeatedly taking an element from the unsorted portion and inserting it into its correct position in the sorted portion of the list.

Objective:

Given a list of key-value pairs, sort the list by key using Insertion Sort. Return a list of lists showing the state of the array after each insertion. If two key-value pairs have the same key, maintain their relative order in the sorted list.

Input:

pairs - a list of key-value pairs, where each key-value has an integer key and a string value. (0 <= pairs.length <= 100).
Example 1:

Input:
pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]

Output:
[[(5, "apple"), (2, "banana"), (9, "cherry")], 
 [(2, "banana"), (5, "apple"), (9, "cherry")], 
 [(2, "banana"), (5, "apple"), (9, "cherry")]]
Notice that the output shows the state of the array after each insertion. The last state is the final sorted array. There should be pairs.length states in total.

Example 2:

Input:
pairs = [(3, "cat"), (3, "bird"), (2, "dog")]

Output:
[[(3, "cat"), (3, "bird"), (2, "dog")], 
 [(3, "cat"), (3, "bird"), (2, "dog")],
 [(2, "dog"), (3, "cat"), (3, "bird")]]
In this example, you can observe that the pairs with key=3 ("cat" and "bird") maintain their relative order, illustrating the stability of the Insertion Sort algorithm.
"""
def insertion_sort_with_states(pairs):
    """
    Perform insertion sort on a list of key-value pairs and return the intermediate states.

    Args:
    pairs (list): List of tuples (key, value) to be sorted by key.

    Returns:
    list: List of lists showing the state of the array after each insertion.
    """
    states = [pairs[:]]  # Initialize with the initial state of the array

    for i in range(1, len(pairs)):
        key_item = pairs[i]
        j = i - 1

        # Move elements of pairs[0..i-1], that are greater than key_item, to one position ahead of their current position
        while j >= 0 and pairs[j][0] > key_item[0]:
            pairs[j + 1] = pairs[j]
            j -= 1

        # Insert the key_item into its correct position
        pairs[j + 1] = key_item

        # Append the current state of the array to the states list
        states.append(pairs[:])

    return states

# Example usage
example1 = [(5, "apple"), (2, "banana"), (9, "cherry")]
example2 = [(3, "cat"), (3, "bird"), (2, "dog")]

print(insertion_sort_with_states(example1))
print(insertion_sort_with_states(example2))

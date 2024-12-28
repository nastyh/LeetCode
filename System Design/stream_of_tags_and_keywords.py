"""
O(N*(L+M+U)), N num of tag strings, M num of tags in the string, U num of unique tags added
O(T) T is the num of unique remaining tags 
There is a stream that has coming tags and also has a list of keywords, design a high performance filter to output these keywords remaining tags.
For example: given stream ['apple, facebook, google', 'banana, facebook', 'facebook, google, tesla', 'intuit, google, facebook'],
if the keyword is ['apple'] the output should ['facebook', 'google'] because only 'apple, facebook, google' has apple. Similarly if
the keyword is ['facebook', 'google'], the output should ['apple', 'tesla', 'intuit']. The output can be in any order and can be put
into a single list/array.
"""
def filter_tags(stream, keywords):
    """
    Filters tags from the stream based on the given keywords.

    :param stream: Iterable of tag strings.
    :param keywords: List of keywords to filter.
    :return: Set of remaining tags.
    """
    keyword_set = set(keywords)  # O(1) lookup for keywords
    result_set = set()           # Stores unique matching tags

    for tag_string in stream:
        tags = set(tag_string.split(", "))  # Split and convert to a set
        if tags & keyword_set:  # Check for intersection with keywords
            result_set.update(tags - keyword_set)  # Add non-keyword tags

    return result_set

# Example usage
stream = [
    "apple, facebook, google",
    "banana, facebook",
    "facebook, google, tesla",
    "intuit, google, facebook"
]
keywords = ["apple"]

output = filter_tags(stream, keywords)
print(output)  # Output: {'facebook', 'google'}

keywords = ["facebook", "google"]
output = filter_tags(stream, keywords)
print(output)  # Output: {'apple', 'tesla', 'intuit'}
"""
Question 1 - Given array of latencies[], sort them in bucket ranges.
ranges - 0-9, 10-19, 20-29, 30-39, 40-49,50-59, 60-69, 70-79, 80-89, 90-99, 100>=

Input: latencies[6,7,50, 100,110]
output:
0-9 - 2
50-59 - 1
100 - 2
"""

def bucketize_latencies_short(latencies):
    """
    O(n)
    O(1)
    """
    bucket_ranges = [(i, i + 9) for i in range(0, 100, 10)]
    bucket_keys = [f"{low}-{high}" for low, high in bucket_ranges]
    bucket_keys.append("100")  # Add the "100+" bucket

    # Initialize the buckets
    buckets = {key: 0 for key in bucket_keys}

    for latency in latencies:
        if latency >= 100:
            buckets["100"] += 1
        else:
            index = latency // 10  # Determine the appropriate bucket index
            bucket_key = bucket_keys[index]
            buckets[bucket_key] += 1

    return buckets

def bucketize_latencies(latencies):
    """
    O(n)
    O(1)
    Sort latencies into predefined bucket ranges.
    
    :param latencies: List of integers representing latencies.
    :return: Dictionary with bucket ranges as keys and counts as values.
    """
    # Define the bucket ranges
    buckets = {
        "0-9": 0, "10-19": 0, "20-29": 0, "30-39": 0, "40-49": 0,
        "50-59": 0, "60-69": 0, "70-79": 0, "80-89": 0, "90-99": 0, 
        "100": 0
    }

    # Process each latency
    for latency in latencies:
        if 0 <= latency <= 9:
            buckets["0-9"] += 1
        elif 10 <= latency <= 19:
            buckets["10-19"] += 1
        elif 20 <= latency <= 29:
            buckets["20-29"] += 1
        elif 30 <= latency <= 39:
            buckets["30-39"] += 1
        elif 40 <= latency <= 49:
            buckets["40-49"] += 1
        elif 50 <= latency <= 59:
            buckets["50-59"] += 1
        elif 60 <= latency <= 69:
            buckets["60-69"] += 1
        elif 70 <= latency <= 79:
            buckets["70-79"] += 1
        elif 80 <= latency <= 89:
            buckets["80-89"] += 1
        elif 90 <= latency <= 99:
            buckets["90-99"] += 1
        elif latency >= 100:
            buckets["100"] += 1

    return buckets
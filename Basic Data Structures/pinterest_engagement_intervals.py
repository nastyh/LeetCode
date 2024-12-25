def calculate_engagements(pins):
    """
    O(nm), n - len of pins, m - max duration of a pin
    O(nm) potentially for space if everything is one unit in the dict
    for each pin
    iterate through every time point between pin[0] and pin[1]: basically b/w the start and end
    if this interval + 1 not in the dict, add it with a count of 0
    Otherwise increment what we have 
    we can return this dict at the end
    """
    d = {}
    for pin in pins:
        for t in range(pin[0], pin[1]):
            if (t, t + 1) not in d: # define a unit time interval
                d[(t, t + 1)] = 0
            d[(t, t + 1)] += 1 
    return d  

# if we are provided with the pins and the timestamp to get an answer for

def calculate_engagements_another(pins, ts):
    """
    take each pin, let's say, all is in minutes
    every minute between start and end should be accounted for
    we store tuples in the dict
    if we already saw this minute, we'll increment its count
    """
    d = {}
    for pin in pins:
        for t in range(pin[0], pin[1]):
            if (t, t + 1) not in d:
                d[(t, t + 1)] = 0
            d[(t, t + 1)] += 1 
    if (ts, ts + 1) in d:
        return d[(ts, ts + 1)]
    else: return 0 

def count_engagement_at_ts(pins, ts):
    """
    Sorting
    O(nlogn) and O(n)
    """
    events = []
    
    # Create events for the start and end times
    for start, end in pins:
        events.append((start, 1))  # Start increases the engagement
        events.append((end, -1))    # End decreases the engagement
    
    # Sort events by their time, and by type (end before start if same time)
    events.sort(key=lambda x: (x[0], x[1]))
    current_engagements = 0
    
    # Process the events and count engagements at time ts
    for time, event_type in events:
        if time > ts:
            break
        current_engagements += event_type
    
    return current_engagements
"""
You are given a list of [time, power] for player A and player B where the first element is the timestamp and second element is
the power output the player reaches at that timestamp.
You are also given a window for how long the game will last. Calculate the percentage of time for which player A has greater power than player B.

Example:
total game window: 300.0 seconds

player A [ [50, 60], [100.33, 40], [200, 80] ]
player B [ [1, 75] , [50.5, 70] ]

percentage of time A > B ~= 33 %
Explanation: From 200 -> 300 is when player A has higher power output that player B. 100/300 ~= 33%
"""

def get_power_at(t, events):
    """
    Helper func
    Given a sorted list of events [time, power] and a time t,
    return the current power at time t. 
    If no event has occurred by t, return 0.
    """
    power = 0
    for time, p in events:
        if time <= t:
            power = p
        else:
            break
    return power

def compute_percentage(total_time, events_A, events_B):
    """
    For each player, before the first event the power is assumed to be 0.
    Once an event occurs, the power is “held” constant until the next event or until the game ends.
    We take the union of 0, the game end time, and all event times from both players.
    This gives us a sorted list of times at which either player’s power might change.
    For each interval,  we determine the power of player A and player B (using the latest event that occurred before or at t_i
    If player A’s power is greater, we add the interval’s duration to the total winning time for A.
    percentage is computed as the total duration where A leads divided by the total game time.
    total_time: total game window in seconds.
    events_A: list of [time, power] for player A.
    events_B: list of [time, power] for player B.
    
    Returns the percentage of time for which A's power > B's power.
    """
    # Include boundaries and all event times from both players.
    times = {0, total_time}
    for time, _ in events_A:
        if 0 <= time <= total_time:
            times.add(time)
    for time, _ in events_B:
        if 0 <= time <= total_time:
            times.add(time)
    
    # Create sorted list of all time boundaries.
    sorted_times = sorted(times)
    
    total_A_win = 0.0
    # Evaluate each interval.
    for i in range(len(sorted_times) - 1):
        t_start = sorted_times[i]
        t_end = sorted_times[i+1]
        # For a representative time in the interval, we pick the start.
        power_A = get_power_at(t_start, events_A)
        power_B = get_power_at(t_start, events_B)
        if power_A > power_B:
            total_A_win += (t_end - t_start)
    
    percentage = (total_A_win / total_time) * 100
    return percentage
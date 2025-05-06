from bisect import bisect_left, bisect_right

class LogSystem:
    """
    put is O(n) worst 
    retrieve is O(logn + k), k matches, n is the array's length
    Storage is O(n)
    """
    #   substring‑end index (exclusive) for every granularity
    _IDX = {"Year": 4, "Month": 7, "Day": 10,
            "Hour": 13, "Minute": 16, "Second": 19}

    #   what to append after the cut‑off to get the *smallest*/ *largest*
    #   timestamp that still belongs to the same bucket
    _MIN_SUFFIX = {
        "Year"  : ":01:01:00:00:00",
        "Month" : ":01:00:00:00",
        "Day"   : ":00:00:00",
        "Hour"  : ":00:00",
        "Minute": ":00",
        "Second": ""
    }
    _MAX_SUFFIX = {
        "Year"  : ":12:31:23:59:59",
        "Month" : ":31:23:59:59",
        "Day"   : ":23:59:59",
        "Hour"  : ":59:59",
        "Minute": ":59",
        "Second": ""
    }

    def __init__(self):
        self._time, self._ids = [], []        # always kept in sorted order

    # O(n) insertion is fine because n ≤ 500
    def put(self, log_id: int, timestamp: str) -> None:
        i = bisect_right(self._time, timestamp)
        self._time.insert(i, timestamp)
        self._ids .insert(i, log_id)

    def retrieve(self, start: str, end: str, granularity: str):
        """
        1. Truncate start/end at the required granularity.
        2. Expand them to the *smallest* / *largest* timestamps that still
           belong to the requested bucket.
        3. Binary‑search in the chronologically‑sorted array.
        """
        cut = self._IDX[granularity]

        lo = start[:cut] + self._MIN_SUFFIX[granularity]
        hi = end  [:cut] + self._MAX_SUFFIX[granularity]

        left  = bisect_left (self._time, lo)
        right = bisect_right(self._time, hi)

        return self._ids[left:right]

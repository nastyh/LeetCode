class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        O(mlogm + mlogn), n is the num of meetings, n is the num of rooms
        O(n+m) for the heaps and room tracking
        Any ongoing meeting that ends before or at the current meeting's start
        time is removed from the ongoing_meetings heap, and the room is added back to available_rooms.
        If a room is available, allocate it. Otherwise, delay the meeting until the earliest room becomes available.
        Increment the count for the room where a meeting is held.
        Identify the room with the maximum meeting count, breaking ties by returning the smallest room number.
        """
        meetings.sort(key=lambda x: x[0]) # by the start time, prob optional 
        available_rooms = list(range(n))  # Initially, all rooms are available
        ongoing_meetings = []  # Min-heap of (end_time, room)
        room_meeting_count = [0] * n
        for start, end in meetings:
        # Step 2: Free up rooms where meetings have ended
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                end_time, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(available_rooms, room)
            
            # Step 3: Assign a room
            if available_rooms:
                # Use the lowest-numbered available room
                room = heapq.heappop(available_rooms)
                heapq.heappush(ongoing_meetings, (end, room))
            else:
                # Delay the meeting until the earliest room becomes free
                end_time, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(ongoing_meetings, (end_time + (end - start), room))
            
            # Increment the meeting count for the assigned room
            room_meeting_count[room] += 1
    
        # Step 4: Find the room with the most meetings
        max_meetings = max(room_meeting_count)
        for i in range(n):
            if room_meeting_count[i] == max_meetings:
                return i

        
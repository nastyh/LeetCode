"""
You're a restaurant manager who's job is to find available time windows for seating N number of guest(s).
Lets assume your restaruant is specified in the following way:

restaurant = {
'restaurant_start': 9,
'restaurant_end': 22,
'capacity': 5,
'reservations': [
{'start': 10, 'end': 14, 'ppl': 3},
{'start': 11, 'end': 13, 'ppl': 2},
{'start': 13.5, 'end': 15, 'ppl': 1},
{'start': 16, 'end': 20, 'ppl': 2}
]
}

Where restaurant_start and restaurant_end are the open and close times of the resturant,
capacity is the maximum number people the restaurant can fit at any point, and reservations are existing
reservations w/ guests (e.g ppl is the number of customers who are already at the restaurant at that time interval).

Write an algorithm that can output all available time intervals for seating an input N guests
from restaurant open to close (e.g [[9,11],....]]).
Assume your input to the function is in the format of the restaurant dictionary
object specified above along with a parameter N indicating the number of people to seat.
"""

def find_available_times(restaurant, N):
  """
  O(R log R + T * R)
  O(R + T)
  R is the number of reservations.
  T is the duration of the restaurant's operating hours (restaurant_end - restaurant_start).
  Finds available time windows for seating N guests in a restaurant.
  Args:
    restaurant: A dictionary representing the restaurant, containing:
      - 'restaurant_start': Opening time of the restaurant.
      - 'restaurant_end': Closing time of the restaurant.
      - 'capacity': Maximum capacity of the restaurant.
      - 'reservations': List of existing reservations, each with 'start', 'end', and 'ppl'.
    N: Number of guests to seat.
  Returns:
    A list of available time windows, where each window is a list of two floats 
    representing the start and end times.
  """
  # Sort reservations by start time
  reservations = sorted(restaurant['reservations'], key=lambda x: x['start'])
  # Initialize variables
  current_time = restaurant['restaurant_start'] # current time we're examining.
  available_times = []
  current_occupancy = 0 # how many guests are currently in the restaurant at any given time
  # Iterate through time and reservations
  while current_time < restaurant['restaurant_end']:
    # Check for overlapping reservations
    while reservations and current_time >= reservations[0]['start']:
      current_occupancy += reservations[0]['ppl']
      reservations.pop(0) # Remove reservations that have already started from the reservations list.

    # Check if there's enough capacity for N guests
    if current_occupancy + N <= restaurant['capacity']: 
      # Find the end time of the available window
      end_time = current_time
      while reservations and end_time >= reservations[0]['start']: # upcoming reservations and the current_time is still within the available slot
        end_time = min(end_time, reservations[0]['start'])
      available_times.append([current_time, end_time]) # Add the available time slot 

    # Update current_time and occupancy
    current_time = end_time
    if reservations:
      current_time = max(current_time, reservations[0]['start'])
      current_occupancy -= reservations[0]['ppl']
      reservations.pop(0)

  return available_times

# Example usage:
restaurant = {
    'restaurant_start': 9,
    'restaurant_end': 22,
    'capacity': 5,
    'reservations': [
        {'start': 10, 'end': 14, 'ppl': 3},
        {'start': 11, 'end': 13, 'ppl': 2},
        {'start': 13.5, 'end': 15, 'ppl': 1},
        {'start': 16, 'end': 20, 'ppl': 2}
    ]
}

N = 2  # Number of guests to seat
available_times = find_available_times(restaurant, N)

print("Available Time Windows:", available_times)


# HEAP SOLUTION

class ReservationScheduler:

    def __init__(self, restaurant):
        self.timeSlotsHeap = self.getTimeSlotsForHeap(restaurant['reservations'])
        self.cap = restaurant['capacity'] # maximum capacity
        self.opening = restaurant['restaurant_start']
        self.close = restaurant['restaurant_end']
        self.currCap = restaurant['capacity'] # current occupancy of the restaurant 

    def getTimeSlotsForHeap(self, reservations):
        heap = []
        for res in reservations:
            # increment at entry
            heapq.heappush(heap, [res['start'], -res['ppl']]) # arrival of guests
            # decrement at leave
            heapq.heappush(heap, [res['end'], res['ppl']]) # departure of guests. More space is available now 
        return heap

    def allAvailableTimeSlotsSeatingNseating(self, n):
        """
        finds all available time slots for seating n guests.
        """
        if n > self.cap:
            return []
        size = len(self.timeSlotsHeap)
        result = []
        heap = list(self.timeSlotsHeap)

        prev = self.opening
        currCap = self.cap # based on the number of guests arriving or leaving.
        for i in range(size):
            time, seats = heap[i]

            if time > prev and currCap >= n:
                result.append([prev, time])
            currCap += seats
            prev = time
        if heap[size - 1][0] < self.close: # last event ends before the restaurant's closing time.
            result.append([heap[size - 1][0], self.close])
        # merge intervals now
        result2 = []
        start = result[0][0]
        end = result[0][1]
        size = len(result)
        for i in range(size):
            if end >= result[i][0]:
                # merge these
                end = max(end, result[i][1])
            else:
                result2.append([start, end])
                start = result[i][0]
                end = result[i][1]
        result2.append([start, end])
        return result2
    

    

restaurant = {
    'restaurant_start': 9,
    'restaurant_end': 22,
    'capacity': 5,
    'reservations': [
        {'start': 10, 'end': 14, 'ppl': 3},
        {'start': 11, 'end': 13, 'ppl': 2},
        {'start': 13.5, 'end': 15, 'ppl': 1},
        {'start': 16, 'end': 20, 'ppl': 2}
    ]
}

rs = ReservationScheduler(restaurant)

print(rs.allAvailableTimeSlotsSeatingNseating(5))
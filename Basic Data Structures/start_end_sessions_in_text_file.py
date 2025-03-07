"""
Implement the Logger interface
two func
start_session(start_time, session_id)
end_session(end_time, session_id)
store in the logs.txt:
session_id start_time duration
duration is the diff between end and start times
if the session ends, it won't happen again.
Write immediately since it's a stream process 
"""
class Logger:
    def __init__(self, log_file='logs.txt'):
        # File where logs will be stored.
        self.log_file = log_file
        # Dictionary to store active sessions: {session_id: start_time}
        self.active_sessions = {}
    
    def start_session(self, start_time, session_id):
        """
        Starts a session by saving the start_time associated with session_id.
        
        Time Complexity: O(1)
        Space Complexity: O(1) per session.
        """
        self.active_sessions[session_id] = start_time
    
    def end_session(self, end_time, session_id):
        """
        Ends a session by calculating its duration and writing it to the log file immediately.
        
        It retrieves the start_time for the given session_id, computes:
            duration = end_time - start_time,
        and appends the record to the file in the format:
            session_id start_time duration
        
        Time Complexity: O(1) for dictionary lookup and file append.
        Space Complexity: O(1) additional space.
        """
        if session_id not in self.active_sessions:
            raise ValueError(f"Session ID {session_id} not found. Please start the session first.")
        
        start_time = self.active_sessions.pop(session_id)
        duration = end_time - start_time

        # Append the log entry to the file immediately.
        with open(self.log_file, 'a') as f:
            f.write(f"{session_id} {start_time} {duration}\n")


# Example usage:
if __name__ == '__main__':
    logger = Logger()

    # Session 1: start at 3, end at 200 (duration 197).
    logger.start_session(3, 12345)
    logger.end_session(200, 12345)  # writes: "12345 3 197"

    # Session 2: start at 212, end at 1089 (duration 877).
    logger.start_session(212, 77677)
    logger.end_session(1089, 77677)  # writes: "77677 212 877"

    # Session 3: start at 123, end at 1100 (duration 977).
    logger.start_session(123, 88999)
    logger.end_session(1100, 88999)  # writes: "88999 123 977"


# If we want to avoid opening a file in each function's call
# we can do it during the initalization

class Logger:
    def __init__(self, log_file='logs.txt'):
        """
        Initialize the Logger by opening the log file once in write mode.
        This file will be used for logging ended sessions.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.log_file = log_file
        self.active_sessions = {}  # Store active sessions: {session_id: start_time}
        # Open the log file once and keep the file handle.
        # avoids the overhead of opening and closing the file for each session end event
        self.log_handle = open(log_file, 'w')
    
    def start_session(self, start_time, session_id):
        """
        Records the start of a session by storing its start time.
        
        Time Complexity: O(1)
        Space Complexity: O(1) per session.
        """
        self.active_sessions[session_id] = start_time
    
    def end_session(self, end_time, session_id):
        """
        Ends a session, computes its duration, and immediately logs the record.
        
        The log entry format is:
            session_id start_time duration
        
        Time Complexity: O(1) for dictionary lookup and file write.
        Space Complexity: O(1)
        """
        if session_id not in self.active_sessions:
            raise ValueError(f"Session ID {session_id} not found. Make sure to start the session first.")
        
        start_time = self.active_sessions.pop(session_id)
        duration = end_time - start_time
        
        # Write the log entry to the already opened file handle.
        self.log_handle.write(f"{session_id} {start_time} {duration}\n")
        self.log_handle.flush()  # Ensure the data is written immediately.
    
    def close(self):
        """
        Closes the log file. It is a good practice to call this method when logging is done.
        """
        self.log_handle.close()


# Example usage:
if __name__ == '__main__':
    logger = Logger()

    # Example 1: start at 3, end at 200 (duration = 197).
    logger.start_session(3, 12345)
    logger.end_session(200, 12345)  # Logs: "12345 3 197"
    
    # Example 2: start at 212, end at 1089 (duration = 877).
    logger.start_session(212, 77677)
    logger.end_session(1089, 77677)  # Logs: "77677 212 877"
    
    # Example 3: start at 123, end at 1100 (duration = 977).
    logger.start_session(123, 88999)
    logger.end_session(1100, 88999)  # Logs: "88999 123 977"
    
    # After all sessions have ended, close the logger.
    logger.close()


# If we want to write the output sorted by the start time 

class Logger:
    def __init__(self, log_file='logs.txt'):
        """
        Initialize the Logger.
        
        Attributes:
          log_file: The file name where logs are stored.
          active_sessions: A dictionary for sessions in progress, mapping session_id to start_time.
          completed_sessions: A list to hold records of ended sessions as tuples (session_id, start_time, duration).
        """
        self.log_file = log_file
        self.active_sessions = {}       # Active sessions: {session_id: start_time}
        self.completed_sessions = []    # Completed sessions: list of (session_id, start_time, duration)
    
    def start_session(self, start_time, session_id):
        """
        Start a session by recording its start time.
        
        Time Complexity: O(1)
        Space Complexity: O(1) per session.
        """
        self.active_sessions[session_id] = start_time
    
    def end_session(self, end_time, session_id):
        """
        Ends a session, computes its duration, and updates the log file.
        
        After computing:
            duration = end_time - start_time,
        the session record (session_id, start_time, duration) is appended to the completed sessions list.
        The list is then sorted by start_time, and the log file is completely rewritten with the updated,
        sorted list.
        
        Time Complexity: O(n log n) per session end call in the worst-case (for sorting the n completed sessions)
                         plus O(n) for rewriting the file.
        Space Complexity: O(1) additional space per ended session.
        """
        if session_id not in self.active_sessions:
            raise ValueError(f"Session ID {session_id} not found. Please start the session first.")
        
        start_time = self.active_sessions.pop(session_id)
        duration = end_time - start_time
        # Append the completed session record.
        self.completed_sessions.append((session_id, start_time, duration))
        
        # Sort the completed sessions by start time (second element of the tuple).
        self.completed_sessions.sort(key=lambda record: record[1])
        
        # Rewrite the log file with the sorted sessions.
        with open(self.log_file, 'w') as f:
            for sess_id, s_time, dur in self.completed_sessions:
                f.write(f"{sess_id} {s_time} {dur}\n")


# Example usage:
if __name__ == '__main__':
    logger = Logger()

    # Example sessions:
    # Session with ID 12345: start at 3, end at 200 => duration 197.
    logger.start_session(3, 12345)
    logger.end_session(200, 12345)  # Will write: "12345 3 197"
    
    # Session with ID 77677: start at 212, end at 1089 => duration 877.
    logger.start_session(212, 77677)
    logger.end_session(1089, 77677)  # Now, file contains:
                                  # 12345 3 197
                                  # 77677 212 877
    
    # Session with ID 88999: start at 123, end at 1100 => duration 977.
    logger.start_session(123, 88999)
    logger.end_session(1100, 88999)  # After sorting by start time, file becomes:
                                  # 12345 3 197
                                  # 88999 123 977
                                  # 77677 212 877


# Same but with the deque

from collections import deque

class Logger:
    def __init__(self, log_file='logs.txt'):
        """
        Initializes the Logger.
        
        Attributes:
          log_file: The file name where logs are stored.
          active_sessions: A dictionary mapping session_id to start_time.
          finished_sessions: A deque storing finished sessions as tuples 
                             (start_time, session_id, duration), maintained in sorted order by start_time.
        """
        self.log_file = log_file
        self.active_sessions = {}
        self.finished_sessions = deque()  # Will hold records sorted by start time.
    
    def start_session(self, start_time, session_id):
        """
        Records the start of a session by storing its start time.
        
        Time Complexity: O(1)
        Space Complexity: O(1) per session.
        """
        self.active_sessions[session_id] = start_time
    
    def end_session(self, end_time, session_id):
        """
        Ends a session by computing its duration and inserting the record into 
        the finished_sessions deque in sorted order (by start time). Then rewrites the log file.
        
        Log entry format: session_id start_time duration
        
        Time Complexity:
          - O(n) in the worst case for inserting into the deque.
          - O(n) for rewriting the log file.
        Space Complexity: O(1) additional space per ended session.
        """
        if session_id not in self.active_sessions:
            raise ValueError("Session ID not found. Please call start_session first.")
        
        start_time = self.active_sessions.pop(session_id)
        duration = end_time - start_time
        record = (start_time, session_id, duration)
        
        # Insert the record in sorted order (by start_time) using the deque.
        inserted = False
        for i, rec in enumerate(self.finished_sessions):
            if rec[0] > start_time:
                self.finished_sessions.insert(i, record)
                inserted = True
                break
        if not inserted:
            self.finished_sessions.append(record)
        
        # Rewrite the log file with the updated, sorted finished sessions.
        self._update_log_file()
    
    def _update_log_file(self):
        """
        Rewrites the log file with all finished sessions in order by start time.
        """
        with open(self.log_file, 'w') as f:
            for start_time, session_id, duration in self.finished_sessions:
                f.write(f"{session_id} {start_time} {duration}\n")


# Example usage:
if __name__ == '__main__':
    logger = Logger()

    # Session with ID 12345: start at 3, end at 200 (duration = 197).
    logger.start_session(3, 12345)
    logger.end_session(200, 12345)  # Log file: "12345 3 197"
    
    # Session with ID 77677: start at 212, end at 1089 (duration = 877).
    logger.start_session(212, 77677)
    logger.end_session(1089, 77677)  # Log file now:
                                  # "12345 3 197"
                                  # "77677 212 877"
    
    # Session with ID 88999: start at 123, end at 1100 (duration = 977).
    logger.start_session(123, 88999)
    logger.end_session(1100, 88999)  # After insertion, the finished_sessions deque becomes:
                                  # [(3, 12345, 197), (123, 88999, 977), (212, 77677, 877)]
                                  # And the log file "logs.txt" will contain:
                                  # 12345 3 197
                                  # 88999 123 977
                                  # 77677 212 877

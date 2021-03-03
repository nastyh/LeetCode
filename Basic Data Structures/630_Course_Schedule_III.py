import heapq
def scheduleCourse(courses):  # O(nlogn) both
    """
    Very tricky question.
    We sort the courses by their expected deadline.
    Now one by one we start doing the courses.
    If by chance, we are exceeding the deadline. We tend to eliminate the courses,
    which take max time so as to accomodate more number of min time courses. If we have 6 minutes, better to do 4+2(2 courses) instead of 1 course(5)
    """
    
    if courses == None or len(courses) == 0:
        return 0
    
    courses.sort(key = lambda x: x[1])
    curr_time = count = 0
    max_heap = []
    heapq.heapify(max_heap)
    
    for i in range(len(courses)):
        heapqheappush(max_heap, -1 * courses[i][0])
        curr_time += courses[i][0]
        count += 1   
        if  curr_time > courses[i][1] :
            curr_time += heapqheappop(max_heap)
            count -= 1
    return count
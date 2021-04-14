from collections import Counter
def countStudents_optimal(students, sandwiches):  # O(n) and O(1)
    """
    Key here is how to define a loop and what to return at the end
    Because we remove elements from students, it will be one of the stopping conditions. 
    Another stopping condition is mismatch != len(students). It's for a case when we're stuck and can longer find any pairs.
    If sandwiches and students match, it's all good: remove the respective pair and nullify mismatch
    If they don't match, move student to the end and increment mismatch 
    """
    mismatch = 0
    while len(students) > 0 and mismatch != len(students):
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            mismatch = 0
        else:
            student_to_move = students[0]
            students.pop(0)
            students.append(student_to_move)
            mismatch += 1
    return len(students)


def countStudents(students, sandwiches):     
        students = Counter(students)
        total_sandwiches = len(sandwiches)
        i = 0
        # Go through all the sanwiches until no more sanwich available. or no student like the ones we have
        while i < total_sandwiches:
            # get the current type of sandwich
            current = sandwiches[i] 
            # the number of the students who like current type of sanwiches is students[current]
            # so when students[current] == 0, we know no students like the current type of sanwich
            if  current not in students or (students[current] == 0):
                return students[0] + students[1]
            else:
                # we give the sandwich to this students, and move to next sandwich
                students[current] -= 1
                i += 1
        return 0

def countStudents_short(students, sandwiches):
    counts = [len(students) - sum(students), sum(students)]        
    for s in sandwiches:
        if not counts[s]:
            return sum(counts)
        counts[s] -= 1            
    return 0

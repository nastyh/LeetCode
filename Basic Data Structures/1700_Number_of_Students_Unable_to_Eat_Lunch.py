from collections import Counter
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


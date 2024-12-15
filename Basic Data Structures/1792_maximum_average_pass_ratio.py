class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """
        O(nlogn) --> insert n classes into a heap
        O(n) --> to store a heap
        it's a max heap, so we have access to the largest gain we can achieve 
        by adding an extra student to a class. 
        Distribute existing students across the classes one by one. 
        From the heap, we can pop a class with the largest potential gain achievable
        from adding an extra person. 
        Then recalculate, push back
        The compute the final result by popping from the heap
        helper calculates an absolute gain from adding an extra student
        """
        m_heap = []
        def _helper(passes, all_stud):
            """
            gain from adding a student to a class
            """
            return (passes + 1) / (all_stud + 1) - passes/all_stud
        for passes, all_students in classes:
            extra_gain = _helper(passes, all_students)
            heapq.heappush(m_heap, (-extra_gain, passes, all_students))

        for _ in range(extraStudents):
            curr_gain, passes, total_students = heapq.heappop(m_heap)
            heapq.heappush(m_heap, (-_helper(passes+1, total_students+1), passes+1, total_students + 1))

        res = 0
        while m_heap:
            _, passes, total_stud = heapq.heappop(m_heap)
            res += passes / total_stud
        return res / len(classes)
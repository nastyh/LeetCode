"""
Given an array arr[] and an integer k, where arr[i] denotes the number of pages of a book and k denotes total number of students.
All the books need to be allocated to k students in contiguous manner, with each student getting at least one book.
The task is to minimize the maximum number of pages allocated to a student. If it is not possible to allocate books to all students, return -1.
"""
def is_feasible(arr, n, k, max_pages): # it's a helper
    """
    O(nlog(sum(arr) - max(arr))), n num of books
    O(1)
    """
    students_required = 1
    current_pages = 0
    
    for pages in arr:
        if pages > max_pages:
            return False  # A single book has more pages than max_pages
        
        if current_pages + pages > max_pages:
            students_required += 1
            current_pages = pages  # Start a new allocation
            
            if students_required > k:
                return False
        else:
            current_pages += pages
            
    return True

def allocate_books(arr, k):
    """
    The minimum possible maximum allocation is the maximum number of pages in the array (max(arr)).
    The maximum possible maximum allocation is the sum of all pages in the array (sum(arr)).
    Perform binary search between these two limits to find the optimal solution.
    """
    n = len(arr)
    if k > n:
        return -1  # Not enough books for each student to get at least one

    low, high = max(arr), sum(arr)
    result = -1

    while low <= high:
        mid = low + (high - low) // 2
        if is_feasible(arr, n, k, mid):
            result = mid  # Record the feasible solution
            high = mid - 1  # Try for a smaller max allocation
        else:
            low = mid + 1  # Increase the max allocation

    return result

def main():
    # Example input (You can modify as needed)
    arr = [12, 34, 67, 90]
    k = 2

    # Call the function and print the result
    result = allocate_books(arr, k)
    print(f"Minimum maximum pages: {result}")

if __name__ == "__main__":
    main()

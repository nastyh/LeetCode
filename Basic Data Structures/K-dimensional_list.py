# /** Suppose you are given a class that implements a k-dimensional array 
#  * interface and you want to perform an operation that requires you to 
#  * iterate over all elements of the array using its indices. To be 
#  * specific, let's assume we want to calculate the sum of all elements in 
#  * the array. The interface only provides you a get(int[]) method which
#  * allows one to fetch the element at that location given the indices along
#  * each dimension.
#  * 
#  * For e.g, suppose we are dealing with 4D arrays, given [2, 1, 3, 0], the 
#  * class will provide you array[2][1][3][0].
#  *
#  * Write a function that given an instance of the k-D array class and size 
#  * of its dimensions, calculates the sum of all elements.
#  *
#  * @param instance of MultiDimArray class that implements a k-D array of 
#  *        ints which provides a method x.get(int[]) to get the element
#  *        located at the indices in the array
#  * @param array of ints stating the size of each dimension of the k-D array
#  * @return an int which is the sum of all elements in the k-D array
#  *
#  * example: Given object m that holds a 2x2x3 array 
#  * a=[[[3, 2, 2], [1, 5, 0]], [[2, 0, 1], [1, 1, -2]]] (Only for illustration
#  * purposes. This need not be the internal implementation of our k-D array) 
#  * the function call arraySum(m, [2, 2, 3]) should return 16 
#  * (=3+2+2+1+5+2+1+1+1-2)
#  */
# public interface MultiDimArray {
#     int get(int[] indices);
# }

# public int arraySum (MultiDimArrayImpl m, int[] dimensions) {
#     //Implementation here
    
# }

# // dimensions [2,2,3]

# get. 0 0 0
# get  0 0 1
# get  0 0 2
# get. 0 1 0
# get  0 1 1
# get  0 1 2
# get. 1 0 0
# get  1 0 1
# get  1 0 2
# get. 1 1 0
# get  1 1 1
# get  1 1 2

# example = [2, 1, 3, 0]

# position = [0, 0, 0]


# counter = 0
# while:
#     # inc the index
#     counter += get(position)
    
#     # check if you reached end index
    

class MultiDimArray:
    def __init__(self, array):
        self.array = array
    
    def get(self, ix):
        pass

    def all_elements(self, example, dim):  # T: O(n * max(dimensions)), S: O(product of all dimensions)
        def _helper(dim):
            if len(dim) == 1:
                res = [i for i in range(dim[0])]
                # return map(lambda x: [x], list(range(dim[0])))  # similar to line 63
                return res
            else:
                res = []
                for first_el in range(dim[0]):
                    for subarray in _helper(dim[1:]):
                        res.append([first_el] + subarray)
            return res
        numbers = [self.get(position) for position in _helper(dim)]
        return sum(numbers) 

k = MultiDimArray([2, 1, 3, 0])
k.all_elements(k.array, k.dim)
            
    
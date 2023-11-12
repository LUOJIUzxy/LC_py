from array import array
import math

def MinimumPRAM(array1: array, N: int) -> int:
    """
    This function takes an array of integers as input and returns the minimum value.
    The length of array N = 2^k.
    """
    k = int(math.log2(N))  # calculate k using log2 function
    for i in range(k):
        for j in range(0, N, 2**(i+1)):
            if array1[j] > array1[j + 2**i]:
                array1[j] = array1[j + 2**i]
    return array1[0]
    
if __name__ == "__main__":
    my_array = array('i', [5, 3, 8, 1, 9, 2, 7, 4])
    result = MinimumPRAM(my_array, 8)
    print(result)  # Output: 1

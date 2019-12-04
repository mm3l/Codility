#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(A):
    """
    MaxSliceSum
    Find a maximum sum of a compact subsequence of array elements.
    
    note: Kadane's algorithm used
    1) ignore A[0] and A[N-1] since by definition they cannot be a part of any 
    double-slice sum.
    2) define max_sum_ending and max_sum_starting
    3) iterate over i, and find the maximum sum of max_sum_ending and 
        max_sum_starting
    """

    N = len(A)

    max_sum_ending = [0] * N
    max_sum_starting = [0] * N

    for i in range(1, N-1): # ignore A[0] and A[N-1]
        max_sum_ending[i] = max(max_sum_ending[i-1] + A[i], 0)

    for i in range(N-2, 0, -1):
        max_sum_starting[i] = max(max_sum_starting[i+1] + A[i], 0)    

    max_ending = 0
    
    for i in range(1, N-1):
        max_ending = max(max_ending, max_sum_ending[i-1] + max_sum_starting[i+1])

    return max_ending

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_MaxDoubleSliceSum():
    assert solution([3,2,6,-1,4,5,-1,2])   == 17
    assert solution([5,5,5])               == 0

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_MaxDoubleSliceSum()

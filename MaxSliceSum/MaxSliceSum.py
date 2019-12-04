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
    """

    N = len(A)

    if not A:
        return 0

    max_ending = 0
    max_slice = A[0]
    
    for i in range(N):
        max_ending = max(A[i], max_ending + A[i])
        max_slice = max(max_slice, max_ending)

    return max_slice

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_MaxSliceSum():
    assert solution([])           == 0
    assert solution([3,2,-6,4,0]) == 5
    assert solution([-2,1])       == 1
    assert solution([-10])        == -10
    assert solution([-10, -10])   == -10

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_MaxSliceSum()

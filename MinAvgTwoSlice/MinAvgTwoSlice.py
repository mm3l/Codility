#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(A):
    """
    MinAvgTwoSlice
    Finds the minimal average of any slice containing at least two elements.

    Note:
    To check the number of the slices that produce the minimum average, we only
    have to check the sum of the consecutive two or three slices.
    """
    
    N     = len(A)
    index = 0

    if N == 2:
        return 0

    # init the current min average of the first 2 elements
    minavg = (A[0] + A[1]) / 2.0
    
    for i in range(2, N):

        # calculate the sum of the consecutive 2 elements
        sum1 = (A[i - 1] + A[i]) / 2.0
        sum2 = (A[i - 2] + A[i - 1] + A[i]) / 3.0

        if sum1 < minavg:
            index = i - 1
            minavg = sum1
        
        if sum2 < minavg:
            index = i - 2
            minavg = sum2

    return index

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_MinAvgTwoSlice():
   assert solution([4,2,2,5,1,5,8])    == 1
#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_MinAvgTwoSlice()

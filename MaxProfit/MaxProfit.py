#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(A):
    """
    MaxProfit
    Given a log of stock prices compute the maximum possible earning.
    """

    N = len(A)

    if not A:
        return 0

    max_ending = max_slice = 0
    min_starting = A[0]
    for i in range(N):
        max_ending = max(0, A[i] - min_starting)
        min_starting = min(min_starting, A[i])
        max_slice = max(max_slice, max_ending)

    return max_slice

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_MaxProfit():
   assert solution([23171,21011,21123,21366,21013,21367]) == 356
   assert solution([])                                    == 0

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_MaxProfit()

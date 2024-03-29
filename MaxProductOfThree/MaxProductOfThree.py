#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(A):
    """
    MaxProductOfThree
    Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).
    """

    N = len(A)

    A = sorted(A)

    return max(A[0] * A[1] * A[N - 1], A[N - 1] * A[N - 2] * A[N - 3])

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_MaxProductOfThree():
   assert solution([-3,1,2,-2,5,6])     == 60
   assert solution([-10,-2,-4])         == -80
   assert solution([-5, 5, -5, 4])      == 125
   assert solution([-4, -6, 3, 4, 5])   == 120
   assert solution([4, 5, 1, 0])        == 20

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_MaxProductOfThree()

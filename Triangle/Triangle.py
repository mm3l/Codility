#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#
def checkValidity(a, b, c):  
    """
    function to check if three sides  form a triangle or not  
    """

    # check condition  
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True

#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(A):
    """
    Triangle
    Determine whether a triangle can be built from a given set of edges.
    """

    N = len(A)
    A = sorted(A)

    for i in range(0, N-2):
        if checkValidity(A[i], A[i+1], A[i+2]): 
            return 1

    return 0

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_Triangle():
   assert solution([10, 2, 5, 1, 8, 20])    == 1
   assert solution([10, 50, 5, 1])          == 0
   assert solution([10, 2, 5])              == 0
   assert solution([10, 7, 5])              == 1
   assert solution([10, 7, 5, 0, 0, 0])     == 1
   assert solution([0, 0, 10, 7, 5, 0])     == 1

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_Triangle()

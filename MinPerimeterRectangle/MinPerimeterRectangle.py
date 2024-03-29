#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#


#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(N):
    """
    MinPerimeterRectangle
    Count factors of given number n.
    """

    i = 1
    result = 0
    min_perimeter = 2 * (N + N)

    while i * i < N:
 
        if N % i == 0:
            min_perimeter = (2 * (i + (N // i)))
            result += 2
        i += 1

    if i * i == N:
        result += 1
        min_perimeter = (2 * (i + (N // i)))

    return min_perimeter

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_MinPerimeterRectangle():
    assert solution(30)   == 22
    assert solution(1)    == 4
    assert solution(36)   == 24

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_MinPerimeterRectangle()

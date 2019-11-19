#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(A):
    """
    TapeEquilibrium
    Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
    """

    arr_length = len(A)
    min_diff = []
    l_count = 0

    for i in range(0, arr_length-1):

        l_count += A[i]
        
        r_count = 0
        for n in range(arr_length-1, i, -1):
            r_count += A[n]

        min_diff.append(abs(l_count - r_count))
        #print "index:", i, "|" , l_count, " - ", r_count, "| = ", abs(l_count - r_count)

    #print min_diff
    
    return min(min_diff)
    
#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_TapeEquilibrium():
    assert solution([3,1,2,4,3]) == 1

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":

    test_TapeEquilibrium()
    print solution([3,1,2,4,3])

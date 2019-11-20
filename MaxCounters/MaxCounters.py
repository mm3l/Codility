#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(N, A):
    """
    MaxCounters
    Calculates the values of counters after applying all alternating operations: 
    increase counter by 1; set value of all counters to current maximum.
    """

    counters = [0] * N

    for i in range(len(A)):
        if A[i] > N:
            maximum = max(counters)
            for j in range(len(counters)):
                counters[j] = maximum            
        else:
            counters[A[i]-1] += 1

        #print counters

    return counters
    
#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_MaxCounters():
    assert solution(5, [3,4,4,6,1,4,4]) == [3,2,2,4,2]

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":

    test_MaxCounters()
    print solution(5, [3,4,4,6,1,4,4])

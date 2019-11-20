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
    last = 0
    maximum = 0

    for i in range(len(A)):

        if A[i] < (N+1):

            if counters[A[i]-1] < last:
                counters[A[i]-1] = last

            counters[A[i]-1] += 1

            if counters[A[i]-1] > maximum:
                maximum = counters[A[i]-1]

        else:
            last = maximum

    for i in range(len(counters)):
        if counters[i] < last:
            counters[i] = last
        
    return counters
    
#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_MaxCounters():
    assert solution(5,  [3,4,4,6,1,4,4])          == [3,2,2,4,2]
    assert solution(6,  [6,6,6,6,6,6,6])          == [0,0,0,0,0,7]
    assert solution(6,  [3,6,4,5,1,1,2])          == [2,1,1,1,1,1]
    assert solution(6,  [1,2,3,4,5,6,7])          == [1, 1, 1, 1, 1, 1]
    assert solution(6,  [7,7,8,9,10,11,12])       == [0, 0, 0, 0, 0, 0]
    assert solution(6,  [9,1,1,1,1,1,1,1,1,1,9])  == [9, 9, 9, 9, 9, 9]
    assert solution(10, [3,4,4,6,1,4,4])          == [1, 0, 1, 4, 0, 1, 0, 0, 0, 0]
    assert solution(3,  [1,1,1,3,1,1,1])          == [6,0,1]
    assert solution(3,  [1,1,1,1,1,1,6])          == [6,6,6]

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_MaxCounters()

#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(A):
    """
    MissingInteger
    Finds the smallest positive integer that does not occur in a given sequence.
    """

    m = max(A)                   # In case all values in our array are negative 
    if m < 1:
        return 1 

    if len(A) == 1:              # If it contains only one element 
        return 2 if A[0] == 1 else 1     

    positives = {}
    for i in range(len(A)):
        if A[i] > 0:
            positives[A[i]] = i

    positives = sorted(positives)

    elem = 1                     # look in the hash table for all positive ints
    for k in positives:
        print (elem, k)
        if elem < k:
            return elem
        elem += 1

    return elem
    
#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_MissingInteger():
    assert solution([1,3,6,4,1,2])    == 5
    assert solution([1,2,3])          == 4
    assert solution([-1,-3])          == 1
    assert solution([1, 1, 0, -1, -2])  == 2
    assert solution([2, 3, 7, 6, 8, -1, -10, 15])          == 1
    assert solution([2, 3, -7, 6, 8, 1, -10, 15])          == 4

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_MissingInteger()

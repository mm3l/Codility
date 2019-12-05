#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#


#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(A):
    """
    Peaks
    Divide an array into the maximum number of same-sized blocks, each of 
    which should contain an index P such that A[P - 1] < A[P] > A[P + 1].
    Solution:
    1) find all the peaks such that A[P−1] < A[P] and A[P] > A[P+1]
    2) find a integral divisor sized block
    3) If each block contains a peak I return the size.
    """

    N = len(A)
    peaks = []

    for p in range(1, N-1):
        if A[p-1] < A[p] > A[p+1]:
            peaks.append(p)

    if len(peaks) == 0:
        return 0

    for size in range(len(peaks), 0, -1):
        if N % size == 0:
            block_size = N // size
            found = [False] * size
            found_cnt = 0
            for peak in peaks:
                block_nr = peak // block_size
                if found[block_nr] == False:
                    found[block_nr] = True
                    found_cnt += 1
 
            if found_cnt == size:
                return size
    return 0

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_Peaks():
    assert solution([1,2,3,4,3,4,1,2,3,4,6,2]) == 3

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_Peaks()

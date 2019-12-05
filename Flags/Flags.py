#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#
def check(x, peaks, N):

    flags = x
    pos = 0
    while pos < N and flags > 0:
        if peaks[pos]:
            flags -= 1
            pos += x
        else:
            pos += 1

    return flags == 0
#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(A):
    """
    Flags
    Find the maximum number of flags that can be set on mountain peaks.
    """

    N = len(A)
    peaks = [False] * N

    for p in range(1, N-1):
        if A[p-1] < A[p] > A[p+1]:
            peaks[p] = True

    print peaks

    for i in range(N):
        if check(i, peaks, N) == False:
            return i - 1

    return 0

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_Peaks():
    assert solution([1,5,3,4,3,4,1,2,3,4,6,2])      == 3
    assert solution([0,0,0,0,0,1,0,1,0,1])          == 2

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_Peaks()

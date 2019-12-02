#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#


#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(A):
    """
    Dominator
    Find an index of an array such that its value occurs at more than half of
    indices in the array.
    """
    
    N = len(A)
    hist = {}

    if not A or N == 0:
        return -1
        
    for i in range(N):
        hist[A[i]] = hist.get(A[i],0) + 1

    candidate = max(hist, key=hist.get)
    count = hist[candidate]

    leader = -1
    if count > N // 2:
        leader = candidate

    return A.index(leader) if leader != -1 else leader

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_Dominator():
   assert solution([3,4,3,2,3,-1,3,3]) in[0,2,4,6,7]
   assert solution([]) == -1
   assert solution([0,0,1,1,1]) in[2,3,4]
   assert solution([0,0,1,1]) == -1

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_Dominator()

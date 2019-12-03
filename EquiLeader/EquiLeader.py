#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#
def findCandidate(A):
    """
    Finds the candidate of an array
    Returns the candidate or 0 otherwise
    """

    N = len(A)

    size = 0
    value = 0
    for i in range(N):
        if size == 0:
            size += 1
            value = A[i]
        else:
            if value != A[i]:
                size -= 1
            else:
                size += 1

    candidate = -1
    if size > 0:
        candidate = value

    return candidate

#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(A):
    """
    EquiLeader
    Find the index S such that the leaders of the sequences A[0], A[1], ..., 
    A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.
    """

    N = len(A)

    candidate = findCandidate(A)
    leader = 0
    count = 0

    for j in range(N):
        if A[j] == candidate:
            count += 1
    
    if (count > N // 2):        # find the leader
        leader = candidate
    else:
        return 0                # impossible

    leader_count = 0
    equiLeaders = 0
    for i in range(N):
        if A[i] == leader:
            leader_count += 1
        r_leaders = count - leader_count
        if leader_count > (i+1) // 2 and r_leaders > (N-i-1) // 2:
            equiLeaders += 1

    return equiLeaders

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_EquiLeader():
   assert solution([4,3,4,4,4,2])       == 2
   assert solution([0])                 == 0
   assert solution([4,4,2,5,3,4,4,4])   == 3

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_EquiLeader()
    

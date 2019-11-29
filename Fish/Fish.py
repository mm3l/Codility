#!/usr/bin/python
#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#


#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(A, B):
    """
    Fish
    N voracious fish are moving along a river. Calculate how many fish are alive.
    """

    UPSTREAM        = 0
    DOWNSTREAM      = 1
    N               = len(A)
    
    stack           = []
    alive_counter   = 0
     
    for i in range(N):
        if B[i] == DOWNSTREAM:              # DOWNSTREAM
            stack.append(A[i])
        elif B[i] == UPSTREAM:              # UPSTREAM
            while stack:
                if stack[-1] > A[i]:
                    break
                else:
                    stack.pop()
            else:
                alive_counter += 1
             
    alive_counter += len(stack)
     
    return alive_counter

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_Fish():
   assert solution([4,3,2,1,5], [0,1,0,0,0])      == 2
   assert solution([0, 1], [1, 1])                == 2
   assert solution([4,3,2,1,5], [0,0,0,0,0])      == 5

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_Fish()

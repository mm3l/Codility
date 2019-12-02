#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(H):
    """
    StoneWall
    Cover "Manhattan skyline" using the minimum number of rectangles.
    """

    N = len(H)
    stones = 0
    stack = [0] * N
    stack_num = 0

    for i in range(N):
        while stack_num > 0 and stack[stack_num - 1] > H[i]: # the stone wall between the two edges cannot be lower than them
            stack_num -= 1
        if stack_num > 0 and stack[stack_num - 1] == H[i]: # if the two horizontal edges are adjacent to the same stone block, they must be at the same height.
            pass
        else:
            stones += 1
            stack[stack_num] = H[i]
            stack_num += 1

    return stones

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_StoneWall():
   assert solution([8,8,5,7,9,8,7,4,8])      == 7

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_StoneWall()

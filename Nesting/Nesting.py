#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#


#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(S):
    """
    Nesting
    Determine whether a given string of parentheses (single type) is properly nested.
    """

    N = len(S)
    if not S or N == 0:
        return 1

    S = list(S)

    rules = "()"
    left  = "("
    right = ")"

    stack = []

    for char in S:
        if char == left:
            stack.append(char)
        elif char == right:

            if len(stack) == 0:
                return 0
                
            pr = stack.pop() + char

            if pr != rules:
                return 0
        else:
            return 0

    return (0 if len(stack) > 0 else 1)

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_Nesting():
   assert solution("(()(())())")      == 1
   assert solution("())")             == 0

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_Nesting()

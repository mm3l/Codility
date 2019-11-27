#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#


#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(S):
    """
    Brackets
    Determines whether a given string of parentheses (multiple types) is 
    properly nested.
    """

    N = len(S)
    if not S or N == 0:
        return 1

    S = list(S)

    rules  = ["{}", "()", "[]"]
    l_rule = ["{", "(", "["]
    r_rule = ["}", ")", "]"]

    stack = []

    for c in S:
        if c in l_rule:
            stack.append(c)
        elif c in r_rule:

            if len(stack) == 0:
                return 0
                
            br = stack.pop() + c
            if br not in rules:
                return 0
        else:
            return 0

    return (0 if len(stack) > 0 else 1)

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_Brackets():
   assert solution("{[()()]}")      == 1
   assert solution("([)()]")        == 0
   assert solution("")              == 1
   assert solution(")(")            == 0
   assert solution("())(()")        == 0
   assert solution("{[]{()}}")      == 1
   assert solution("[{}{})(]")      == 0

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_Brackets()

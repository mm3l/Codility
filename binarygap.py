#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#
def decimalToBinary(n): 
    """ 
    Function that convert  a decimal number to binary string
    @Note: size of an integer is  assumed to be 32 bits
    @Return An array representing a string of binary digits
    """

    bnum = []
    for i in range(32, -1, -1):
        k = n >> i
        if (k & 1):
            bnum.append("1")
        else:
            bnum.append("0")

    return bnum

#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#

def solution(N):
    
    binary_arr = decimalToBinary(N)

    gaps = []
    for i in range(0, len(binary_arr)):
        if binary_arr[i] == '0':
            continue
        gaps.append(i)

    result = []
    if len(gaps) > 1:
        for j in range(0, len(gaps) -1):
            result.append(gaps[j+1] - gaps[j])
        return max(result) -1
    else:
        return 0

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_binarygap():
    assert solution(1041)       == 5
    assert solution(15)         == 0
    assert solution(32)         == 0
    assert solution(1)          == 0
    assert solution(5)          == 1
    assert solution(6)          == 0
    assert solution(2147483647) == 0
    assert solution(16)         == 0
    assert solution(328)        == 2
    assert solution(9)          == 2
    assert solution(19)         == 2
    assert solution(42)         == 1
    assert solution(1162)       == 3
    assert solution(51712)      == 2
    assert solution(561892)     == 3
    assert solution(66561)      == 9
    assert solution(6291457)    == 20
    assert solution(74901729)   == 4
    assert solution(805306373)  == 25
    assert solution(1376796946) == 5
    assert solution(1073741825) == 29
    assert solution(1610612737) == 28

#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    
    test_binarygap()


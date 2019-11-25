#!/usr/bin/python

#-----------------------------------------------------------------------------#
#                                 Helper Functions                            #
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#                                 Solution                                    #
#-----------------------------------------------------------------------------#
def solution(S, P, Q):
    """
    GenomicRangeQuery
    Finds the minimal nucleotide from a range of sequence DNA.
    """

    dna_factors = { 'A': 1, 'C': 2, 'G': 3, 'T': 4}
    nucleotides = []

    for i in range(len(P)):
        p = P[i]
        q = Q[i]

        if 'A' in S[p:q+1]:
            nucleotides.append(1)
        elif 'C' in S[p:q+1]:
            nucleotides.append(2)
        elif 'G' in S[p:q+1]:
            nucleotides.append(3)
        else:
            nucleotides.append(4)

    return nucleotides

#-----------------------------------------------------------------------------#
#                                 TEST                                        #
#-----------------------------------------------------------------------------#
def test_GenomicRangeQuery():
    assert solution("CAGCCTA", [2,5,0], [4,5,6])          == [2,4,1]
    assert solution("CAGCCTA", [1,2,0], [4,5,6])          == [1,2,1]
#-----------------------------------------------------------------------------#
#                                 MAIN                                        #
#-----------------------------------------------------------------------------#

if __name__ == "__main__":
    test_GenomicRangeQuery()

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

    nucleotides = []
    dna_factors = { 'A': 1, 'C': 2, 'G': 3, 'T': 4}
 
    nucleotides_factors = [0] * len(S)
    
    for i in range(len(S)):
        nucleotides_factors[i] = dna_factors[S[i]]

    #print nucleotides_factors

    p = 0
    q = 0
    for i in range(len(P)):
        p = P[i]
        q = Q[i]
        nucleotide = nucleotides_factors[p:q+1]

        #print p,q, nucleotide
        nucleotides.append(min(nucleotide))

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

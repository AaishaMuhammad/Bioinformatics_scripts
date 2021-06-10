'''
A script that finds all strings of a given length that occur repeatedly within short intervals. 

Input: str Genome, int k - length of string, int l - length of interval, int t
Output: All k-mers that occur at least t times within an interval of l length.

'''

# This function has been written before in the frequent words excercise.
# It may be imported instead of rewritten. 

def FrequencyTable(txt, k):
    freqMap = {}
    txt = str(txt)
    n = len(txt)
    for i in range(n - k+1):
        Pattern = str(txt[i:k+i])
        if Pattern in freqMap:
            freqMap[Pattern] += 1
        else:
            freqMap[Pattern] = 1
    return freqMap

# k, l, t - used for genomic consistency. Substitute if too vague.
def FindClumps(gen, k, l, t):
    patterns = []
    for i in range(0, len(gen)-l):
        window = gen[i:l+i]
        freqMap = FrequencyTable(window, k)
        for s in freqMap.keys():
            if freqMap[s] >= t:
                patterns.append(s)

    patterns = list(dict.fromkeys(patterns))
    return patterns



# Testing on provided debug dataset. Substitute for the .txt data file. 


ans = FindClumps("CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG", 3, 25, 3)

print(" ".join(x for x in ans))


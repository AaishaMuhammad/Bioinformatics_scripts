'''
An improved version of the frequent words script that will account for minor mismatches. 

Input: str Text, int k and d
Output: All frequently occuring k-mers within Text with up to d mismatches. 

'''

# This function has been written previously and can be imported for ease. 
def hamming(genome_a, genome_b):
    h_dis = 0
    for a, b in zip(genome_a, genome_b):
        if a != b:
            h_dis +=1
    return h_dis

# This function has been written previously and can be imported for ease. 
def Neighbors(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ["A", "C", "G", "T"]
    
    neighborhood = []

    suffixNeighbors = Neighbors(pattern[1:], d)

    for text in suffixNeighbors:
        if hamming(pattern[1:], text) < d:
            for n in ["A", "C", "G", "T"]:
                neighborhood.append(n + text)
        else:
            neighborhood.append(pattern[0] + text)
    return neighborhood

# This function has been written previously and can be imported for ease. 
def MaxMap(di):
    return max(di.values())

def FrequentWordsWithMismatches(Text, k, d):
    Patterns = []
    freqMap = {}
    n = len(Text)
    for i in range(0, n-k+1):
        Pattern = Text[i:i+k]
        neighborhood = Neighbors(Pattern, d)
        for neighbor in neighborhood:
            if neighbor in freqMap:
                freqMap[neighbor] += 1
            else:
                freqMap[neighbor] = 1
    
    m = MaxMap(freqMap)

    for pattern in freqMap:
        if freqMap[pattern] == m:
            Patterns.append(pattern)
    return Patterns


# Testing on provided debug dataset. Substitute for the .txt data file.

ans = FrequentWordsWithMismatches("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1)
print(" ".join(x for x in ans))
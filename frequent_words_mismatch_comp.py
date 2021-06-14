'''
A final improved version of the frequent words script that accounts for the reverse complement as well as a certain amount of mismatches. 

'''

def hamming(genome_a, genome_b):
    h_dis = 0
    for a, b in zip(genome_a, genome_b):
        if a != b:
            h_dis +=1
    return h_dis

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

def MaxMap(di):
    return max(di.values())

def DnaReverse(txt):
    newtxt = list(txt)
    nucs = {
        "A":"T",
        "C":"G",
        "G":"C",
        "T":"A",
    }
    for i in range(len(txt)):
        newtxt[i] = nucs[txt[i]]
    newdna = "".join(newtxt)
    newdna = newdna[::-1]
    return newdna

def FrequentWordsWithMismatches(Text, k, d):
    Patterns = []
    freqMap = {}
    n = len(Text)
    rev = DnaReverse(Text)
    for i in range(0, n-k+1):
        Pattern = Text[i:i+k]
        rev_pattern = rev[i:i+k]
        neighborhood = Neighbors(Pattern, d)
        rev_neighborhood = Neighbors(rev_pattern, d)

        for neighbor in neighborhood:
            if neighbor in freqMap:
                freqMap[neighbor] += 1
            else:
                freqMap[neighbor] = 1
        for neighbor in rev_neighborhood:
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
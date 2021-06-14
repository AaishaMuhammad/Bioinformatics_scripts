'''
Final project to discover the ORI for salmonella Enterica. This is an ungraded project due to the Salmonella Ori not being experimentally confirmed. 

All scripts used here have been written previously and can be imported for ease. 

'''

def min_skew(genome):
    skew_count = 0
    minim = 0
    minims_list = list()
    for i in range(0, len(genome)+1):
        if genome[i-1] == "G":
            skew_count +=1
        elif genome[i-1] == "C":
            skew_count -= 1

        if skew_count < minim:
            minim = skew_count
            minims_list = [i]
        elif skew_count == minim:
            minims_list.append(i)
        else:
            pass

    return minims_list

    
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
        for neighbor in neighborhood:
            if neighbor in freqMap:
                freqMap[neighbor] += 1
            else:
                freqMap[neighbor] = 1
        rev_neighborhood = Neighbors(rev_pattern, d)
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

f = open("./salmonella_enterica.txt")
genome = f.read()
skew_pos = int(min(min_skew(genome))) # Finding minimum skew to define scanning window. 
window = genome[skew_pos:skew_pos+500] # Specifying a window of 500 nucleotides.
out = FrequentWordsWithMismatches(window, 9, 1) 

print(" ".join(x for x in out))

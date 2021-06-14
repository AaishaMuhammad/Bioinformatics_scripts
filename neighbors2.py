'''
A script to regenerate a given strings with up to d mismatches.

Input: str Pattern
Output: list of all genomic strings with up to d mismatches.

'''

# This function has been written previously and can be imported for ease. 
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



# Testing on provided debug dataset. Substitute for the .txt data file.

ans = Neighbors("ACG", 1)
print(" ".join(x for x in ans))
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
    
def count(pattern, genome, d):
    count = 0
    for i in range(len(genome) - len(pattern)+1):       
        pat = genome[i:i+len(pattern)]
        if hamming(pattern, pat) <= d:
            count +=1
    return count

def MotifEnumeration(Dna, k, d):
    Patterns = list()
    dna_list = Dna.split()
    first = dna_list[0]
    all_neighbors = list()
    for index in range(len(first)-k+1): 
        pat = first[index:index+k]
        neighbors = Neighbors(pat, d)
        all_neighbors.extend(neighbors)

    for neighbor in all_neighbors:
        if all(count(neighbor, string, d) != 0 for string in dna_list):
            Patterns.append(neighbor)


    Patterns = list(dict.fromkeys(Patterns))
    return Patterns

out = MotifEnumeration("TCACACAACCAATGCCAACTCTCGT AAGTTGGCTCGCTAGCAGTATAACA TAACATCACGGTTAAGACGCGCCCA ACTCTAGGGAGATAACAACGTCGAT CCCACAATTCTAGTTAAACCGTCAT TAGAAGAACTAGGTAACATCGGCCG", 5, 2)
ans = " ".join(x for x in out)
print(ans)
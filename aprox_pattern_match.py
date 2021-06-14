'''
A script to find all instances where a given string appears within the genome, with some specified amount of mismatches. 

Input: strings pattern and genome, int d
Output: List of starting positions of Pattern within Genome, with up to d mismatches. 

'''

# This script has been written previously and can be imported for ease. 
def hamming(genome_a, genome_b):
    h_dis = 0
    for a, b in zip(genome_a, genome_b):
        if a != b:
            h_dis +=1
    return h_dis

def aprox_pat_match (pattern, genome, d):
    starters = list()
    for i in range(len(genome) - len(pattern)+1):
        if hamming(pattern, genome[i:i+len(pattern)]) <= d:
            starters.append(str(i))
    return starters


# Testing on provided debug dataset. Substitute for the .txt data file.

ans = aprox_pat_match("ATTCTGGA", "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT", 3)
print(" ".join(x for x in ans))
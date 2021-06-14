'''
A script to count the total occurrences of pattern in genome with up to d mismatches.

'''

def hamming(genome_a, genome_b):
    h_dis = 0
    for a, b in zip(genome_a, genome_b):
        if a != b:
            h_dis +=1
    return h_dis

def count(pattern, genome, d):
    count = 0
    for i in range(len(genome) - len(pattern)+1):       
        pat = genome[i:i+len(pattern)]
        if hamming(pattern, pat) <= d:
            count +=1
    return count


# Testing on provided debug dataset. Substitute for the .txt data file.

print(count("GAGG", "TTTAGAGCCTTCAGAGG", 2))

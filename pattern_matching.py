'''
A script to find all the positions where a given string occurs in a longer genome. 

Input: Strings Pattern and Genome
Output: All starting positions where Pattern occurs in Genome.

'''


def pattern_match(gen, pat):
    starters = []
    for i in range(len(gen) - len(pat) + 1):
        if gen[i:i+len(pat)] == pat:
            starters.append(i)

    return starters


# Testing on provided debug dataset. Substitute for the .txt data file.

ans = pattern_match("AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT", "TTT")

print(" ".join(str(x) for x in ans))

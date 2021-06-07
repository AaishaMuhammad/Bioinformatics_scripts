'''A script to count how many times a specicfic pattern occurs within a larger genome.

Input: genome, pattern
Output: Number of times 'pattern' occurs in 'genome'.'''


def PatternCount(gen, pat):
    count = 0
    for i in range(len(gen) - len(pat) +1):
        if gen[i:i+len(pat)] == pat:
            count += 1
    return(count)


# Testing on provided debug dataset. Substitute for the .txt data file. 


print(PatternCount("CTGTTTTTGATCCATGATATGTTATCTCTCCGTCATCAGAAGAACAGTGACGGATCGCCCTCTCTCTTGGTCAGGCGACCGTTTGCCATAATGCCCATGCTTTCCAGCCAGCTCTCAAACTCCGGTGACTCGCGCAGGTTGAGTA", "CTC"))
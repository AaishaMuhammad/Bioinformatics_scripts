'''
A script that finds the index/s of the genome where GC Skew is minimum. 

Input: str genome
Output: list of indices where GC Skew is minimum. 

'''

def min_skew(genome):
    skew_count = 0
    minim = 0
    minims_list = list()

    for index, item in enumerate(genome, start=1):
        if item == "G":
            skew_count += 1
        elif item == "C":
            skew_count -= 1

        if skew_count < minim:
            minim = skew_count
            minims_list = [index]
        elif skew_count == minim:
            minims_list.append(index)

    return minims_list


# Testing on provided debug dataset. Substitute for the .txt data file.
            
ans = min_skew("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT")
print(" ".join(str(x) for x in ans))


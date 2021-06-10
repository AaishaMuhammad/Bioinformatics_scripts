'''
A script to calculate the GC Skew of a given genome

Input: str genome
Output: list of int skew values

'''

def skew(genome):
    skew_list = [0]
    skew_count = 0
    for i in genome:
        if i == "G":
            skew_count += 1
        elif i == "C":
            skew_count -= 1
        else:
            pass
        skew_list.append(skew_count)
    return skew_list


# Testing on provided debug dataset. Substitute for the .txt data file.
ans=skew("CATGGGCATCGGCCATACGCC")
ans = " ".join(str(x) for x in ans)

# Automated checks with provided answers to reduce human error.
# Not applicable for problem sets.
if ans == "0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2":
    print(ans)

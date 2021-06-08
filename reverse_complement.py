'''
A script that produces the reverse complement of a given genome, by substituing each nucleotide with its complement, then reversing the result string.

'''

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


# Testing on provided debug dataset. Substitute for the .txt data file.


ans = DnaReverse("AAAACCCGGT")

# Output verification using provided debug answers, to reduce human-error during debugging. 
# Do not implement this step with actual data.

if ans == "ACCGGGTTTT":
    print(ans)
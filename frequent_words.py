'''
A script that counts the frequency of fixed-length strings within a larger genome.

Input: str genome, int k
Output: Most frequent strings of length k within genome

'''

def MaxMap(di):
    return max(di.values())


# Counts k-mers within genome, outputs a dictionary k-mer:count
def FrequencyTable(txt, k):
    freqMap = {}
    txt = str(txt)
    n = len(txt)
    for i in range(n - k+1):
        Pattern = str(txt[i:k+i])
        if Pattern in freqMap:
            freqMap[Pattern] += 1
        else:
            freqMap[Pattern] = 1
    return freqMap


# Generates frequency table, finds maximum point. Outputs most frequent k-mer/s
def BetterFrequentWords(txt, k):
    FrequentPatterns = []
    freqMap = FrequencyTable(txt, k)
    maxi = MaxMap(freqMap)
    for i in freqMap:
        if freqMap[i] == maxi:
            FrequentPatterns.append(i)
    return FrequentPatterns


# Testing on provided debug dataset. Substitute for the .txt data file. 

ans = BetterFrequentWords("CCAGCGGGGGTTGATGCTCTGGGGGTCACAAGATTGCATTTTTATGGGGTTGCAAAAATGTTTTTTACGGCAGATTCATTTAAAATGCCCACTGGCTGGAGACATAGCCCGGATGCGCGTCTTTTACAACGTATTGCGGGGTAAAATCGTAGATGTTTTAAAATAGGCGTAAC", 5)

print(" ".join(x for x in ans))

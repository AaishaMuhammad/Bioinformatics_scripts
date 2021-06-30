def ImmediateNeighbors(Pattern):
    neighborhood = [Pattern]
    nucs = ["A", "T", "C", "G"]
    for i in range(len(Pattern)):
        symbol = Pattern[i]
        for nuc in nucs: 
            if nuc != symbol:
                neighborhood.append(Pattern[:i] + nuc + Pattern[i+1:])
    return neighborhood

ans = ImmediateNeighbors("ACA")
print(" ".join(x for x in ans))
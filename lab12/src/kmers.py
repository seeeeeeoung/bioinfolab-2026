seq = "TATGGGGTGC"
k = 5
kmers = []
for i in range(len(seq) - k + 1):
    kmers.append(seq[i:i + k])
for km in kmers:
    print(km)
print("k-mer 개수:", len(kmers))

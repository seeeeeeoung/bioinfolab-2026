import sys

def read_fastq(filename):
    records = []
    with open(filename) as f:
        lines = f.readlines()
    for i in range(0, len(lines), 4):
        name = lines[i].rstrip()[1:]
        seq = lines[i + 1].rstrip()
        qual = lines[i + 3].rstrip()
        records.append((name, seq, qual))
    return records

reads = read_fastq(sys.argv[1])

# 위치마다 품질 점수 합계와 read 개수를 따로 센다
sums = []
counts = []
for name, seq, qual in reads:
    for pos in range(len(qual)):
        score = ord(qual[pos]) - 33
        if pos >= len(sums):
            sums.append(0)
            counts.append(0)
        sums[pos] = sums[pos] + score
        counts[pos] = counts[pos] + 1

print("위치\t평균품질\tread수")
for pos in range(len(sums)):
    print(str(pos + 1) + "\t" + str(round(sums[pos] / counts[pos], 2)) + "\t" + str(counts[pos]))

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
print("read 개수:", len(reads))
print("첫 read 이름:", reads[0][0])
print("첫 read 서열:", reads[0][1])
print("첫 read 길이:", len(reads[0][1]))

# 서열 길이와 품질 길이가 같은지 모든 read 검사
bad = 0
for name, seq, qual in reads:
    if len(seq) != len(qual):
        bad = bad + 1
        print("길이 다름:", name, len(seq), len(qual))
print("길이가 다른 read 개수:", bad)

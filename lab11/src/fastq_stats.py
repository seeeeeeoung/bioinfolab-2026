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

def mean_quality(qual):
    scores = []
    for ch in qual:
        scores.append(ord(ch) - 33)
    return sum(scores) / len(scores)

print("파일\tread개수\t평균길이\t평균품질\t최소길이\t최대길이")
for filename in sys.argv[1:]:
    reads = read_fastq(filename)
    lengths = []
    total_q = 0
    for name, seq, qual in reads:
        lengths.append(len(seq))
        total_q = total_q + mean_quality(qual)
    n = len(reads)
    print(filename + "\t" + str(n) + "\t" + str(round(sum(lengths) / n, 2)) + "\t"
          + str(round(total_q / n, 2)) + "\t" + str(min(lengths)) + "\t" + str(max(lengths)))

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

def base_name(name):
    # 이름의 첫 단어만 쓰고, 끝의 /1 또는 /2 는 뗀다
    first = name.split()[0]
    if first.endswith("/1") or first.endswith("/2"):
        first = first[:-2]
    return first

r1 = read_fastq(sys.argv[1])
r2 = read_fastq(sys.argv[2])
print("파일1 read 개수:", len(r1))
print("파일2 read 개수:", len(r2))
print("개수가 같은가:", len(r1) == len(r2))

bad = 0
for i in range(min(len(r1), len(r2))):
    n1 = base_name(r1[i][0])
    n2 = base_name(r2[i][0])
    if n1 != n2:
        bad = bad + 1
        if bad <= 5:
            print("짝이 안 맞음:", i + 1, r1[i][0], "/", r2[i][0])
print("짝이 안 맞는 read 수:", bad)
print("첫 번째 짝:", r1[0][0], "|", r2[0][0])
print("마지막 짝:", r1[-1][0], "|", r2[-1][0])

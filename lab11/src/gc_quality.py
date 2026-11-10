import sys
import os

# 07번에서 만든 fasta.py의 gc_content 함수를 불러온다
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "..", "lab07", "src"))
from fasta import gc_content

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

reads = read_fastq(sys.argv[1])

# read마다 (GC 비율, 평균 품질, 이름)을 모은다
data = []
for name, seq, qual in reads:
    data.append((gc_content(seq), mean_quality(qual), name))

total = 0
for gc, q, name in data:
    total = total + q
overall = total / len(data)
print("전체 read 수:", len(data))
print("전체 평균 품질:", round(overall, 2))

# GC 비율 순서로 정렬해서 가장 낮은 10개, 가장 높은 10개를 고른다
data.sort()
low10 = data[:10]
high10 = data[-10:]

for title, group in [("GC 비율이 가장 낮은 10개", low10), ("GC 비율이 가장 높은 10개", high10)]:
    print()
    print(title)
    print("GC비율\t평균품질\t이름")
    s = 0
    for gc, q, name in group:
        print(str(round(gc, 3)) + "\t" + str(round(q, 2)) + "\t" + name)
        s = s + q
    print("이 10개의 평균 품질:", round(s / len(group), 2), "/ 전체 평균과 차이:", round(s / len(group) - overall, 2))

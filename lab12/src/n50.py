import sys
import os

# 스크립트 위치를 기준으로 lab07/src 의 fasta.py 를 불러온다
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "..", "lab07", "src"))
from fasta import read_fasta

def n50(lengths):
    lengths = sorted(lengths, reverse=True)
    total = sum(lengths)
    half = total / 2
    running = 0
    for length in lengths:
        running = running + length
        if running >= half:
            return length

# 인자 검사
if len(sys.argv) != 2:
    print("사용법: python3 n50.py <contigs.fasta>")
    sys.exit(1)

# 파일 검사
if not os.path.isfile(sys.argv[1]):
    print("오류: 파일이 없습니다:", sys.argv[1])
    sys.exit(1)

seqs = read_fasta(sys.argv[1])
lengths = []
for name in seqs:
    lengths.append(len(seqs[name]))
print("contig 개수:", len(lengths))
print("전체 길이:", sum(lengths))
print("가장 긴 contig:", max(lengths))
print("N50:", n50(lengths))

# contig 길이를 긴 것부터 정렬해서 lab12/doc/contig_lengths.txt 에 저장
# (스크립트 위치 기준이라 어느 폴더에서 실행해도 같은 곳에 저장된다)
out_path = os.path.join(here, "..", "doc", "contig_lengths.txt")
sorted_lengths = sorted(lengths, reverse=True)
count = 0
with open(out_path, "w") as out:
    for length in sorted_lengths:
        out.write(str(length) + "\n")
        count = count + 1
print("저장한 줄 수:", count)

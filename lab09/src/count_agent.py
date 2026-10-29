"""FASTA 파일의 서열 개수를 출력한다.

사용법: python3 count_agent.py 파일.fasta
"""
import sys

if len(sys.argv) != 2:
    print("사용법: python3 count_agent.py 파일.fasta")
    sys.exit(1)

count = 0
with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith(">"):
            count = count + 1
print(count)

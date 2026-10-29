"""FASTA 파일의 서열 개수를 출력한다. (lab07의 read_fasta 사용)

사용법: python3 count_agent2.py 파일.fasta
"""
import sys
import os

# 이 스크립트 위치를 기준으로 lab07/src를 찾아 경로에 추가한다
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "..", "lab07", "src"))
from fasta import read_fasta

if len(sys.argv) != 2:
    print("사용법: python3 count_agent2.py 파일.fasta")
    sys.exit(1)

filename = sys.argv[1]
if not os.path.isfile(filename):
    print("오류: 파일이 없습니다: " + filename)
    sys.exit(1)

seqs = read_fasta(filename)
print(len(seqs))

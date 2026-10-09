#!/usr/bin/env python3
# shortlines.py — FASTA 파일에서 최소 길이보다 짧은 서열 줄의 개수를 출력한다
# 사용법: python3 shortlines.py <FASTA파일> <최소길이>

import sys
import os

if len(sys.argv) < 3:
    print("사용법: python3 shortlines.py <FASTA파일> <최소길이>")
    sys.exit(1)

filename = sys.argv[1]

if not os.path.isfile(filename):
    print("오류: 파일을 찾을 수 없습니다:", filename)
    sys.exit(1)

if not sys.argv[2].isdigit():
    print("오류: 최소길이는 숫자여야 합니다:", sys.argv[2])
    sys.exit(1)

minlen = int(sys.argv[2])

n = 0
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if not line.startswith(">"):
            if len(line) < minlen:
                n = n + 1

print(n)

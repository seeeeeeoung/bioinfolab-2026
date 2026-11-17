#!/usr/bin/env python3
# contig 길이 목록의 N50을 계산하는 연습 코드
import sys

# 인자 검사: 이 스크립트는 인자를 받지 않는다
if len(sys.argv) != 1:
    print("사용법: python3 n50_test.py")
    sys.exit(1)

lengths = [12, 3, 20, 8, 1, 15, 6]

# 1. 긴 것부터 정렬
sorted_lengths = sorted(lengths, reverse=True)

# 2. 누적 합 구하기
cumsum = []
total = 0
for length in sorted_lengths:
    total = total + length
    cumsum.append(total)

# 3. 전체 길이와 절반 값
half = total / 2

# 4. 누적 합이 절반 이상이 되는 첫 contig의 길이 = N50
n50 = 0
for i in range(len(sorted_lengths)):
    if cumsum[i] >= half:
        n50 = sorted_lengths[i]
        break

print("정렬한 길이:", sorted_lengths)
print("누적 합:", cumsum)
print("전체 길이:", total)
print("절반 값:", half)
print("N50:", n50)

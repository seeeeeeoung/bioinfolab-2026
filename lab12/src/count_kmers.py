#!/usr/bin/env python3
# count_kmers.py
# 길이가 L인 서열에서 만들 수 있는 k-mer 개수를 공식(L - k + 1)으로 구하고,
# 실제 서열을 한 글자씩 밀면서 직접 센 값과 비교한다.
#
# 사용법: python3 count_kmers.py   (인자 없음)

import sys


def count_kmers(L, k):
    # k가 L보다 크면 k-mer를 하나도 만들 수 없다
    if k > L:
        return 0
    return L - k + 1


def count_kmers_direct(L, k):
    # 길이 L인 서열을 실제로 만들고, 한 글자씩 밀면서 k-mer를 잘라 센다
    seq = "A" * L
    count = 0
    for i in range(len(seq)):
        kmer = seq[i:i + k]
        # 끝부분에서 잘린 조각은 길이가 k보다 짧으므로 세지 않는다
        if len(kmer) == k:
            count = count + 1
    return count


# 인자 검사: 이 스크립트는 인자를 받지 않는다
if len(sys.argv) != 1:
    print("사용법: python3 count_kmers.py")
    sys.exit(1)

tests = [(10, 5), (10, 1), (10, 10), (150, 31), (150, 111), (3, 5)]

print("L\tk\t공식\t직접\t일치")
for pair in tests:
    L = pair[0]
    k = pair[1]
    formula = count_kmers(L, k)
    direct = count_kmers_direct(L, k)
    if formula == direct:
        same = "O"
    else:
        same = "X"
    print(str(L) + "\t" + str(k) + "\t" + str(formula) + "\t" + str(direct) + "\t" + same)

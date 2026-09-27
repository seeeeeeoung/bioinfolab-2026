#!/usr/bin/bash
# topwords.sh — 텍스트 파일에서 가장 많이 나오는 단어 10개와 그 횟수를 구해 파일로 저장한다
#               대소문자는 구분하지 않는다 (문제 1-2의 파이프라인)
# 사용법: topwords.sh <입력파일> <결과파일>
# 예: ./src/topwords.sh data/alice.txt doc/top10.txt

IN=$1     # 첫 번째 인자: 분석할 파일
OUT=$2    # 두 번째 인자: 결과를 저장할 파일

cat $IN | tr -s " " "\n" | tr "A-Z" "a-z" | sort | uniq -c | sort -nr | head -10 > $OUT

echo "$IN 의 상위 10개 단어를 $OUT 에 저장했습니다."
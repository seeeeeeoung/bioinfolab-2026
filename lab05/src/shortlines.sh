#!/usr/bin/bash
# shortlines.sh — FASTA 파일에서 최소 길이보다 짧은 서열 줄의 개수를 출력한다
# 사용법: shortlines.sh <FASTA파일> <최소길이>
if [ -z "$1" ] || [ -z "$2" ]
then
echo "사용법: $0 <FASTA파일> <최소길이>"
echo " 최소길이보다 짧은 서열 줄의 개수를 출력합니다."
exit 1
fi
if [ ! -f "$1" ]
then
echo "오류: 파일을 찾을 수 없습니다: $1"
exit 1
fi
if ! echo "$2" | grep -q "^[0-9][0-9]*$"
then
echo "오류: 최소길이는 숫자여야 합니다: $2"
exit 1
fi
FILE="$1"
MIN="$2"
grep -v ">" "$FILE" | while read LINE
do
if [ "${#LINE}" -lt "$MIN" ]
then
echo "$LINE"
fi
done | wc -l
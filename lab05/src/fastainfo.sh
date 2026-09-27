#!/usr/bin/bash
# fastainfo.sh — FASTA 파일의 요약 정보를 출력한다
# 사용법: fastainfo.sh <FASTA파일>
if [ -z "$1" ]
then
echo "사용법: $0 <FASTA파일>"
echo " 파일 이름, 서열 개수, 서열 이름 목록, 총 염기 수를 출력합니다."
exit 1
fi
if [ ! -f "$1" ]
then
echo "오류: 파일을 찾을 수 없습니다: $1"
exit 1
fi
FILE="$1"
echo "파일: $FILE"
echo "서열 개수: $(grep -c ">" "$FILE")"
echo "서열 이름:"
grep ">" "$FILE" | cut -d " " -f 1 | tr -d ">"
echo "총 염기 수(대략): $(grep -v ">" "$FILE" | tr -d "\n" | wc -c)"
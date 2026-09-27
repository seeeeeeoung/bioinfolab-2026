#!/usr/bin/bash
# batchinfo.sh — 폴더 안 모든 FASTA 파일의 서열 개수를 표로 출력한다
# 사용법: batchinfo.sh <폴더>
if [ -z "$1" ]
then
echo "사용법: $0 <폴더>"
echo " 폴더 안 모든 FASTA 파일의 이름과 서열 개수를 출력합니다."
exit 1
fi
if [ ! -d "$1" ]
then
echo "오류: 폴더를 찾을 수 없습니다: $1"
exit 1
fi
DIR="$1"
echo -e "file\tcount"
for F in "$DIR"/*.fasta
do
if [ ! -f "$F" ]
then
echo "오류: $DIR 폴더에 FASTA 파일이 없습니다"
exit 1
fi
echo -e "$(basename "$F")\t$(grep -c ">" "$F")"
done
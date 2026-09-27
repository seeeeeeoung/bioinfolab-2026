#!/usr/bin/bash
if [ -z "$1" ]
then
echo "사용법: $0 <출력폴더>"
exit 1
fi
OUT="$1"
mkdir -p "$OUT"
echo "결과" > "$OUT/result.txt"
cat "$OUT/result.txt"
#!/usr/bin/bash
# printn.sh — 1부터 첫 번째 인자로 받은 수까지 출력한다
# 사용법: printn.sh <개수>
for X in $(seq 1 $1)
do
echo $X
done
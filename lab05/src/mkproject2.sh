#!/usr/bin/bash
# mkproject2.sh — 프로젝트 폴더를 만들고 그 안에 data, doc, src 폴더를 만든다
# 사용법: mkproject2.sh <프로젝트이름>
if [ -z "$1" ]
then
echo "사용법: $0 <프로젝트이름>"
echo " 프로젝트 폴더와 그 안의 data, doc, src 폴더를 만듭니다."
exit 1
fi
NAME="$1"
if [ -d "$NAME" ]
then
echo "오류: 같은 이름의 폴더가 이미 있습니다: $NAME"
exit 1
fi
mkdir -p "$NAME/data" "$NAME/doc" "$NAME/src"
echo "만들어진 구조:"
ls -R "$NAME"
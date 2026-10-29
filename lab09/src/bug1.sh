#!/usr/bin/bash
# 인자가 없거나 디렉터리가 아니면 사용법을 보여주고 끝낸다
if [ $# -ne 1 ]; then
    echo "사용법: $0 <디렉터리>"
    exit 1
fi

DIR="$1"
if [ ! -d "$DIR" ]; then
    echo "오류: 디렉터리가 없습니다: $DIR"
    exit 1
fi

ls "$DIR"

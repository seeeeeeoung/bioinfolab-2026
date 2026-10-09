#!/usr/bin/env python3
# mkproject.py — 프로젝트 폴더를 만들고 그 안에 data, doc, src 폴더를 만든다
# 사용법: python3 mkproject.py <프로젝트이름>

import sys
import os

if len(sys.argv) < 2:
    print("사용법: python3 mkproject.py <프로젝트이름>")
    sys.exit(1)

name = sys.argv[1]

if os.path.isdir(name):
    print("오류: 같은 이름의 폴더가 이미 있습니다:", name)
    sys.exit(1)

for sub in ["data", "doc", "src"]:
    os.makedirs(name + "/" + sub)

print(name, "프로젝트를 만들었습니다.")

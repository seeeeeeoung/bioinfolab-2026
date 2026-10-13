# 나의 bash + 파이썬 치트시트 (03~06)

## 스크립트 만드는 다섯 단계
| 단계 | bash | 파이썬 |
|---|---|---|
| 1 | 터미널에서 직접 실행 | 대화형 파이썬(`>>>`)에서 실행 |
| 2 | 파일로 옮겨 `bash src/x.sh` | 파일로 옮겨 `python3 src/x.py` |
| 3 | `FILE="data/seqs.fasta"` | `filename = "data/seqs.fasta"` |
| 4 | `FILE="$1"` | `filename = sys.argv[1]` |
| 5 | `[ -z "$1" ]`, `[ ! -f "$1" ]`, `exit 1` | `len(sys.argv) < 2`, `os.path.isfile()`, `sys.exit(1)` |

## 내가 실제로 한 실수
- bash `DIR = $1` → `=` 양쪽 공백 금지 / 파이썬은 `name = "x"` 공백 있어도 됨
- bash 따옴표 빠뜨림("my project" 쪼개짐) / 파이썬은 `sys.argv[1]`이 하나의 글자라 문제없음
- bash `done` 빠뜨림 / 파이썬은 `for`, `if` 끝의 콜론(`:`)과 들여쓰기 4칸 빠뜨림
- 파이썬 `"길이:" + len(seq)` → TypeError. `str()`로 바꾸거나 쉼표로 넘기기
- 파이썬 `rstrip()` 빠뜨림 → 서열 길이가 줄마다 1씩 길어짐

## 고장 났을 때
| 하려는 일 | bash | 파이썬 |
|---|---|---|
| 오류 읽기 | 마지막 줄부터 | Traceback 마지막 줄부터 (오류 종류: 원인) |
| 종료 상태 | `echo $?` | 똑같이 `echo $?` (오류 나면 1) |
| 실행 추적 | `set -x` | 중간에 `print()` 넣기 |

## 따옴표와 변수
| 하려는 일 | bash | 파이썬 |
|---|---|---|
| 변수 만들기 | `NAME=gene1` | `name = "gene1"` |
| 값 꺼내기 | `$NAME` | `name` (달러 없음) |
| 글자 표시 | 따옴표 없어도 됨 | 반드시 따옴표 |

## 검사식
| 하려는 일 | bash | 파이썬 |
|---|---|---|
| 인자 없음 | `[ -z "$1" ]` | `len(sys.argv) < 2` |
| 파일 없음 | `[ ! -f "$1" ]` | `not os.path.isfile(f)` |
| 폴더 있음 | `[ -d "$1" ]` | `os.path.isdir(d)` |
| 숫자 비교 | `[ "$A" -lt 13 ]` | `a < 13` |
| 그리고 / 또는 / 아님 | `&&` / `\|\|` / `!` | `and` / `or` / `not` |
| 숫자인가 | `grep -q "^[0-9][0-9]*$"` | `s.isdigit()` |
| 실패로 끝내기 | `exit 1` | `sys.exit(1)` |

## 자주 쓸 명령어
| 하려는 일 | bash | 파이썬 |
|---|---|---|
| 서열 개수 | `grep -c ">" 파일` | `line.startswith(">")`이면 `n = n + 1` |
| 서열 이름 | `cut -d " " -f 1 \| tr -d ">"` | `line[1:].split()[0]` |
| 총 염기 수 | `grep -v ">" \| tr -d "\n" \| wc -c` | `total = total + len(line.rstrip())` |
| 글자 수 | `${#SEQ}` | `len(seq)` |
| 특정 글자 개수 | `grep -o G \| wc -l` | `seq.count("G")` |
| 한 줄씩 읽기 | `while read LINE` | `for line in f:` |
| 여러 파일 | `data/*.fasta` | `glob.glob("data/*.fasta")` |
| 폴더 만들기 | `mkdir -p a/b` | `os.makedirs("a/b")` |
| 결과 저장 | `> result.tsv` | 옮기지 않음: 07번에서 배울 예정, 지금은 bash의 `>` 사용 |

## 파이썬으로 푼 것 (05번에서 막혔던 것)
- 소수 계산: `gc / len(seq)`, `round(x, 4)`
- 이름으로 값 찾기: 딕셔너리 `counts["seqs.fasta"]`
- 앞줄 기억: `name` 변수 하나
- 조건 여러 개: `and`로 한 줄

## 파이썬으로 옮길 필요 없는 것
- `cd`, `ls`, `chmod`, `git`: 파일과 폴더를 다루는 일은 터미널(bash)이 더 간단함

## 07. 함수와 파일 저장

### def로 함수 만들기
```python
def 함수이름(받을값):
    계산
    return 돌려줄값
```

### print와 return의 차이
`print`는 화면에 보여 주고 끝나지만, `return`은 값을 다음 코드에 넘겨주어 계산을 이어 갈 수 있게 한다.

### 모듈 불러오기
```python
from 모듈 import 함수
```
`모듈`은 파일 이름에서 `.py`를 뺀 것이고, 모듈과 스크립트는 같은 폴더에 둔다.

### if __name__ == "__main__":
모듈에 시험 코드를 넣을 때 쓴다. 그 파일을 직접 실행했을 때만 돌고, 다른 파일이 import할 때는 실행되지 않는다.

### "w"와 "a"
- `open(파일, "w")`: 새로 쓴다. 있던 내용은 지워진다. bash의 `>`와 같다.
- `open(파일, "a")`: 끝에 이어 쓴다. bash의 `>>`와 같다.

### 오늘 겪은 오류 두 가지
1. `ZeroDivisionError: division by zero` : 빈 서열의 길이가 0이라 `gc / len(seq)`가 0으로 나누기가 됨. `if len(seq) == 0: return 0.0`으로 해결.
2. `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'` : `return` 없이 `print`만 하는 함수의 결과(`None`)에 1을 더해서 발생. 값이 필요하면 `return`을 쓴다.

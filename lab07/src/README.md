# fasta.py 도구 상자

FASTA 서열 파일을 읽고, 계산하고, 저장하는 함수 모음이다. 사용하려면 `src` 폴더 안의 스크립트에서 `from fasta import 함수이름`으로 불러온다.

## 함수 목록

### read_fasta(filename)
- 받는 것: FASTA 파일 이름 / 돌려주는 것: `{서열 이름: 서열}` 딕셔너리 (서열은 모두 대문자, 여러 줄은 한 줄로 합쳐짐, 이름은 제목 줄의 첫 단어만 사용)
- 예: `seqs = read_fasta("../data/seqs.fasta")`

### gc_content(seq)
- 받는 것: 서열 문자열 / 돌려주는 것: 전체 글자 중 G와 C의 비율(0~1 사이 숫자), 빈 서열이면 0.0
- 예: `gc = gc_content(seqs["gene1"])`

### write_fasta(seqs, filename)
- 받는 것: `{서열 이름: 서열}` 딕셔너리와 저장할 파일 이름 / 돌려주는 것: 없음 (파일을 만들어 저장하며, 같은 이름의 파일이 있으면 덮어씀)
- 예: `write_fasta(selected, "../doc/long.fasta")`

### reverse_complement(seq)
- 받는 것: A, T, G, C로 된 서열 문자열 / 돌려주는 것: 상보 서열을 만든 뒤 순서를 뒤집은 역상보 서열
- 예: `rc = reverse_complement("ATGCGATACG")`

### length_stats(seqs)
- 받는 것: `read_fasta`가 돌려준 딕셔너리 / 돌려주는 것: 서열 개수(count), 전체 길이(total), 평균 길이(mean), 최소(min), 최대(max)를 담은 딕셔너리
- 예: `stats = length_stats(seqs)`

## 아직 부족한 점과 추가하고 싶은 함수

- `reverse_complement`는 A, T, G, C 이외의 글자(N 등)가 있으면 오류가 난다. N 같은 글자도 처리하도록 고치고 싶다.
- `read_fasta`는 제목 줄의 설명 부분(예: `chloroplast rbcL partial`)을 버린다. 설명도 함께 보관하는 방법이 필요하다.
- `write_fasta`는 서열을 한 줄로 길게 쓴다. 60글자 정도에서 줄을 바꿔 쓰는 기능을 추가하고 싶다.
- 추가하고 싶은 함수: 서열에서 N의 개수를 세는 함수, 서열을 단백질로 번역하는 함수.

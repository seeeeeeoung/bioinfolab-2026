#!/usr/bin/bash
# 식물 여덟 종의 rbcL 서열을 NCBI E-utilities로 받는 스크립트
# 종마다 esearch로 첫 번째 ID를 찾고, efetch로 FASTA(.fa)와 GenBank(.gb)를 받는다.
# 사용법: bash get_rbcL.sh
# 결과는 스크립트 위치 기준 ../data 폴더에 저장된다.

here=$(cd "$(dirname "$0")" && pwd)
outdir="$here/../data"
BASE="https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

if [ ! -d "$outdir" ]; then
    echo "오류: 저장할 폴더가 없습니다: $outdir"
    exit 1
fi

cd "$outdir"

while read genus species name; do
    # 검색어: 학명[Organism] AND rbcL[Gene] AND 1300:1500[SLEN]
    term="${genus}+${species}[Organism]+AND+rbcL[Gene]+AND+1300:1500[SLEN]"
    id=$(wget -q -O - "$BASE/esearch.fcgi?db=nuccore&retmax=1&term=$term" \
         | grep -o '<Id>[0-9]*</Id>' | head -1 | sed 's/<[^>]*>//g')
    sleep 1

    if [ -z "$id" ]; then
        echo "검색 결과 없음: $genus $species"
        continue
    fi

    echo "$genus $species → ID $id → $name.fa, $name.gb"
    wget -q -O "$name.fa" "$BASE/efetch.fcgi?db=nuccore&id=$id&rettype=fasta&retmode=text"
    sleep 1
    wget -q -O "$name.gb" "$BASE/efetch.fcgi?db=nuccore&id=$id&rettype=gb&retmode=text"
    sleep 1
done <<'EOF'
Arabidopsis thaliana rbcL_arabidopsis
Panax ginseng rbcL_ginseng
Oryza sativa rbcL_rice
Zea mays rbcL_maize
Ginkgo biloba rbcL_ginkgo
Pinus thunbergii rbcL_pine
Adiantum capillus-veneris rbcL_fern
Marchantia polymorpha rbcL_liverwort
EOF

echo "완료"

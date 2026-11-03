# rbcL 데이터 출처

| 파일 | VERSION | ORGANISM | 길이 | 확인 방법 | 문제 |
|---|---|---|---|---|---|
| rbcL_arabidopsis | OK432498.1 | Arabidopsis thaliana | 1440 | grep ORGANISM/VERSION/DEFINITION, fasta.py 길이 | DEFINITION이 UNVERIFIED, large subunit-like로 검증되지 않은 서열 |
| rbcL_ginseng | 없음 | - | - | esearch Count 직접 확인 (1300:1500 → 0, 1000:2000 → 0, 100000:200000 → 49) | 길이 조건에 맞는 레코드가 없어 받지 못함 |
| rbcL_rice | L24073.1 | Oryza sativa | 1355 | grep ORGANISM/VERSION/LOCUS, fasta.py 길이 | LOCUS가 mRNA. 에이전트가 LOCUS 이름(RICCHRBCLA)을 등록번호로 잘못 적음 |
| rbcL_maize | Z11973.1 | Zea mays | 1431 | grep ORGANISM/VERSION, fasta.py 길이 | 없음 |
| rbcL_ginkgo | KF221173.1 | Ginkgo biloba | 1317 | grep ORGANISM/VERSION, fasta.py 길이 | 없음 |
| rbcL_pine | JQ512595.1 | Pinus thunbergii | 1428 | grep ORGANISM/VERSION, fasta.py 길이 | 없음 |
| rbcL_fern | MW620303.1 | Adiantum capillus-veneris | 1308 | grep ORGANISM/VERSION, fasta.py 길이 | 없음 |
| rbcL_liverwort | LC536762.1 | Marchantia polymorpha subsp. ruderalis | 1399 | grep ORGANISM/VERSION, fasta.py 길이 | 요청한 종의 아종(subsp. ruderalis) |

- 모든 FASTA 파일은 grep -c ">" 결과 서열이 1개였다.
- 모든 길이는 fasta.py 결과와 GenBank LOCUS 길이가 같았고, 1,300~1,500 bp 사이였다.
- 받은 날짜: 2026-11-03, 도구: wget + NCBI E-utilities (esearch, efetch)

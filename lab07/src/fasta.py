"""FASTA 파일을 다루는 함수 모음"""

def read_fasta(filename):
    """FASTA 파일을 읽어 {이름: 서열} 딕셔너리로 돌려준다."""
    seqs = {}
    name = None
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            if line.startswith(">"):
                name = line[1:].split()[0]
                seqs[name] = ""
            else:
                seqs[name] = seqs[name] + line.upper()
    return seqs

def gc_content(seq):
    """서열의 GC 비율을 0과 1 사이의 수로 돌려준다."""
    if len(seq) == 0:
        return 0.0
    gc = seq.count("G") + seq.count("C")
    return gc / len(seq)

def write_fasta(seqs, filename):
    """{이름: 서열} 딕셔너리를 FASTA 파일로 저장한다."""
    with open(filename, "w") as out:
        for name in seqs:
            out.write(">" + name + "\n")
            out.write(seqs[name] + "\n")

def reverse_complement(seq):
    """서열의 역상보 서열을 돌려준다."""
    comp = {"A": "T", "T": "A", "G": "C", "C": "G"}
    result = ""
    for base in seq:
        result = result + comp[base]
    return result[::-1]

def length_stats(seqs):
    """{이름: 서열} 딕셔너리의 개수, 전체/평균/최소/최대 길이를 딕셔너리로 돌려준다."""
    lengths = []
    for name in seqs:
        lengths.append(len(seqs[name]))
    if len(lengths) == 0:
        return {"count": 0, "total": 0, "mean": 0.0, "min": 0, "max": 0}
    total = sum(lengths)
    return {
        "count": len(lengths),
        "total": total,
        "mean": total / len(lengths),
        "min": min(lengths),
        "max": max(lengths),
    }

if __name__ == "__main__":
    import sys
    seqs = read_fasta(sys.argv[1])
    for name in seqs:
        print(name, len(seqs[name]), round(gc_content(seqs[name]), 3))
    seq = "ATGCGATACG"
    print(reverse_complement(seq))
    print(reverse_complement(reverse_complement(seq)) == seq)
    print(length_stats(seqs))

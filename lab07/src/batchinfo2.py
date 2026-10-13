import sys
import glob
import os
from fasta import read_fasta, gc_content

folder = sys.argv[1]
outfile = sys.argv[2]

files = sorted(glob.glob(folder + "/*.fasta"))

with open(outfile, "w") as out:
    out.write("file\tcount\ttotal\tavg_gc\n")
    for path in files:
        seqs = read_fasta(path)
        total = 0
        gc_sum = 0.0
        for name in seqs:
            total = total + len(seqs[name])
            gc_sum = gc_sum + gc_content(seqs[name])
        if len(seqs) > 0:
            avg = round(gc_sum / len(seqs), 4)
        else:
            avg = 0.0
        out.write(os.path.basename(path) + "\t" + str(len(seqs)) + "\t" + str(total) + "\t" + str(avg) + "\n")

print(len(files), "개 파일을", outfile, "에 저장했습니다.")

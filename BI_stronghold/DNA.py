f = open("./data/rosalind_dna.txt", 'r')
sample = f.readlines()[0]
f.close()

base = ["A", "C", "G", "T"]

cnt_A = sample.count(base[0])
cnt_C = sample.count(base[1])
cnt_G = sample.count(base[2])
cnt_T = sample.count(base[3])

print(cnt_A, cnt_C, cnt_G, cnt_T)
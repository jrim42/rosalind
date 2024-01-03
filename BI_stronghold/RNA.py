f = open("./data/rosalind_rna.txt", 'r')
sample = f.readlines()[0]
f.close()

print(sample.replace("T", "U"))
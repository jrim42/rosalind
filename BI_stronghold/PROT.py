from codon import codon_table

f = open("./data/rosalind_prot.txt", 'r')
mRNA = f.readlines()[0]
f.close()

mRNA = mRNA.replace("U", "T")
length = len(mRNA)
AAstring = ""

for i in range(0, length, 3):
  triplet = mRNA[i:i+3]
  AA = codon_table[triplet]
  if AA == "*":
    break
  AAstring += AA

print(AAstring)  
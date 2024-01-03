f = open("./data/rosalind_revc.txt", 'r')
sample = f.readlines()[0]
f.close()

sample = sample[:-1]
rev = sample[::-1]

comp = ""

for i in rev:
  if i == "A":
    comp = comp + "T"
  elif i == "T":
    comp = comp + "A"
  elif i == "C":
    comp = comp + "G"
  else:
    comp = comp + "C"

print(comp)
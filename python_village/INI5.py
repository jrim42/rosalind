f = open("./data/rosalind_ini5.txt", 'r')
lines = f.readlines()
f.close()

line_no = 1
res = ""

for line in lines:
  if line_no % 2 == 1:
    res = res + line
  line_no = line_no + 1

print(res)
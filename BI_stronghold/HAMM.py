f = open("./data/rosalind_hamm.txt", 'r')
lines = f.readlines()
f.close()

s = lines[0]
t = lines[1]

pt_mt = 0

for i in range(0, len(s)):
  if s[i] != t[i]:
    pt_mt = pt_mt + 1

print(pt_mt)
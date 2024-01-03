f = open("./data/rosalind_subs.txt", 'r')
lines = f.readlines()
f.close()

s = lines[0][:-1]
t = lines[1][:-1]

s_len = len(s)
t_len = len(t)

location = []

for i in range(s_len):
  target = s[i:i + t_len]
  if t == target:
    location.append(i + 1)

for i in location:
  print(i, end=" ")
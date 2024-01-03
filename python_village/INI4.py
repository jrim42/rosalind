f = open("./data/rosalind_ini4.txt", 'r')
lines = f.readlines()[0]
f.close()

num = lines.split()
a = int(num[0])
b = int(num[1])
sum = 0

for i in range(a, b):
  if i % 2 == 1:
    sum = sum + i

print(sum)
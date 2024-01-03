f = open("./data/rosalind_ini2.txt", 'r')
lines = f.readlines()[0]
f.close()

num = lines.split()
a = int(num[0])
b = int(num[1])

res = pow(a, 2) + pow(b, 2)
print(res)
f = open("./data/rosalind_fib.txt", 'r')
lines = f.readlines()[0]
f.close()

num = lines.split()
n = int(num[0])
k = int(num[1])

d = [0] * (n + 1)

d[1] = 1
d[2] = 1

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2] * k

print(d[n])
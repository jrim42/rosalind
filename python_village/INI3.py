f = open("./data/rosalind_ini3.txt", 'r')
lines = f.readlines()
f.close()

s = lines[0]
idx_list = lines[1].split()
idx_list = [int(element) for element in idx_list]

res1 = s[idx_list[0]:idx_list[1] + 1]
res2 = s[idx_list[2]:idx_list[3] + 1]
print(res1, res2)
f = open("./data/rosalind_ini6.txt", 'r')
sample = f.readlines()[0]
f.close()

s_list = sample.split()
s_dict = dict.fromkeys(s_list, 0)

for i in s_dict:
  s_dict[i] = s_list.count(i)

for key, value in s_dict.items():
  print(key, value)
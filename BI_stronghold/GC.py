f = open("./data/rosalind_gc.txt", 'r')
lines = f.readlines()
f.close()

rosalind = {}
GC_content = {}
tmp_key = ""
tmp_val = ""

for line in lines:
  if line[0] == '>':
    if tmp_val != "":
      rosalind[tmp_key] = tmp_val
      tmp_val = ""
    tmp_key = line[10:14]
    GC_content[tmp_key] = 0
  else:
    tmp_val = tmp_val + line[:-1]

for key, value in rosalind.items():
  length = len(value)
  GC_cnt = rosalind[key].count("C") + rosalind[key].count("G")
  GC_ratio = round(GC_cnt / length * 100, 6)
  GC_content[key] = GC_ratio

max_key = max(GC_content, key=GC_content.get)
max_val = GC_content[max_key]

print("Rosalind_" + max_key)
print(max_val)
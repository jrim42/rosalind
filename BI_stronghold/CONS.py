#----------------------------------------------
def readFile():
  f = open("./data/rosalind_cons.txt", 'r')
  lines = f.readlines()
  f.close()
  return(lines)

#----------------------------------------------
def splitSeq(lines):
  rosalind = {}
  tmp_key = ""
  tmp_val = ""

  for line in lines:
    if line[0] == '>':
      if tmp_val != "":
        rosalind[tmp_key] = tmp_val
        tmp_val = ""
      tmp_key = line[10:14]
    else:
      tmp_val = tmp_val + line[:-1]

  if tmp_val != "":
      rosalind[tmp_key] = tmp_val
  seq_len = len(tmp_val)
  return (seq_len, rosalind)

#----------------------------------------------
def getConsensus(rosalind, nt_tbl):
  cons_tbl = []
  consensus = ""

  for i in range(0, seq_len):
    tmp_lst = [0, 0, 0, 0]
    for key, value in rosalind.items():
      nt = value[i]
      if nt == "A":
        tmp_lst[0] += 1
      elif nt == "C":
        tmp_lst[1] += 1
      elif nt == "G":
        tmp_lst[2] += 1
      else:
        tmp_lst[3] += 1
    max_idx = tmp_lst.index(max(tmp_lst))
    consensus += nt_tbl[max_idx]
    cons_tbl.append(tmp_lst)
  return(consensus, cons_tbl)

#----------------------------------------------
def displayTable(cons_tbl, nt_tbl):
  tbl_len = len(cons_tbl)
  for i in range(0, 4):
    print(nt_tbl[i], end=": ")
    for j in range(0, tbl_len):
      print(cons_tbl[j][i], end=" ")
    print()

#----------------------------------------------
nt_tbl = ["A", "C", "G", "T"]

lines = readFile()
[seq_len, rosalind] = splitSeq(lines)
[consensus, cons_tbl] = getConsensus(rosalind, nt_tbl)
print(consensus)
displayTable(cons_tbl, nt_tbl)


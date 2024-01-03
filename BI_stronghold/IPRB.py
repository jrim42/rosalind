# The probability that two randomly selected mating organisms will produce an individual 
#  possessing a dominant allele (and thus displaying the dominant phenotype).
#  Assume that any two organisms can mate.

f = open("./data/rosalind_iprb.txt", 'r')
lines = f.readlines()
f.close()

num = lines[0].split()
k = int(num[0])
m = int(num[1])
n = int(num[2])
pop = k + m + n

# case(1): first selected = homozygous dominant 
dom = (k / pop)

# case(2): first selected = heterozygous
het1dom2 = (m / pop) * (k / (pop - 1))
het1het2 = (m / pop) * ((m - 1) / (pop - 1)) * (3 / 4)
het1rec2 = (m / pop) * (n / (pop - 1)) * (1 / 2)
het = het1dom2 + het1het2 + het1rec2

# case(3): first selected = recessive
rec1dom2 = (n / pop) * (k / (pop - 1))
rec1het2 = (n / pop) * (m / (pop - 1)) * (1 / 2)
rec = rec1dom2 + rec1het2

res = round(dom + het + rec, 6)
print(res)


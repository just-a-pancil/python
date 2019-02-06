dna = input()
a = 0
dna_enc = ''
last_sim = dna[0]
for sim in dna:
	if sim == last_sim:
		last_sim = sim
		a+=1
	elif sim!=last_sim:
		dna_enc += last_sim + str(a)
		last_sim = sim
		a = 1
dna_enc += last_sim + str(a)
# aaaabbcaa
# print(len(dna))
print(dna_enc)


# much better solution:

# genome = input()+' '
# s = 0
# n=genome[0]
# for i in genome:       
#     if n!=i:
#         print(n + str(s), end = '')
#         s=0
#         n=i
#     s+=1
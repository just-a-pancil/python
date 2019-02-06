# dic = {'code': str(input()),
# 	   'encode': str(input())}
code_str0 = {k:v for (k,v) in zip(str(input()),str(input()))}
code_str1 = {v:k for (k,v) in code_str0.items()}
str0 = str(input())
str1 = str(input())
enc_str0 = ''
enc_str1 = ''

for x in str0:
	enc_str0 += code_str0[x]

for x in str1:
	enc_str1 += code_str1[x]

print(enc_str0)
print(enc_str1)
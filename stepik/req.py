import requests
main_addr = "https://stepic.org/media/attachments/course67/3.6.3/"
with open("C:/python/stepik/files/dataset_3378_3.txt") as f:
	link = f.readline().strip()
	print(link)
# print(type(r.text))

r = requests.get(link)
while r.text.split()[0]!= 'We':
	link = r.text
	r = requests.get(main_addr+link)
	print(link)
print(r.text)
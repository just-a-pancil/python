import pickle
f = open("pic-ed.txt", 'wb')
s = 'fuck'
# f1 = open("sample.py","rb")
# pickle.dumps(s,f)
pickle.dump(s,f)
f.close()
f3 = open("pic-ed.txt", "rb")
print(pickle.load(f3))
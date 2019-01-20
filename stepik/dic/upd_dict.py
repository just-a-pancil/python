# def update_dictionary(d, key, value): # thats mine peace of shit
# 	if key in d:
# 		d[key] += [value]
# 	elif key not in d:
# 		if key*2 in d:
# 			d[key*2] += [value]
# 		else: 
# 			d[key*2] = [value]


def update_dictionary(d, key, value): # and thats someonces code
    key += key * (key not in d)
    d[key] = d.get(key, []) + [value]

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
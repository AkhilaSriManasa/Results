
f = open("fi_ir.txt")
text = f.readlines()
# print(text)
mylist = []
s_dict = []
words = []
# print(len(text))
for i in text:
	# print(i)

	nspace = i.split(" ")
	list_dict = {}	
	for k in nspace:
		if(k):
			new = k.split("-")
			# print(new)
			if(len(new)==2):
				list_dict[new[1]]=new[0]
	
	s_dict = sorted(list_dict.items(), key=lambda x: x[1], reverse=True)
	# print((s_dict))
	if(len(s_dict)>6):
		je = 0
		for ke in range(0,4):
			je = ke
			
			if(s_dict[je][0] not in words):
				words.append(s_dict[je][0])
				mylist.append(s_dict[je])
			else:
				words.append(s_dict[je+1][0])
				mylist.append(s_dict[je+1])	

# 		print(str(len(mylist)))
# print(len(mylist))
# for v in mylist:
# 	words.append(v[0])
# if('"error"' not in words):
# 	words.append('"error"')
# if('"issue"' not in words):
# 	words.append('"issue"')	

print(words)


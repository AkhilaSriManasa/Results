from statistics import mean
from difflib import get_close_matches 
fe = open("ir_err.txt")
fp = open("ir_prj.txt")
ff = open("ir_file.txt")
fa = open("ir_api.txt")

# te = fe.readlines

te = fe.readlines()
tp = fp.readlines()
tf = ff.readlines()
ta = fa.readlines()
txt = []
txt.append(te[0])
txt.append(tp[0])
txt.append(tf[0])
txt.append(ta[0])

import csv
import pandas as pd
df = pd.read_csv("resultpython_ir.csv")
Data = df["Topics"]
# Program to measure similarity between  
# two sentences using cosine similarity. 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

with open('python_ir_label.csv', 'w', newline='',encoding="utf-8-sig", errors='ignore') as result_file:
	writer = csv.writer(result_file)
	writer.writerow(["Name"])

# X = input("Enter first string: ").lower() 
# Y = input("Enter second string: ").lower() 
	for d in range(len(Data)):
		# print(i.split('),'))
		testSet = []
		i = Data[d]

		t0 = i.split('),')[0]
		t1 = i.split('),')[1]
		t2 =i.split('),')[2]
		t3 = i.split('),')[3]
		# t4 = i.split('),')[4]
		testSet.append(t0)
		testSet.append(t1)
		testSet.append(t2)
		testSet.append(t3)
		# testSet.append(t4)
		fin = []

		for tests in range(len(testSet)):
			sim_cosine = []


			for label in range(len(txt)):
				X = txt[label]
				Y = testSet[tests]


				# tokenization 
				X_list = word_tokenize(X)  
				Y_list = word_tokenize(Y) 
				  
				# sw contains the list of stopwords 
				sw = stopwords.words('english')  
				l1 =[];l2 =[] 
				  
				# remove stop words from string 
				X_set = set(X_list)
				Y_set = set(Y_list)
				  
				# form a set containing keywords of both strings  
				rvector = X_set.union(Y_set)  
				for w in rvector: 
				    if w in X_set: l1.append(1) # create a vector 
				    else: l1.append(0) 
				    if w in Y_set: l2.append(1) 
				    else: l2.append(0) 
				c = 0
				  
				# cosine formula  
				for i in range(len(rvector)): 
				        c+= l1[i]*l2[i] 
				cosine = c / float((sum(l1)*sum(l2))**0.5) 
				sim_cosine.append(cosine)
			maxprob = max(sim_cosine)
			avg = mean(sim_cosine)
			diff = maxprob-avg
			print(diff)
			print(avg)
			if(maxprob-avg > -0.05):
				index = sim_cosine.index(max(sim_cosine))
				if(index==0):
					res = ("t"+str(tests)+" = error")
					fin.append(res)


				if(index==1):
					res = ("t"+str(tests)+" = project")
					fin.append(res)
				if(index==2):
					res = ("t"+str(tests)+" = File")
					fin.append(res)

				if(index==3):
					res = ("t"+str(tests)+" = API")
					fin.append(res)	
			else:
				res = ("t"+str(tests)+" = error")
				fin.append(res)
			# else if(index==3):
			# 	print("t0 = License")


		
			print(sim_cosine)
		writer.writerow([fin])		

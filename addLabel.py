import csv
import pandas as pd
df = pd.read_csv("resultpython_ir.csv")
df1 = pd.read_csv("python_ir_label.csv")
Labels = df1["Name"]
with open('Res_python_ir.csv', 'w', newline='',encoding="utf-8-sig", errors='ignore') as result_file:
	writer = csv.writer(result_file)
	writer.writerow(["Name","F","E","P","A"])

	for x in range(len(Labels)):
		vals = Labels[x].split(',')
		fc = []
		ec = []
		pc = []
		ac = []
		# lc = []
		for t in vals:
			tnum = t.split("=")[0]

			tname = t.split("=")[1]
			col_val = ((tnum[2:4]).upper())
			if("File" in tname):
				fc.append(df[col_val][x])
			if("error" in tname):
				ec.append(df[col_val][x])
			if("API" in tname):
				ac.append(df[col_val][x])
			if("project" in tname):
				pc.append(df[col_val][x])
			# if("License" in tname):
			# 	lc.append(df[col_val][x])
		writer.writerow([df['Name'][x],sum(fc),sum(ec),sum(pc),sum(ac)])		
	
		
import random
import csv

def openfile():#INI UNTUK MEMASUKKAN DATA CSV
	tampung= []
	with open('data_latih_opsi_2.csv', 'r') as csvFile:
		reader = csv.reader(csvFile)
		for row in reader:
			tampung.append(row)
			# print(row)
	# csvFile.close()
	return tampung

def rules(): #MEMBUAT RULE DENGAN ACAK*5
	rule=[]
	acak=random.randint(1,10)
	print "rule",acak
	for x in range(acak):
		rule.append(str(random.randint(0,2)))
		rule.append(str(random.randint(0,3)))
		rule.append(str(random.randint(0,3)))
		rule.append(str(random.randint(0,2)))
		rule.append(str(random.randint(0,1)))
	return rule

def populasi(): #MEMBUAT BANYAKNYA KROMOSOM DARI RULE
	tampungpop =[]
	acak = random.randint(1,4)
	print "populasi",acak
	for x in range(acak):
		tampungpop.append(rules())
	return tampungpop

def spliter(kromosom): #SPLIT KROMOSOM
	hasil=[]
	# for x in range(len(kromosom)):
	# 	hasil=kromosom[x]
	for i in range(0, len(kromosom),5):
   		yield kromosom[i:i+5]

def fitness(csv,split):
	add=0
	temp=[]
	tenan=0

	# for x in range(len(split)):
	# 	hasil=split[x]
	# 	for i in range(len(csv)):
	# 		hasil2=csv[i]
	# 		if hasil == hasil2:
	# 			add=add+1
	# 	temp.append(add)
	# 	add=0
	# print(split)

	# for x in range(len(split)):
	# 	hasil=split[x]
	# 	for i in range(len(csv)):
	# 		hasil2=csv[i]
	# 		if hasil == hasil2:
	# 			add=add+1
	# return add	

	for tiapRule in split:
		# print(tiapRule)
		for i in range(len(csv)):
			hasil2=csv[i]
			# print(hasil2)
			if tiapRule == hasil2:
				# print(tiapRule," == ",hasil2)
				add=add+1
	print add
	tenan=add+0
	return tenan*(1.25/100)
	# return add

# def splitRule(arrayK):
# 	temp=[]
# 	print "ssss"
# 	for i in range(0, len(arrayK),5):
#    		yield arrayK[i:i+5]		

# def therealspliter():
			


# ===MAIN PROGRAM===
hasilsplit=[]
dataLatih=[]
tampfit = []
x = populasi()
# print x
dataLatih = openfile()
for i in x:
	print(i)
for tiapKromosom in x:
	getSplit = list(spliter(tiapKromosom))
	z = fitness(dataLatih,getSplit)
	tampfit.append(z)
print(tampfit)	
# print getSplit

# print "1",dataLatih[0]
# print fitness(dataLatih,getSplit,x)
# for i in x:
# 	print(i)
# print "======"
# print "--------"

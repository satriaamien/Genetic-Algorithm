import random	
import csv

def openfile():#INI UNTUK MEMASUKKAN DATA CSV
	tampung= []
	with open('data_latih_opsi_1.csv', 'r') as csvFile:
		reader = csv.reader(csvFile)
		for row in reader:
			tampung.append(row)
	return tampung

def rule():
	rule=[]
	pilih=[0,1]
	pilih2=[15,30,45]
	# for x in range(15):
	# 	rule.append(random.choice(pilih))
	# return rule
	rule=[random.choice(pilih) for x in range(random.choice(pilih2))]
	return rule

def kromosom():
	kromosom=[]
	pilih=random.randint(2,3)
	# for x in range(pilih):
	# 	kromosom.append(rule())
	# return kromosom
	kromosom=[rule() for x in range(pilih)]
	return kromosom

def spliter(pop):
	for x in range(0,len(pop),15):
		yield pop[x:x+15]

# def encoding(csv):
# 	temp=[]
# 	datacsv=[]
# 	for x in range(len(csv)):
# 		if (x[0] == [0,1,0]):#suhu #normal
# 			temp.append("normal")
# 		elif (x[0]==[1,0,0]):#tinggi
# 			temp.append("tinggi")
# 		elif (x[0])==[0,0,1]:#rendah
# 			temp.append("rendah")

# 		if (x[1] == [1,0,0,0]):#waktu #wpagi
# 			temp.append("pagi")
# 		elif (x[1] == [0,1,0,0]):#siang
# 			temp.append("siang")
# 		elif (x[1] == [0,0,1,0]):#sore
# 			temp.append("sore")
# 		elif (x[1] == [0,0,0,1]):#malam
# 			temp.append("malam")
		
# 		if (x[2] == [1,0,0,0]):#langit #berawan
# 			temp.append("berawan")
# 		if (x[2] == [0,1,0,0]):#cerah
# 			temp.append("cerah")
# 		if (x[2] == [0,0,1,0]):#hujan
# 			temp.append("hujan")
# 		if (x[2] == [0,0,0,1]):#rintik
# 			temp.append("rintik")

# 		if (x[3] == [0,1,0]):#lembap #normal
# 			temp.append("normal")
# 		elif (x[3] == [1,0,0]):#tinggi
# 			temp.append("tinggi")
# 		elif(x[3] == [0,0,1]):#rendah
# 			temp.append("rendah")

# 		if (x[4] == [1]):#ya
# 			temp.append("ya")
# 		else:
# 			temp.append("tidak")

# 		datacsv.append(temp)
# 	return datacsv

def decode(suhu,waktu,langit,lembap,kondisi):
	temp=[]
	data=[]
	if (suhu == [1,1,1]):
		temp.append(["tinggi","normal","rendah"])
	elif (suhu == [1,1,0]):
		temp.append(["tinggi","normal"])
	elif (suhu == [0,1,1]):
		temp.append(["normal","rendah"])
	elif (suhu == [1,0,1]):
		temp.append(["tinggi","rendah"])
	elif (suhu == [1,0,0]):
		temp.append(["tinggi"])
	elif (suhu == [0,1,0]):
		temp.append(["normal"])
	elif (suhu == [0,0,1]):
		temp.append(["rendah"])
	elif (suhu == [0,0,0]):
		temp.append(["rendah"])


	if (waktu ==[1,1,1,1]):
		temp.append(["pagi","siang","sore","malam"])
	elif (waktu==[1,1,1,0]):
		temp.append(["pagi","siang","sore"])	
	elif (waktu==[1,1,0,1]):
		temp.append(["pagi","siang","malam"])
	elif (waktu==[1,0,1,1]):
		temp.append(["pagi","sore","malam"])
	elif (waktu==[0,1,1,1]):
		temp.append(["siang","sore","malam"])
	elif (waktu==[1,1,0,0]):
		temp.append(["pagi","siang"])
	elif (waktu==[0,0,1,1]):
		temp.append(["sore","malam"])
	elif (waktu==[1,0,0,1]):
		temp.append(["pagi","malam"])
	elif (waktu==[0,1,1,0]):
		temp.append(["siang","sore"])
	elif (waktu==[1,0,1,0]):
		temp.append(["pagi","sore"])
	elif (waktu==[0,1,0,1]):
		temp.append(["sore","malam"])
	elif (waktu==[1,0,0,0]):
		temp.append(["pagi"])
	elif (waktu==[0,1,0,0]):
		temp.append(["siang"])
	elif (waktu==[0,0,1,0]):
		temp.append(["sore"])
	elif (waktu==[0,0,0,1]):
		temp.append(["malam"])
	elif (waktu==[0,0,0,0]):
		temp.append(["malam"])


	if (langit ==[1,1,1,1]):
		temp.append(["berawan","cerah","hujan","rintik"])
	elif (langit==[1,1,1,0]):
		temp.append(["berawan","cerah","hujan"])	
	elif (langit==[1,1,0,1]):
		temp.append(["berawan","cerah","rintik"])
	elif (langit==[1,0,1,1]):
		temp.append(["berawan","hujan","rintik"])
	elif (langit==[0,1,1,1]):
		temp.append(["cerah","hujan","rintik"])
	elif (langit==[1,1,0,0]):
		temp.append(["berawan","cerah"])
	elif (langit==[0,0,1,1]):
		temp.append(["hujan","rintik"])
	elif (langit==[1,0,0,1]):
		temp.append(["berawan","rintik"])
	elif (langit==[0,1,1,0]):
		temp.append(["cerah","hujan"])
	elif (langit==[1,0,1,0]):
		temp.append(["berawan","hujan"])
	elif (langit==[0,1,0,1]):
		temp.append(["cerah","rintik"])
	elif (langit==[1,0,0,0]):
		temp.append(["berawan"])
	elif (langit==[0,1,0,0]):
		temp.append(["cerah"])
	elif (langit==[0,0,1,0]):
		temp.append(["hujan"])
	elif (langit==[0,0,0,1]):
		temp.append(["rintik"])
	elif (langit==[0,0,0,0]):
		temp.append(["rintik"])

	if (lembap==[1,1,1]):
		temp.append(["tinggi","normal","rendah"])
	elif (lembap == [1,1,0]):
		temp.append(["tinggi","normal"])
	elif (lembap == [0,1,1]):
		temp.append(["normal","rendah"])
	elif (lembap == [1,0,1]):
		temp.append(["tinggi","rendah"])
	elif (lembap == [1,0,0]):
		temp.append(["tinggi"])
	elif (lembap == [0,1,0]):
		temp.append(["normal"])
	elif (lembap == [0,0,1]):
		temp.append(["rendah"])
	elif (lembap == [0,0,1]):
		temp.append(["rendah"])
	elif(lembap == [0,0,0]):
		temp.append(["rendah"])

	if (kondisi== [1]):
		temp.append(["ya"])
	else:
		temp.append(["tidak"])
	
	# data.append(temp)
	return temp

# def csvmatching(csv):
# 	kolom=0
# 	for x in range(len(csv)):
# 		kolom=csv[x]

# def matchingdecode(splitcode):
	# for x in range(len(splitcode)):
	# 	if (splitcode[x] == )

# def coditionmatching():


def matching(bariscsv,getdecode):
# suhu,waktu,langit,lembap,kondisi=0,0,0,0,0
	print getdecode
	print "===================="
	for i in getdecode:
		print getdecode
	print "xxx", bariscsv[0]
	a,b,c,d,e,getfit=0,0,0,0,0,0
	for i in range(len(bariscsv)):
		column=bariscsv[i]#baris csv
		print "column -",i," ",bariscsv[i]
		for w in range(len(getdecode)):# perulangan setiap rule di kromosom
			decoderule=getdecode[w] #baris decode
			for x in range(len(column)):#perulangan di tiap kolom baris csv 
				getbaris=column #baris csv

				if (x==0):
					for y in range(len(decoderule[0])):
						tiapsuhu=decoderule[0][y]# data tiap suhu
						if (getbaris[0] == tiapsuhu): #dicocokkan jk benar nambah 1
							a=a+1
						else:
							a=a+0
				if (x==1):
					for y in range(len(decoderule[1])):
						tiapwaktu=decoderule[1][y]# data tiap waktu
						if (getbaris[1] == tiapwaktu): #dicocokkan jk benar nambah 1
							b=b+1
						else:
							b=b+0
				if (x==2):
					for y in range(len(decoderule[2])):
						tiaplangit=decoderule[2][y]# data tiap langit
						if (getbaris[2] == tiaplangit): #dicocokkan jk benar nambah 1
							c=c+1
						else:
							c=c+0
				if (x==3):
					for y in range(len(decoderule[3])):
						tiaplembap = decoderule[3][y]# data tiap lembap
						if (getbaris[3] == tiaplembap): #dicocokkan jk benar nambah 1
							d=d+1
						else:
							d=d+0					
				if (x==4):
					for y in range(len(decoderule[4])):
						tiapkondisi = decoderule[4][y]# data tiap kondisi
						if (getbaris[4] == tiapkondisi): #dicocokkan jk benar nambah 1
							e=e+1
						else:
							e=e+0
			if (a+b+c+d+e==5):
				get = True
				a,b,c,d,e=0,0,0,0,0
				break
			else:
				get = False
				a,b,c,d,e=0,0,0,0,0
		if (get == True):
			getfit = getfit + 1
		else:
			getfit = getfit + 0
	return getfit*(1.25/100)

def spliterrule(rule):
	getdecode=[]
	for x in range(len(rule)):
		print "x",x
		temp = rule[x]
		suhu = temp[:3]
		waktu = temp[3:7]
		langit= temp[7:11]
		lembap = temp[11:14]
		kondisi= temp[14]
		getdecode.append(decode(suhu,waktu,langit,lembap,kondisi))
	return getdecode

		# # bariscsv = csv[x]
		# matching(csv,getdecode)

		# print "ss",matching(csv,getdecode)
		# print matching(baris,getdecode)
	# 	if (suhu == [1,1,1] and (suhu ==[1,0,0] or suhu == [0,1,0] or suhu == [0,0,1])):
	# 		if suhu == []	
			
			

populasi=[]
tempe=[]
populasi = kromosom()
filecsv=openfile()
# print filecsv
# encode(filecsv)
# for x in openfile():
# 	print x
print populasi
print "==="
for pop in range(len(populasi)):
	getsplit = list(spliter(populasi[pop]))
	decodekromosom = spliterrule(getsplit)
	print matching(filecsv,decodekromosom)
 	tempe.append(matching(filecsv,decodekromosom))
print tempe
	# break
	# break
	# for i in getdecode:	
	# 	print "getdecode", getdecode
	# spliterrule(getsplit)





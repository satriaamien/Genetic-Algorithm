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
	pilih2=[30]
	rule=[random.choice(pilih) for x in range(random.choice(pilih2))]
	return rule

def kromosom():
	kromosom=[]
	pilih=random.randint(2,4)
	kromosom=[rule() for x in range(pilih)]
	return kromosom

def spliter(pop):
	for x in range(0,len(pop),15):
		yield pop[x:x+15]

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

def matching(bariscsv,getdecode):
	a,b,c,d,e,getfit=0,0,0,0,0,0
	for i in range(len(bariscsv)):
		column=bariscsv[i]#baris csv
		print ("column -",i," ",bariscsv[i])
		for w in range(len(getdecode)):# perulangan setiap rule di kromosom
			decoderule=getdecode[w] #baris decode
			for x in range(len(column)):#perulangan di tiap kolom baris csv 
				getbaris=column #baris csv

				if (x==0):
					for h in range(len(decoderule[0])):
						tiapsuhu=decoderule[0][h]# data tiap suhu
						if (getbaris[0] == tiapsuhu): #dicocokkan jk benar nambah 1
							a=a+1
						else:
							a=a+0
				if (x==1):
					for j in range(len(decoderule[1])):
						tiapwaktu=decoderule[1][j]# data tiap waktu
						if (getbaris[1] == tiapwaktu): #dicocokkan jk benar nambah 1
							b=b+1
						else:
							b=b+0
				if (x==2):
					for k in range(len(decoderule[2])):
						tiaplangit=decoderule[2][k]# data tiap langit
						if (getbaris[2] == tiaplangit): #dicocokkan jk benar nambah 1
							c=c+1
						else:
							c=c+0
				if (x==3):
					for l in range(len(decoderule[3])):
						tiaplembap = decoderule[3][l]# data tiap lembap
						if (getbaris[3] == tiaplembap): #dicocokkan jk benar nambah 1
							d=d+1
						else:
							d=d+0					
				if (x==4):
					for m in range(len(decoderule[4])):
						tiapkondisi = decoderule[4][m]# data tiap kondisi
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
	return getfit

def valuefitness(x):
	hasilfit = x*(1.25/100)
	return hasilfit

def spliterrule(rule):#decode rule 
	getdecode=[]
	for x in range(len(rule)):
		print("x",x)
		temp = rule[x]
		suhu = temp[:3]
		waktu = temp[3:7]
		langit= temp[7:11]
		lembap = temp[11:14]
		kondisi= temp[14]
		getdecode.append(decode(suhu,waktu,langit,lembap,kondisi))#panggil kondisi untuk rule
	return getdecode

def roulete(fit):
	tot=0
	p=0
	r=random.random()
	for x in range(len(fit)):
		tot += fit[x]
	i=0
	while (r>0):
		r = r-(fit[i]/(tot+0.000000000000001))
		i +=1
	return i-1

def crossover1(gettipot,p1,p2):
	temp=[]
	x=gettipot[0]
	y=gettipot[1]
	p1[x:y],p2[x:y]=p2[x:y],p1[x:y]
	return p1,p2

def tipot(p1,p2):
	tipotparent1=[]
	x =0
	y =0	
	while (x==y) or (x>=y):
		x = random.randint(0,(len(p1)//2)-1)
		y = random.randint(0,len(p2))
		if(x<=y and x!=y):
			tipotparent1= [x,y]
			break
	# print "x,y",x,y
	# print "0",tipotparent1[0]
	# print "1",tipotparent1[1]
	selisih=tipotparent1[1]-tipotparent1[0]
	# print "sel",selisih
	modulo= selisih % 15
	# print "modulo",modulo
	a=[tipotparent1[0],tipotparent1[0]+selisih]
	# print "a",a
	b=[tipotparent1[0],tipotparent1[0]+modulo]
	# print "b",b
	c=[tipotparent1[1]-selisih,tipotparent1[1]]
	# print "c",c
	d=[tipotparent1[1]-modulo,tipotparent1[1]]
	# print "d",d
	if ((a[0]<15 and a[1]>=15) and ((b[0]<15 and b[1]>=15))):
		# print"123"
		return crossover1(a,p1,p2)
	if (a[0]<15) and (a[1]>=15) and (b[0]<15 and b[1]<15):
		# print"23"
		ptg1kiri=a[0]
		ptg1kanan=a[1]
		temp1=[]
		temp2=[]
		temp1.extend(p1)
		temp2.extend(p2)
		print("p1 sebelum",temp1)
		print("p2 sebelum", temp2)
		# print"p2 sebelum",temp2
		print("ptg1kiri",ptg1kiri)
		print("ptg1kanan",ptg1kanan)
		temp1[ptg1kiri:ptg1kanan]=temp2[ptg1kiri:ptg1kanan]
		print("p1 sesudah",temp1)
		# print"p2 sesudah",temp2
		###########################
		arrp1=[]
		arrp2=[]
		arrp1.extend(p1)
		arrp2.extend(p2)
		ptg2kiri=b[0]
		ptg2kanan=b[1]	
		print("ptg2kiri",ptg2kiri)	
		print("ptg2kanan",ptg2kanan)
		q=arrp2[:ptg2kiri]
		print ("q",len(q))
		w=arrp1[ptg1kiri:ptg1kanan]
		print("ptg1kiri",ptg1kiri)
		print("ptg1kanan",ptg1kanan)
		print ("w",len(w))
		e=arrp2[ptg2kanan:]
		print ("e",len(e))
		total=q+w+e
		if (len(total) % 15 != 0):
			i=0
			while((i<=100) and (len(total) % 15 != 0)):
				print("total proses",total)
				if (len(total)%15==0):
					break
				else:
					ptg1kanan+=1
					q=temp2[:ptg2kanan]

					w=p1[ptg1kiri:ptg1kanan]
					e=temp2[ptg2kanan:]
					total=q+w+e
				i+=1

		return temp1,total
	else:
		return crossover1(a,p1,p2)


def mutation(parent):
	mut1=parent[0]
	mut2=parent[1]
	val1=random.randrange(0,30)
	val2=random.randrange(0,30)
	prb1=random.random()
	prb2=random.random()
	for x in range(len(mut1)):
		if (x==val1) and (prb1<=0.7):
			if (mut1[x]==0):
				
				mut1[x]=1
			else:
				mut1[x]=0
	for y in range(len(mut2)):
		if (y==val2) and (prb2<=0.7):
			if (mut2[y]==0):
				mut2[y]=1
			else:
				mut2[y]=0
	# print"mut1",mut1
	# print"mut2",mut2
	return [mut1,mut2]


populasi=[]
populasi = kromosom()
totalfitness=[]
nilaifitness=[]
filecsv=openfile()

print(populasi)
print("===")
for x in range(1):
	tmpgen=[]
	for totpop in range(1):
		for pop in range(len(populasi)):
			getsplit = list(spliter(populasi[pop]))
			decodekromosom = spliterrule(getsplit)
			totalfitness.append(matching(filecsv,decodekromosom))
		print ("fitness",totalfitness)
		p1=roulete(totalfitness)
		p2=roulete(totalfitness)
		print ("p1,p2",p1,p2)
		getcrossover = tipot(populasi[p1],populasi[p2])
		print ("ss",getcrossover[0])
		print ("ss",getcrossover[1])
		getmutation= mutation(getcrossover)
		print(getmutation)
		tmpgen.append(getmutation)
	populasi=tmpgen
print (totalfitness[0]*(1.25/100))
print("kromosom terbaik",populasi[0])



import numpy as np
import pandas as pd
import random
from copy import deepcopy

data = pd.read_csv('data_latih_opsi_2.csv',header=None,names=['Suhu','Waktu','Kondisi_Langit','Kelembapan','Terbang/Tidak']) ## Baca dataset
X,y = data.drop(['Terbang/Tidak'],axis=1),data['Terbang/Tidak'] ## Pisahin parameter dan label

params = {'Suhu':3,'Waktu':4,'Kondisi_Langit':4,'Kelembapan':3}

def initPopulasi(count):
    populasi = []
    for i in range(count):
        chromosome = np.random.randint(2, size=2*14) ## buat chromosome random dengan panjang 2 rule (2*14)
        populasi.append({'chro' : chromosome, 'ruleSize' : 14, 'params' : params})
    return populasi

def mutation(c,mr=0.01):
    for i in range(len(c['chro'])):
        p = np.random.uniform(0,1)
        if p<=mr:
            c['chro'][i] = 0 if c['chro'][i]==1 else 1
            c['chro'] = np.array(c['chro'])

def crossOver(parents):
    '''
    contoh input
        parents :
        [
            {'chro': array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 'ruleSize': 4},
            {'chro': array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'ruleSize': 4}
        ]
    '''
    # size adalah ukuran 1 rule
    size = 14
    
    # sort dari parent dengan ukuran terbanyak
    parent = sorted(deepcopy(parents), key = lambda x:len(x['chro']), reverse=True)
    
    if(type(parent[0]['chro']) is not list):
        parent[0]['chro'] = parent[0]['chro'].tolist()
    if(type(parent[1]['chro']) is not list):
        parent[1]['chro'] = parent[1]['chro'].tolist()
    
    # x1 = titik potong pertama pada parent 1
    # y1 = titik potong kedua pada parent 2
    # generate x1,y1
    x1 = random.randint(1,len(parent[0]['chro'])-2)
    y1 = random.randint(x1+1,len(parent[0]['chro'])-1)
    
    # membuat semua kemungkinan panjang titik potong di parent 2 sesuai dengan panjang titik potong pada parent 1
    possibility = []
    for it in range(len(parent[1]['chro'])//size):
        possibility.append(((y1-x1) % size) + size*it)
    # random pilihan mana yang terpilih
    choosen = random.randint(0,len(possibility)-1)
    
    # generate x2,y2
    x2 = random.randint(0, (len(parent[1]['chro'])-1) - possibility[choosen])
    y2 = x2+possibility[choosen]
    
    offspring = deepcopy(parent)
    
    # swap chromosome dengan metode increase/decrease
    temp = deepcopy(offspring[0]['chro'][x1:y1])
    offspring[0]['chro'][x1:y1] = deepcopy(offspring[1]['chro'][x2:y2])
    offspring[1]['chro'][x2:y2] = temp
    
    # ubah chromosome menjadi np array kembali
    offspring[0]['chro'] = np.array(offspring[0]['chro'])
    offspring[1]['chro'] = np.array(offspring[1]['chro'])
    
    for child in offspring:
        if (len(child['chro']) % 14) != 0:
            return deepcopy(parent) 
    
    return offspring

def predict(X,c):
    '''
    Input : X -> data yang ingin dipredict dalam bentuk dataframe
    Input : c -> Chromosome dari rule berbentuk dictionary yang mempunyai attribut: 
                    genotype -> e.g. [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0,
                                            0, 1, 0, 1, 1, 1]
                    
                    params   -> banyak kategori dalam setiap kolum dalam dataset tersebut e.g. 
                                {'Kelembapan': 3, 'KondisiLangit': 4, 'Suhu': 3, 'Waktu': 4}
                    
                    ruleSize -> panjang rule berdasarkan dataset e.g. 14
    
    Output : y -> hasil predict sebanyak data di X dalam bentuk 1/0
    '''
    geno = c['chro'].reshape((-1,c['ruleSize'])) ## Membagi genotype dari chromosome menjadi rule sepanjang ruleSize e.g. 28 -> 2 * 14 karena panjang rule yang diterima adlah 14
    decoded = decode(geno,c['params']) ## Mendapatkan rule untuk tiap attribut
    # print(geno)
    # print(decoded)
    # print(X.iterrows)
    preds = False ## Default nya kita akan predict false
    for rule in decoded: ## Untuk tiap rule
        preds_per_rule = np.array([])
        # print(preds_per_rule)
        for x in X.iterrows(): ## untuk tiap data
            temp = True ## 
            for attr in rule: ## untuk tiap attribut
                print(attr,rule[attr])
                print("x",x[1][attr])
                temp = temp & rule[attr][x[1][attr]] ## apakah attribut attr di data ke_x cocok dengan rule dari chromosome, 
                # print(temp & rule[attr][x[1][attr]])
                print(temp)
                                                    ## semua attribut harus cocok dengan rule agar satu row data dipredict True 
                                                    ## karena itu pakai '&' 
            preds_per_rule = np.append(preds_per_rule,temp) ## Simpan hasil predict dari tiap rule
        
        preds = np.logical_or(preds_per_rule,preds) ## Jika salah satu rule menyatakan bahwa suatu row data dapat terbang maka itulah yang kita predict karena itu kita pakai 
                                                 ## 'logical_or'
    
    return preds

def decode(geno,attr):
    '''
    input : geno -> genotype yang telah dibagi menjadi rule
    input : attr -> banyak kategori dalam setiap kolum dalam dataset tersebut e.g. 
                                {'Kelembapan': 3, 'KondisiLangit': 4, 'Suhu': 3, 'Waktu': 4} 
    output : Rule untuk tiap parameter e.g. {'Kelembapan': [1,0,1], 'KondisiLangit': [1,1,0,1], 'Suhu': [1,0,0], 'Waktu': [1,0,0,1]} 
    '''
    rule = [] ## buat list kosong untuk rule
    for i in range(geno.shape[0]): ## ulang untuk setiap rule dari kromosom
        idx = 0 ## index
        rule.append({}) ## tambahkan dict kosong ke rule
        for j in params: ## Untuk tiap parameter ['Suhu', 'Kelembapan', 'Kondisilangit', 'Waktu]
            rule[i][j] = geno[i][idx:idx+params[j]] ## rule parameter mulai dari gen setelah gen terakhir parameter sebelumnya+panjang parameter sekarang 
            idx += params[j] ## index + parameter rule sekarang
    return rule

def accuracy(y_true,y_pred):
    '''
    input : y_true -> Label sebenarnya dari data
    input : y_pred -> Label yang diprediksi dari chromosome kita
    
    output : Akurasi dari chromosome
    '''
    return np.sum(np.array(y_true)==np.array(y_pred))/len(y_true) ## banyak prediksi benar / benyak data 

def fitness(c,X,y):
    '''
    input : c -> chromosome
    input : X -> data yang ingin dipredik
    input : y -> label (Terbang/Tidak) dari X
    
    output : fitness dari chromosome
    '''
    y_preds = predict(X,c) ## Prediksi data X menggunakan chromosome c
    c['fit'] = accuracy(y_preds,y) ## Hitung akurasi berdasarkan berapa prediksi yang benar

def tournament_selection(pop,k=5):
    '''
    input : pop -> Populasi dari chromosome yang ingin diambil parent
    input : k -> jumlah peserta untuk tournament
    
    output : 2 chromosome yang dipilih menjadi parent
    '''
    peserta = random.choices(pop,k=k) ## Pilih random dari populasi sebanyak k
    peserta = sorted(peserta, key=lambda x: x['fit'], reverse=True) ## sort dari yang paling bagus ke jelek
    chosen = peserta[:2] ## pilih 2 peserta teratas
    return chosen

def GA_Tree(X, y, generation, count):
    '''
    input : X -> Data train yang ingin diprediksi
    input : y -> Label dari data train (X)
    input : generation -> banyak iterasi yang akan dilakukan
    input : count -> banyak chromosome yang dibuat setiap generasi 
    
    output : Chromosome dengan fit terbaik
    '''
    population = initPopulasi(count) ## Membuat populasi awal

    for j in range(count):
        fitness(population[j],X,y) ## Hitung fitness dari semua populasi awal
        
    population.sort(key=lambda x: x['fit'],reverse=True) ## Sort dari yang bagus sampai paling jelek

    for i in range(generation): ## Perulangan tiap generasi
        new_pop = [population[0]] ## Elitism -> simpan 1 chromosome terbaik
        for j in range(count//2): ## Perulangan mencari parents
            parents = tournament_selection(population.copy()) ## Menggunakan Seleksi Tournament untuk mendapatkan 2 orang tua
            childs = crossOver(parents) ## crossOver
            new_pop.extend(childs) ## extend anak ke list populasi baru
        
        for j in range(1,len(new_pop)): ## Perulangan untuk mutasi
            mutation(new_pop[j]) ## Mutasi semua chromosome baru
            fitness(new_pop[j],X,y) ## hitung fitness hasil mutasi

        population = new_pop ## simpan new populasi ke populasi sekarang

        population.sort(key=lambda x: x['fit'],reverse=True) ## sort lagi
    return population[0] ## return yang paling bagus


if __name__ == '__main__':
	# a =GA_Tree(X,y,20,20) 
    # print(X)
    # print(y)
    populasi = initPopulasi(5)
    for i in populasi:
        print(i)
	
    for j in range(5):
        fitness(populasi[j],X,y) ## Hitung fitness dari semua populasi awal
        break
        # print(fitness(popula[j],X,y))
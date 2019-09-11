# 1 Year Of investment

def calculate_years(principal, interest, tax, desired):
    bunga  = interest * principal
    bungabersih = bunga * (1-tax)
    calculation =  principal + ((interest * principal) * (1-tax))
    year = 1
    while  calculation < desired:
        calculation = calculation + ((interest * calculation) * (1-tax))
        year += 1
    print(year)
    

calculate_years(1500, 0.07,0.6,5000)

#2 Number in Expand Form
import math
def expandForm(num):
    satuan  = len(str(num))
    angka1 = num
    angka = []
    angka2 = num/10
    angka3 = 0
    angka4 = 0
    for i in range(satuan-1):
        angka.append((math.floor(((num-angka4)/(10**(i+1)))))*10)
        angka4 += math.floor((num/(10**(i+1))))*10
    for z in angka:
        angka3 += z
    print(*angka,sep='+',end="+")
    print(num-angka3)

expandForm(12)

#3 Build Tower

def towerbuilder(n_floors, block_size):
    w, h = block_size
    panjang  = (w**2)*n_floors
    bintang  = "* "
    spasi  = " "
    angka = []
    banyakspasi = []
    for a in range(n_floors):
        for b in range(h):
            angka.append(bintang*(w+((w**2)*a)))
    for a in range(n_floors):
        for b in range(h):
            banyakspasi.append(spasi*(panjang-((w**2)*a)))
    for c in range(len(angka)):
        print(banyakspasi[c]  + angka[c] )


towerbuilder(3,(2,3))
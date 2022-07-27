import ParametrySiatki as Par #Parametry Siatki Bragga
import temperature as temp
import numpy as np
import matplotlib.pyplot as plt
import cmath as cmath
import time

#Obecna data
date = time.strftime("%Y%m%d-%H%M%S")

#Parametry światłowodowej siatki Bragga
##########################################
Lambda=1547.5*1e-9  #początek długość fali
y=1550*1e-9 #koniec długość fal
krok=0.0005*1e-9 #krok zmiany długości fali
neff=1.447 #współczynnik załamania efektywny
period=530*1e-9 #okres siatki
L=0.005 #długość siatki
norm=0.0001 #normalizacja (do zmniejszenia sygnału)
refelctivity=[] #odbicie
fale=[] #fale w nm
##########################################
legend = []
#######################################
#Czas
time=1
step=1
time_end=2

time_array=[]
arrtemp=[]
#######################################
arr=[]



#for number in range(ile):
#    r1 = Par.Reflectivity(neff, period, Lambda, norm, L, a, b, c, T, y, krok)
#    uno, duo = r1.funkcja()
#    T=T+krokT
#    plt.plot(duo,uno)
#    legend.append(T)


#f=open("%s.txt" %date,"x")
#for element in jeden:
#    f.write(element)



while time<time_end:
    tx = temp.Temperature(0,5,295,time,0,0,)
    txx=tx.temp()
    arrtemp.append(txx)
    time_array.append(time)
    rx= Par.Reflectivity(1.447,533*1e-9,Lambda,norm,3*1e-3,0,9*1e-12,3*1e-9,txx,y,krok)
    uno, dos = rx.funkcja()
    plt.plot(dos,uno)
    dos.insert(0,time)
    uno.insert(0,txx)
    arr.append(dos)
    arr.append(uno)
    time = time + step
#print(arrtemp)
#print(time_array)


#arr2=np.array([arrtemp,time_array])
#f = open("%s.txt" %date,"x")
#columns = ["Temp","Time"]
#f.write(str(columns)+"\n")
#for column in arr2.T:
#    f.write(str(column)+"\n")
#f.close()
arr = list(zip(*arr))

f = open("%s.txt" %date,"x")
for column in arr:
    f.write(str(column)+"\n")
f.close()

plt.xlabel("Wavelength [nm]")
plt.ylabel("Reflectivity[a.u.]")
plt.legend(legend)
plt.show()



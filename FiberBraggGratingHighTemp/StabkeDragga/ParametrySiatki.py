#Prosta Symulacja refelktancji Siatki Bragga
import numpy as np
import cmath as cmath

class Reflectivity:
    def __init__(self,neff,period,Lambda,norm,L,a,b,c,T,y,krok):
        self.neff=neff
        self.period=period
        self.Lambda=Lambda
        self.norm=norm
        self.L=L
        self.a=a
        self.b=b
        self.c=c
        self.T=T
        self.y=y
        self.krok=krok

    def reflectivity1(self):
        lambda_d=2*self.neff*self.period+(self.a**2*self.T+self.b*self.T+self.c)
        delta= 2*np.pi * self.neff * ((1 / self.Lambda) - (1 / lambda_d))
        sigma = 2 * np.pi * self.norm / self.Lambda
        kappa = np.pi * self.norm / self.Lambda
        r_inside = cmath.sqrt(kappa ** 2 - (delta + sigma) ** 2) * self.L
        r1 = cmath.sinh(r_inside) ** 2
        r2 = cmath.cosh(r_inside) ** 2 - ((delta + sigma) ** 2 / kappa ** 2)
        r = r1 / r2
        return r.real

    def funkcja(self):
        ref=[]
        fale=[]
        while (self.Lambda<self.y):
            ref.append(self.reflectivity1())
            fale.append(self.Lambda)
            self.Lambda=self.Lambda+self.krok
        return ref,fale

class Reflectivity2:
    def __init__(self,neff,period,Lambda,norm,L,T,y,krok):
        self.neff=neff
        self.period=period
        self.Lambda=Lambda
        self.norm=norm
        self.L=L
        self.T=T
        self.y=y
        self.krok=krok
    def reflectivity(self):
        lambda_d=2*self.neff*self.period+(self.T)
        delta= 2*np.pi * self.neff * ((1 / self.Lambda) - (1 / lambda_d))
        sigma = 2 * np.pi * self.norm / self.Lambda
        kappa = np.pi * self.norm / self.Lambda
        r_inside = cmath.sqrt(kappa ** 2 - (delta + sigma) ** 2) * self.L
        r1 = cmath.sinh(r_inside) ** 2
        r2 = cmath.cosh(r_inside) ** 2 - ((delta + sigma) ** 2 / kappa ** 2)
        r = r1 / r2
        return r.real
    def funkcja(self):
        ref = []
        fale = []
        while (self.Lambda < self.y):
            ref.append(self.reflectivity())
            fale.append(self.Lambda)
            self.Lambda = self.Lambda + self.krok
        return ref, fale



#def Lambda_d(neff,period,a,b,c,T):
#    lambda_d=2*neff*period+(a**2*T+b*T+c)
#    return lambda_d

#def Delta(neff,period,Lambda,a,b,c,T):
#    delta=2*np.pi*neff*((1/Lambda)-(1/Lambda_d(neff,period,a,b,c,T)))
#    return delta

#def Sigma(Lambda,normalisation):
#    sigma=2*np.pi*normalisation/Lambda
#    return sigma

#def Kappa(Lambda,normalisation):
#    kappa = np.pi * normalisation/Lambda
#    return kappa

"""
def reflectivity(neff,period,Lambda,norm,L,a,b,c,T):
    lambda_d = 2 * neff * period + (a ** 2 * T + b * T + c)
    delta = 2 * np.pi * neff * ((1 / Lambda) - (1 / lambda_d))
    sigma = 2 * np.pi * norm / Lambda
    kappa = np.pi * norm / Lambda
    r_inside=cmath.sqrt(kappa**2-(delta+sigma)**2)*L
    r1=cmath.sinh(r_inside)**2
    r2=cmath.cosh(r_inside)**2-((delta+sigma)**2/kappa**2)
    r=r1/r2
    return r.real

def funkcja(neff,period,Lambda,norm,L,a,b,c,T,y,krok):
    ref=[]
    fale=[]
    while (Lambda<y):
        ref.append(reflectivity(neff,period,Lambda,norm,L,a,b,c,T))
        fale.append(Lambda)
        Lambda=Lambda+krok
    return ref,fale
"""
"""
#for number in range(ile):
#    uno,duo = Par.funkcja(neff,period,x,norm,L,a,b,c,T,y,krok)
#    T=T+krokT
#    plt.plot(duo,uno)
#    legend.append(T)
"""
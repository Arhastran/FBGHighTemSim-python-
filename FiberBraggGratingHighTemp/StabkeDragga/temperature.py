import numpy as np
import cmath as cmath

class Temperature:
    def __init__(self,a,b,c,t,n,step):
        self.a=a
        self.b=b
        self.c=c
        self.t=t
        self.n=n #optional
        self.step = step #optional

    def temp(self):
        temperature = self.a*self.a*self.t+self.b*self.t+self.c
        return temperature

    def timerepeat(self):
        temp=[]
        time=[]
        t=self.t
        for i in range(self.n):
            temp.append(self.a*t*t+self.b*t+self.c)
            time.append(t)
            t=t+self.step
        return temp,time




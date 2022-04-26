import math as m
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl 
from scipy.linalg import solve
from matplotlib import style 
t0=-1.0
tn=1.0
h=0.4
t=round((t0+t0+h)/2.0,10)
tcopy=t0
alpha=[]
res=[]
matr=[]
vect=[]
coef=0.0
sv=0.0
n=4
for j in range(0,n):
        for k in range(1,n+1):
            while m.fabs(t0-tn)>=0.0000000000001:
                coef=(-m.cos(k*m.acos(t))/2.0+m.exp(t)*m.sin(k*m.acos(t)))*m.cos(j*m.acos(t))+coef
                sv=(-m.log(m.fabs((t-1)/(t+1)))+2*t+t*t*m.log(m.fabs((t-1)/(t+1)))-m.exp(t)*(t*t-1))*m.cos(j*m.acos(t))+sv  
                t0=round(t0+h,10)
                t=round((t0+t0+h)/2.0,10)
            t0=tcopy
            t=round((t0+t0+h)/2.0,10)
            res.append(round(coef,2))
            if k==n:
                vect.append(round(sv*(-1),2))
            sv=0.0
            coef=0.0
        matr.append(res)
        res=[]

print(matr)
print(vect)
matrnp=np.array(matr)
vectnp=np.array(vect).reshape((len(vect),1))
X1=[]
Y1=[]
X2=[]
Y2=[]
pp=-1.0
npp=solve(matrnp,vectnp)
print(npp)
while pp<=1:
   X1.append(pp)
   Y1.append(pp*pp-1)
   #print('x('+str(round(pp,3))+')= ' +str(round(pp*pp-1,3)))
   pp+=0.0001
rs=0.0
pp=-1.0
while pp<=1.0:
   for i in range(1,n+1):
        rs+=npp[i-1][0]*m.sin(i*m.acos(pp))
   X2.append(pp)
   Y2.append(rs)
   #print('x_n('+str(round(pp,3))+')= ' +str(round(rs,3)))
   rs=0.0
   pp+=0.00001
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.plot(X1,Y1,color='b',label='$x^{*}(t)$')
ax.plot(X2,Y2,color='r', label='$x^{*}_{n}(t)$')
ax.legend(ncol=1,loc=1,fontsize=15)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.grid(color='grey',which='both', linestyle=':',linewidth=0.5)
ax.text(5,0,'X',fontsize=10)
ax.text(0,5,'Y',fontsize=10)
ax.xaxis.set_major_locator(mpl.ticker.MaxNLocator(11))
ax.xaxis.set_minor_locator(mpl.ticker.MaxNLocator(22))
ax.yaxis.set_major_locator(mpl.ticker.MaxNLocator(11))
ax.yaxis.set_minor_locator(mpl.ticker.MaxNLocator(22))
plt.show()
import numpy as np
from scipy.fttpack import ftt, ifft
N=64 #number of points
T=1/64.0 #spacing btwn points(period)
x=np.linspace(0, 2*np.pi*N*T, N)
y1=np.cos(20*x)
y2=np.sin(10*x)
y3=np.sin(5*x)
y=y1+y2+y3 #produces random signal
fy=fft(y) #finds the fft
xf=np.linspace(0.0, 1.0/(2.0*T), N/2)
plt.plot(xf, (2.0/N)*np.abs(fy[:N/2]))
#only half is valid the other is a duplicate
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-5,5,300)
def f(a,b,c,x):
   f=a*pow(x,4)+np.cos(x/c)*pow(x,3)+b*x**2+c
   return f
y=f(2,3,4,x)
dydx=np.gradient(y,x)
fig,ax=plt.subplots()
ax.set_ylim(-5,20)
ax.set_xlim(min(x),max(x))
ax.set_title('functions')
ax.set_xlabel('x')
ax.set_ylabel('y(x),dy/dx')
plt.axhline(0,color='red',linestyle='--')
plt.axvline(0,color='red',linestyle='--')
plt.plot(x,y,color='blue',label='y(x)')
plt.plot(x,dydx,color='orange',label='dy/dx')

plt.grid()
plt.legend()
plt.show()



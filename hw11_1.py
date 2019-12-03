#
#  hw4_2.py
#
#
#  Created by Jim Drachenberg on 12/3/19.
#

from scipy.integrate import odeint
from pylab import * # for plotting commands
#---------------------------------------------------------
# Define the deriv function, which sets the system of ODEs
def deriv(r,t,m,k,K): # return derivatives
    x,px,y,py = r
    drdt = [px/m,-k*x, py/m,K]
    return drdt

# End deriv definition
#---------------------------------------------------------

#---------------------------------------------------------
# forced oscillator with quadratic drag
m = 2       # mass
k = 1.0     # x-constant
K = 1.0     # y-constant
x0 = 1.0    # initial position for x
px0 = 0.0   # initial momentum for x
y0 = 0.0    # initial position for y
py0 = 2.0   # initial momentum for y

r0 = [x0,px0,y0,py0]
t = np.linspace(0, 100, 1000)
sol = odeint(deriv,r0,t,args=(m,k,K))   # solve the ODE

figure()
plot(sol[:,0],sol[:,2],'b')
xlabel('x (m)')
ylabel('y (m)')

X,PX=np.meshgrid(np.arange(0-4,4,0.5),np.arange(-4,4,0.5))
Y,PY=np.meshgrid(np.arange(0-4,4,0.5),np.arange(-4,4,0.5))
grad=deriv([X,PX,Y,PY],0,m,k,K)
plt.figure()
#plt.quiver(X,PX,grad[0],grad[1])
plt.streamplot(X,PX,grad[0],grad[1],density=1.5)
plt.xlabel('x (m)')
plt.ylabel('$p_{x}$ (kg$\cdot$m/s)')
plt.figure()
plt.quiver(Y,PY,grad[2],grad[3])
plt.xlabel('y (m)')
plt.ylabel('$p_{y}$ (kg$\cdot$m/s)')

show()

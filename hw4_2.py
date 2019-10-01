#
#  hw4_2.py
#
#
#  Created by Jim Drachenberg on 9/30/19.
#

from scipy.integrate import odeint
from pylab import * # for plotting commands

#---------------------------------------------------------
# Define the deriv function, which sets the system of ODEs
def deriv(r,t,c,k,f,w): # return derivatives of the array phi
    y, v = r
    drdt = [v, -1*c*v*np.sqrt(v*v) - k*y + f*np.sin(w*t)]
    return drdt

# End deriv definition
#---------------------------------------------------------


#Solving the ode set:

#---------------------------------------------------------
# forced oscillator with quadratic drag
c = 4.0     # coefficient for v^2
k = 12.0    # coefficient for y
f = 80.0    # driving force coefficient
w = 2.0     # driving frequency
y0 = 0.0    # initial position
v0 = 0.0    # initial velocity

r0 = [y0, v0]
t = np.linspace(0, 4*2*np.pi/w, 1000)
sol = odeint(deriv,r0,t,args=(c,k,f,w))   # solve the ODE

figure()
plot(t,sol[:,0],'b',t,sol[:,1],'g')
xlabel('t (s)')
ylabel('y (m) & v (m/s)')
show()

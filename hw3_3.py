#
#  hw3_3.py
#
#
#  Created by Jim Drachenberg on 9/24/19.
#

from scipy.integrate import odeint
from pylab import * # for plotting commands

#---------------------------------------------------------
# Define the deriv function, which sets the system of ODEs
def deriv(phi,t,g,l): # return derivatives of the array phi
    phipos, phivelo = phi
    dphidt = [phivelo, -1*(g/l)*np.sin(phipos)]
    return dphidt

# End deriv definition
#---------------------------------------------------------


#Solving the ode set:

#---------------------------------------------------------
# simple pendulum
g = 9.8     # acceleration due to gravity in m/s
l = 1.0     # string length in m
m = 1.0     # bob mass in kg
iphi = 2  # initial angle from equilibrium
iphidot = 0.0   # initial angular velocity
period = 2*(np.pi)*(np.sqrt(l/g))

phi0 = [iphi, iphidot]
t = np.linspace(0, period, 1000)
sol = odeint(deriv,phi0,t,args=(g,l))   # solve the ODE

kinetic = 0.5*m*l*l*sol[:,1]*sol[:,1]   # calculate KE
potential = m*g*l*(1-np.cos(sol[:,0]))  # calculate PE
energy = kinetic + potential            # calculate total E

figure()
plot(t,sol[:,0],'b',t,sol[:,1],'g')
xlabel('t (s)')
figure()
plot(sol[:,0],sol[:,1],'b')
xlabel('$\phi$ (rad)')
ylabel('$d\phi/dt$ (rad/s)')
figure()
plot(t,kinetic,'b',t,potential,'g',t,energy,'r')
xlabel('t (s)')
ylabel('E (J)')
show()

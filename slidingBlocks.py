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
def deriv(r,t,g,m1,m2): # return derivatives of the array phi
    rpos, rdot, theta, thetadot = r
    drdt = [rdot, (m2/(m1+m2))*(rpos*thetadot*thetadot+g*np.cos(theta)), thetadot, -1*(g/rpos)*np.sin(theta)-2*rdot*thetadot/rpos]
    return drdt

# End deriv definition
#---------------------------------------------------------


#Solving the ode set:

#---------------------------------------------------------
# simple pendulum
g = 9.8     # acceleration due to gravity in m/s^2
m1 = 5.0    # mass 1 in kg (the larger this is, the slower the blocks slide and the more oscillations we get)
m2 = 1.0    # mass 2 in kg (opposite effect of m1)
rpos0 = 0.1 # initial r (need to keep it nonzero, otherwise the blocks won't ever start sliding...and Python gets upset!)
rdot0 = 0.0 # initial r velocity (zero is releasing "from rest")
theta0 = 0.1    # initial r
thetadot0 = 0.0 # initial r velocity (zero is releasing "from rest")

r0 = [rpos0, rdot0, theta0, thetadot0]
t = np.linspace(0, 2, 1000)             # remember that we left out drag, so the block falls a long way in a short time!
sol = odeint(deriv,r0,t,args=(g,m1,m2)) # solve the ODE

x = sol[:,0]*np.sin(sol[:,2])       # calculate x position from r and theta
y = -1*sol[:,0]*np.cos(sol[:,2])    # calculate y position from r and theta

figure()
plot(t,sol[:,0],'b',t,sol[:,2],'g') # plots r vs. t in blue and theta vs. t in green
xlabel('t (s)')
ylabel('r (m) & $\\theta$ (rad)')
figure()
plot(t,x,'b',t,y,'g')               # plots x vs. t in blue and y vs. t in green
xlabel('t (s)')
ylabel('x (m) & y (m)')
figure()
plot(x,y,'b')                       # plots y vs. x in blue
xlabel('x (m)')
ylabel('y (m)')
show()

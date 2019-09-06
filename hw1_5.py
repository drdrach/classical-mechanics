#
#  HW1.py
#
#
#  Created by Jim Drachenberg on 9/5/19.
#

from scipy.integrate import odeint
from pylab import * # for plotting commands

#---------------------------------------------------------
# Define the deriv function, which sets the system of ODEs
def deriv(r,t,s,p,d,m,g): # return derivatives of the array r
    xpos, xvelo, ypos, yvelo = r
    drdt = [xvelo, -1*(s*p*d*d/m)*xvelo*np.sqrt(xvelo*xvelo+yvelo*yvelo), yvelo, -g - (s*p*d*d/m)*yvelo*np.sqrt(xvelo*xvelo+yvelo*yvelo)]
    return drdt

# End deriv definition
#---------------------------------------------------------


#Solving the ode set:

#---------------------------------------------------------
# Yordan Alvarez's mashed baseball with quadratic drag
s = 0.157   # shape factor?
p = 1.19    # density of air in kg/m^3
d = 0.08    # diameter of baseball in m
m = 0.150   # mass of the baseball in kg
g = 9.8     # acceleration due to gravity in m/s
theta = 24.0*np.pi/180.0    # launch angle in radians
ispeed = 50.16              # exit speed in m/s

r0 = [0.0, ispeed*np.cos(theta), 0.0, ispeed*np.sin(theta)]
t = np.linspace(0, 5, 1000)
sol = odeint(deriv,r0,t,args=(s,p,d,m,g))
figure()
plot(sol[:,0],sol[:,2],'b')
xlabel('x (m)')
ylabel('y (m)')
show()

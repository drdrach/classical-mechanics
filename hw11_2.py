#
#  hw11_2.py
#
#
#  Created by Jim Drachenberg on 12/3/19.
#

from scipy.integrate import odeint
from pylab import * # for plotting commands
#---------------------------------------------------------
# Define the deriv function, which sets the system of ODEs
def deriv(r,t,m,L,g): # return derivatives of the array
    theta,ptheta,phi,pphi = r
    drdt = [ptheta/(m*L*L),pphi*pphi*np.cos(theta)/(m*L*L*np.sin(theta)*np.sin(theta)*np.sin(theta))+m*g*L*np.sin(theta), pphi/(m*L*L*np.sin(theta)*np.sin(theta)),0]
    return drdt

# End deriv definition
#---------------------------------------------------------

#---------------------------------------------------------
# forced oscillator with quadratic drag
m = 1       # mass
L = 1.0     # length
g = 1.0     # grav. accel.
pphi0 = 0.2 # p_phi

THETA,PTHETA=np.meshgrid(np.arange(0.1,np.pi,0.05),np.arange(-2,2,0.05))
grad=deriv([THETA,PTHETA,0,pphi0],0,m,L,g)
plt.figure()
plt.streamplot(THETA,PTHETA,grad[0],grad[1], density = 2)
plt.xlabel('$\\theta$')
plt.ylabel('$p_{\\theta}$')
show()

#
#  LotkaVolterra.py
#
#
#  Created by Jim Drachenberg on 11/28/19. Happy Thanksgiving!
#

from scipy.integrate import odeint
from pylab import * # for plotting commands

#---------------------------------------------------------
# Define the deriv function, which sets the system of ODEs

# Predator-prey model by Lotka-Volterra
def deriv(r,t,a,b,c,d): # return derivatives
    rabbit, fox = r
    drdt = [a*rabbit-b*rabbit*fox, -1*c*fox+d*rabbit*fox]
    return drdt

# End deriv definition
#---------------------------------------------------------


#Solving the ode set:

#---------------------------------------------------------
# predator-prey model
a = 1.0
b = 1.0
c = 2.0
d = 1.0
R0 = 2.0
F0 = 0.5
r0 = [R0, F0]
t = np.linspace(0, 12, 1000)
sol = odeint(deriv,r0,t,args=(a,b,c,d))

figure()
plot(t,sol[:,0],'b',t,sol[:,1],'r')
xlabel('t')
ylabel('Rabbits,Foxes')
figure()
plot(sol[:,0],sol[:,1],'b')
xlabel('Rabbits')
ylabel('Foxes')

X,Y=np.meshgrid(np.arange(0,3,0.1),np.arange(0,3,0.1))
testgrad=deriv([X,Y],0,a,b,c,d)
plt.figure()
# use "quiver" if you want a vector field; gives the "size" of the gradient
#plt.quiver(X,Y,testgrad[0],testgrad[1])
# use "streamplot" if you just want the direction of the "flow"; sometimes easier to "see" the solution if the magnitude changes rapidly
plt.streamplot(X,Y,testgrad[0],testgrad[1],density=1.5)

show()



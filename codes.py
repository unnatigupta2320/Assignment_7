import numpy as np
import matplotlib.pyplot as plt

O = np.array(([0,0]))

#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def ellipse_gen(a,b):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_ellipse = np.zeros((2,len))
	x_ellipse[0,:] = a*np.cos(theta)
	x_ellipse[1,:] = b*np.sin(theta)
	x_ellipse = (x_ellipse.T + O).T
	return x_ellipse

#Standard Ellipse
a = 6.40
b = 4
c=5
x = ellipse_gen(a,b)

#Vertices
A1 = np.array([a,0])
A2 = -A1
B1 = np.array([0,b])
B2 = -B1

#Plotting the ellipse
plt.plot(x[0,:],x[1,:],'r' ,label='ellipse')

#Labelling points
plt.plot(-5,0, 'o')
plt.text(-5.4 ,-0.4,'F1',weight='bold')
plt.plot(5,0, 'o')
plt.text(4.8 ,-0.4,'F2',weight='bold')
plt.plot(0,0, 'o')
plt.text(-0.7 ,-0.3,'O',weight='bold')

#Labelling points
plt.plot(6.40,0,'o',color='g')
plt.text(6.0 ,0,'A')
plt.plot(0,4, 'o',color='g')
plt.text(0,3.5,'B')

#Plotting line OF1
O=np.array([0,0])
F1=np.array([c,0])
OF1 = line_gen(O,F1)
plt.plot(OF1[0,:],OF1[1,:],'b')

#Plotting line OF2
O=np.array([0,0])
F2=np.array([-c,0])
OF2 = line_gen(O,F2)
plt.plot(OF2[0,:],OF2[1,:],'b')



plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()

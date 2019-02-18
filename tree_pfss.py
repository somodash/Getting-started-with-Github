import numpy as n
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.ion()

a1 = n.linspace(-n.pi/2,n.pi/2,180)
b1 = n.linspace(0,2.0*n.pi,360)
xx,yy = n.meshgrid(b1,a1)

fact1 = 0.15-0.02
fact2 = 0.22-0.02
fact3 = 0.30-0.02
fact4 = 0.37-0.02
fact5 = 0.05

cent = n.pi
ycent1 = 1.0-0.1
ycent2 = 0.7-0.1
ycent3 = 0.3-0.1
ycent4 = -0.2-0.1
ycent5 = 1.2

s1 = (xx-cent)*n.exp(-(xx-cent)*(xx-cent)/(fact1*fact1)-(yy-ycent1)*(yy-ycent1)/(fact1*fact1))/fact1
s2 = (xx-cent)*n.exp(-(xx-cent)*(xx-cent)/(fact2*fact2)-(yy-ycent2)*(yy-ycent2)/(fact2*fact2))/fact2
s3 = (xx-cent)*n.exp(-(xx-cent)*(xx-cent)/(fact3*fact3)-(yy-ycent3)*(yy-ycent3)/(fact3*fact3))/fact3
s4 = (xx-cent)*n.exp(-(xx-cent)*(xx-cent)/(fact4*fact4)-(yy-ycent4)*(yy-ycent4)/(fact4*fact4))/fact4
s5 = (xx-cent)*n.exp(-(xx-cent)*(xx-cent)/(fact5*fact5)-(yy-ycent5)*(yy-ycent5)/(fact5*fact5))/fact5
s6 = (xx-cent)*n.exp(-(xx-cent)*(xx-cent)/(fact5*fact5)-(yy-ycent5)*(yy-ycent5)/(fact5*fact5))/fact5
s7 = n.exp(-(xx-cent)*(xx-cent)/(fact5*fact5)-(yy-ycent5)*(yy-ycent5)/((fact5)*(fact5)))/fact5

profile1 =  200.0*(s1-s2+s3-s4+s6) +20.0*n.sin(yy) #+200.0*(s1-s2+s3-s4+s6)+5*n.sin(yy) 

plt.pcolormesh(b1,a1,profile1,cmap=plt.cm.jet)
#plt.pcolormesh(b1,a1,0.5*n.sin(yy),cmap=plt.cm.jet)
plt.colorbar(extend='both')
plt.axis('image')
#plt.show()



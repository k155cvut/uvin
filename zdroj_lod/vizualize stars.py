from numpy import *
import matplotlib.pyplot as plt
import matplotlib.image as im

#Set axis
plt.axis('equal')

#Load image
img = im.imread('e:/Tomas/Java/detectprojv2j/test/Povazan/JPEG/D1A_00019_00053/D1A_00019_00053_hem1.jpg')
imgplot = plt.imshow(img)

#Load points
points = loadtxt('E:/Tomas/Python/CelestialMaps/rozdily_1687_Boo.txts', usecols=range(8))
x_old = points[:,6]
y_old = points[:,7]
x_cat = points[:,3]
y_cat = points[:,4]

#Plot points
plt.plot(x_cat, y_cat, 'r*')
plt.plot(x_old, y_old, 'b.')

#Draw lines connecting points
for i in range(len(x_old)):
    plt.plot([x_old[i], x_cat[i]], [y_old[i], y_cat[i]], 'k', linestyle="-")

#Compute differences
dx = x_old - x_cat
dy = y_old - y_cat

#Draw vectors connecting points
plt.quiver(x_cat, y_cat, dx, dy, scale = 1, scale_units='xy', angles = 'xy', width = 0.002)

#Show the plot
plt.show()



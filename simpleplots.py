import numpy
import matplotlib.pyplot as plt
x = numpy.linspace(0,3,20)
y = numpy.linspace(0,9,20)
plt.plot(x,y)
plt.plot(x,y,'o')
plt.grid()
plt.figure()
image = numpy.random.rand(30,30)
plt.imshow(image)
plt.gray()
plt.figure()
plt.pcolor(image)
plt.hot()
plt.colorbar()
plt.show()

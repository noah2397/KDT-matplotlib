import numpy
import matplotlib.pyplot as plt

T = numpy.linspace(0, 2 * numpy.pi, 1024)

# 타원을 실제 종횡비로 그린다
plt.plot(2. * numpy.cos(T), numpy.sin(T), c='k', lw=3.)

#plt.gca().set_aspect('equal') # plt.axes().set_aspect('equal')

plt.show()

import numpy
import matplotlib.pyplot as plot

N = 8
A = numpy.random.random(N)
B = numpy.random.random(N)

plot.bar(range(N), A, color = 'w', hatch = 'x', edgecolor="k")
bars=plot.bar(range(N), A + B, bottom = A, color = 'None', hatch = '/',
            edgecolor="k")


plot.show()



import random
import matplotlib.pyplot as plot
import matplotlib.tri as tri


count = 100
X = [random.random() for i in range(count)]
Y = [random.random() for i in range(count)]
Z = [0.] * count

triangles = tri.Triangulation(X, Y)

# triplot이 아니니 tripcolor 사용
plot.tripcolor(triangles, Z, edgecolors='w')
plot.show()

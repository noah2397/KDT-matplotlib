import random
import matplotlib.pyplot as plot
import matplotlib.tri as tri


count = 100
X = [random.random() for i in range(count)]
Y = [random.random() for i in range(count)]

triangles = tri.Triangulation(X, Y) # Trianglation을 거친뒤에

plot.triplot(triangles, 'bo-') # triplot으로 그릴 수 있다
plot.show()

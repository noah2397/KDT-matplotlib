import matplotlib.pyplot as plot
import numpy as np
data = [5, 25, 50, 20]

plot.pie(data)
plot.show()



X=np.random.randn(1000) #정규 분포의 1000개 값을 그림
plot.hist(X, bins=20)
plot.show()
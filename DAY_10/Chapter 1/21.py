import random
import matplotlib.pyplot as plot

data = [random.gauss(0., 1.) for i in range(100)]
# random.gauss(평균, 표준편차) -> 정규분포 데이터를 생성

plot.boxplot(data)

plot.show()

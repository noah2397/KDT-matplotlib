import numpy
import matplotlib.pyplot as plot

data = numpy.array([[5., 30., 45., 22.],
                    [5., 25., 50., 20.],
                    [1.,  2.,  1.,  1.]])

color_list = ['b', 'g', 'r']

# X=[0,1,2,3] 만들기
X = numpy.arange(data.shape[1])

print(X)
for i in range(data.shape[0]):
    #S : data의 i번째 행까지 "열" 방향으로 더함
    # 0,0,0,0
    # 5,30,45,22
    # 10,55,95,42
    S = numpy.sum(data[:i], axis = 0)
    print(S)
    plot.bar(X, data[i], bottom = S, color = color_list[i % len(color_list)])

plot.show()

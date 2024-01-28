import matplotlib.pyplot as plot

data = [5., 25., 50., 20.]

plot.bar(range(len(data)), data, width = 1.) # 막대 그래프의 너비 설정
plot.show()

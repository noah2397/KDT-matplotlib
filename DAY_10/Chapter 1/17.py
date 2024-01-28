import matplotlib.pyplot as plot

A = [5., 30., 45., 22.]
B = [5., 25., 50., 20.]

X = range(4)
plot.bar(X, A, color = 'b')
plot.bar(X, B, color = 'r', bottom = A)# 치역 값을 bottom 매개변수에 지정
plot.show()


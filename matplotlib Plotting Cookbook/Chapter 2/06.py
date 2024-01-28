import random
import matplotlib.pyplot as plot

values = [random.randint(0, 99) for i in range(50)]
values.sort()
color_set = ['.00', '.25', '.50', '.75']

# 4*(0~99)까지의 값을 100으로 나눔 ->  0~396까지의 값을 100나누어 0,1,2,3으로 변환
color_list = [color_set[(len(color_set) * val) // 100] for val in values]

plot.bar(range(len(values)), values, color = color_list)
plot.show()

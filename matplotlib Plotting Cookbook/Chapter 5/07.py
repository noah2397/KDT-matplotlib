import random
import matplotlib.pyplot as plot

name_list = ('Omar', 'Serguey', 'Max', 'Zhou', 'Abidin')
value_list = [random.randint(0, 99) for name in name_list]
pos_list = range(len(name_list))

plot.bar(pos_list, value_list, alpha = .5, color = '.25', align = 'center')

plot.xticks(pos_list, name_list) # xtick로 값마다 눈금을 만듦

# bar.png를 투명한 이미지로 저장
plot.savefig('bar.png', transparent = True)

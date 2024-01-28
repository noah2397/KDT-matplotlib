import matplotlib.pyplot as plot

data = [[5., 25., 50., 20.],
        [4., 23., 51., 17.],
        [6., 22., 52., 19.]]
# gap은 조금 다르지만 일일히 숫자를 부여하지 않고 gap으로 통일함
gap = .8 / len(data) # 0.8/3=0.266666
print(gap, len(data))
for i, row in enumerate(data):
        # x를 comprehension 시키면서 row 길이만큼 정의역 생성
	plot.bar([x + i * gap for x in range(len(row))], row, width = gap)
plot.show()


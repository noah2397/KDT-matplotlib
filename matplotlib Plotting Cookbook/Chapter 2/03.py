import numpy
import matplotlib.pyplot as plot

label_list = ( # iris.data.txt 에 있는 붓꽃의 종류를 갖고옴
	b'Iris-setosa',
	b'Iris-versicolor',
	b'Iris-virginica',
)

def read_label(label):
	return label_list.index(label)

data = numpy.loadtxt('iris.data.txt',
                     delimiter = ',',
					 # converters : 4번째 인덱스 요소(파일에 있는 붓꽃 이름)
					 # 을 읽어와 read_label함수를 적용시키겠다는 뜻
					 # read_label 함수는 label_list의 인덱스를 반환하기에
					 # Iris-setosa에 해당하는 행들은
					 # 5.1,3.5,1.4,0.2,Iris-setosa
					 # -> [5.1 3.5 1.4 0.2 0. ]로 변환된다
					 # (Iris-setosa가 0으로 바뀜)
                     converters = { 4 : read_label })


color_set = ('.00', '.50', '.25')
# 전체 행의 4번째에 해당하는 열로 판단하여 점의 투명도를 계산함
color_list = [color_set[int(label)] for label in data[:,4]]

# 전체 행의 첫번째와 두번째 열을 출력, color 인자로 리스트 할당 가능
plot.scatter(data[:,0], data[:,1], color = color_list)
plot.show()


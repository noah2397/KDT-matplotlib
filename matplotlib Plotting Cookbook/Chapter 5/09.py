import numpy
from matplotlib import pyplot as plot
from matplotlib.backends.backend_pdf import PdfPages

# 데이터 생성
data = numpy.random.randn(15, 1024)

# PDF 문서 생성
pdf_pages = PdfPages('histograms.pdf')

# 페이지 생성
nb_plots = data.shape[0] # 15
nb_plots_per_page = 5 # 5
nb_pages = int(numpy.ceil(nb_plots / float(nb_plots_per_page)))
grid_size = (nb_plots_per_page, 1) # 5:1 로 페이지를 설정한다

for i, samples in enumerate(data):
    # 새로운 페이지를 생성
    if i % nb_plots_per_page == 0:
        fig = plot.figure(figsize=(8.27, 11.69), dpi=100)  # A4 용지 크기 (210mm x 297mm)

    # 히스토그램 그리기
    plot.subplot2grid(grid_size, (i % nb_plots_per_page, 0)) # 5 X 1 공간에 그리기
    plot.hist(samples, 32, density=1, facecolor='#808080', alpha=0.75)

    # 마지막 플롯이거나 페이지의 마지막 플롯인 경우 페이지 닫기
    if (i + 1) % nb_plots_per_page == 0 or (i + 1) == nb_plots:
        plot.tight_layout()
        pdf_pages.savefig(fig)

# PDF 문서를 디스크에 저장
pdf_pages.close()

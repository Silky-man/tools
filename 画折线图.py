# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
names = ['2', '4', '8', '16', '32']
x = range(len(names))
y = [51.17, 52.11, 53.04,53.33, 52.47]
#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#pl.xlim(-1, 11)  # 限定横轴的范围
#pl.ylim(-1, 110)  # 限定纵轴的范围
plt.plot(x, y, marker='o')
#plt.plot(x, y1, marker='*', ms=10,label=u'y=x^3曲线图')
#plt.legend()  # 让图例生效
plt.xticks(x, names)
plt.ylim(51,54,0.5)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.tick_params(labelsize=14)
plt.xlabel(u"r",fontdict={ 'family': 'Times New Roman','size': 14}) #X轴标签
plt.ylabel("Accuary/%",fontdict={'family': 'Times New Roman', 'size': 14}) #Y轴标签
#plt.title("A simple plot") #标题
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
# 解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

def main():
    path = "smooth_run-test-tag-accuracy.csv"
    ydata = []
    xdata = []
    # 使用python下pandas库读取csv文件
    data = pd.read_csv(path, encoding='gbk')
    # print(data)

    ydata = data.ix[:, 'Step']
    xdata = data.ix[:, 'Value']
    # # 读取列名为距离误差的前1000行数据
    # # ydata = data.ix[:1000,'距离误差']
    # plt.figure(1)
    # # 点线图
    # # plt.plot(xdata,ydata,'bo-',label=u'cte_误差',linewidth=1)
    # # 点图
    # plt.scatter(xdata, ydata, s=1)
    # plt.title(u"CTE误差", size=10)
    # plt.legend()
    # plt.xlabel(u'时间点(点数)', size=10)
    # plt.ylabel(u'cte误差（米）', size=10)
    # # 在展示图片前可以将画出的曲线保存到自己路径下的文件夹中
    # plt.savefig('C:\\Users\\yangyukuan\\Desktop\\data_nyj\\12.11\\cte误差.jpg')
    # plt.show()
    # print("all picture is starting")


if __name__ == "__main__":
    main()

from scipy import *
import pylab as pl  # pylab 模块是一款由python提供的可以绘制二维，三维数据的工具模块，其中包括了绘图软件包 matplotlib


def cost(c, all_points):
    return sum(sum((c - all_points) ** 2, axis=1) ** 0.5)


def gradient(c, all_points):
    dx = sum((c[0] - all_points[:, 0]) / sum((c - all_points) ** 2, axis=1) ** 0.5)  # 求x偏导数
    dy = sum((c[1] - all_points[:, 1]) / sum((c - all_points) ** 2, axis=1) ** 0.5)  # 求y偏导数
    s = (dx ** 2 + dy ** 2) ** 0.5
    dx = dx / s
    dy = dy / s
    return array([dx, dy])  # 得到梯度向量


all_points = rand(20, 2)


x = array([0, 1])  # 出发点
theta = 0.03  # 学习率
loop_max = 1000  # 最大迭代次数(防止死循环)
epsilon = 1e-6  # 设置阈值
xb = x

for i in range(loop_max):
    cost1 = cost(x, all_points)  # 梯度更新前的损失函数值
    xi = x - theta * gradient(x, all_points)  # 梯度更新后的新的点
    costi = cost(xi, all_points)  # 更新后的损失函数值
    if cost1 - costi > epsilon:  # 更新前损失函数值减去更新后的差大于阈值，继续循环
        x = xi
        cost1 = costi
    elif costi - cost1 > epsilon:  # 更新后损失函数值减去更新前的差大于阈值，说明步长过大，需要调小
        theta = theta * 0.3
    else:
        break
    xb = vstack((xb, x))

print (costi)

c = x

pl.plot(all_points[:, 0], all_points[:, 1], 'g.')
pl.plot(xb[:, 0], xb[:, 1], 'r.')
pl.plot(xb[:, 0], xb[:, 1], 'k-')
pl.xlabel('c = (%.3f, %.3f)' % (c[0], c[1]))

pl.show()

print(c)
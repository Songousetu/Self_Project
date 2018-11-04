from scipy import *
import pylab as pl


def cost(c, all_points):
    return sum(sum((c - all_points) ** 2) ** 0.5)


all_points = rand(20, 2)


def stochasticgradient(c, r):
    dx = (c[0] - r[0]) / sum((c - r) ** 2) ** 0.5  # 求x偏导数
    dy = (c[1] - r[1]) / sum((c - r) ** 2) ** 0.5  # 求y偏导数
    s = (dx ** 2 + dy ** 2) ** 0.5
    dx = dx / s
    dy = dy / s
    return array([dx, dy])  # 得到梯度向量


x = array([0, 1])  # 出发点

theta = 0.08  # 学习率
xb = x
loop_max = 10000  # 最大迭代次数(防止死循环)
epsilon = 1e-8

for i in range(loop_max):
    from random import choice

    r = choice(all_points)
    cost1 = cost(x, all_points)
    xi = x - theta * stochasticgradient(x, r)
    costi = cost(xi, all_points)
    if cost1 - costi > epsilon:
        x = xi
        cost1 = costi
    elif costi - cost1 > epsilon:
        theta = theta * 0.5
    else:
        break
    xb = vstack((xb, x))

c = x

pl.plot(all_points[:, 0], all_points[:, 1], 'g.')
pl.plot(xb[:, 0], xb[:, 1], 'r.')
pl.plot(xb[:, 0], xb[:, 1], 'k-')
pl.xlabel('c = (%.3f, %.3f)' % (c[0], c[1]))

pl.show()

print(c)
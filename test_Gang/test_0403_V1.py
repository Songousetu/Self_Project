from scipy import *
import pylab


def f(p, pts):
    return sum(sum((p - pts) ** 2, axis=1) ** 0.5)


def fd(p, pts):
    dx = sum((p[0] - pts[:, 0]) / sum((p - pts) ** 2, axis=1) ** 0.5)
    dy = sum((p[1] - pts[:, 1]) / sum((p - pts) ** 2, axis=1) ** 0.5)
    s = (dx ** 2 + dy ** 2) ** 0.5
    dx /= s
    dy /= s
    return array([dx, dy])


pts = rand(10, 2)
x = array([0, 0])

t = 0.1
xstep = x
for k in range(100):
    y = f(x, pts)
    xk = x - t * fd(x, pts)
    yk = f(xk, pts)
    if y - yk > 1e-8:
        x = xk
        y = yk
    elif yk - y > 1e-8:
        t *= 0.5
    else:
        break
    xstep = vstack((xstep, x))
print(x, y)

pylab.plot(pts[:, 0], pts[:, 1], 'bo')
pylab.plot(xstep[:, 0], xstep[:, 1], 'ro')
pylab.plot(xstep[:, 0], xstep[:, 1], 'k-')
pylab.xlabel('iter = %d, Min = %.3f, p = (%.3f, %.3f), t = %f' % (k, y, x[0], x[1], t))
pylab.show()
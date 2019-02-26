import math
from matplotlib import pylab as plt
import numpy as np
import scipy.optimize as opt


def f(x, ctx=math):
    '''Given function f(x). 
    Variable ctx is used to unify usage of any module:
    math or smth else - it is enough to change module.name in function definition'''
    #x = float(x)
    return ctx.sin(x/5) * ctx.exp(x/10) + 5*(ctx.exp(-x/2))

if __name__ == "__main___":
	xs = np.arange(1.0, 30., 0.01)
	ys = [f(x) for x in xs]
	print plt.plot(xs,ys)

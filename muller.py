from __future__ import division
from numpy import *
#from matplotlib.pylab import plot, show


def muller(f, p0, p1, p2, tol, max_iter=100):
    h1 = p1 - p0
    h2 = p2 - p1
    f_p1 = f(p1)
    f_p2 = f(p2)
    d1 = ( f_p1 - f(p0) ) / h1
    d2 = ( f_p2 - f_p1 ) / h2
    d = (d2-d1) / (h2+h1)
    i = 3
    while i <= max_iter:
        b = d2 + h2*d
        # sqrt function knows to use complex numbers
        # if we make sure the argument is complex
        # (by adding 0j in case argument starts as real)
        # D is the discriminant
        D = sqrt(b*b - 4 * f_p2 *d + 0j)
        if abs(b-D) < abs(b+D):
            # ensure we don't subtract similar values
            E = b+D
        else:
            E = b-D
        h = -2 * f_p2 / E
        p = p2 + h
        print "i=%i: D= %f, p= %.6f + %.6fj" % (i, D, p.real, p.imag)
        if abs(h) < tol:
            return p
        p0 = p1
        p1 = p2
        p2 = p
        h1 = p1 - p0
        h2 = p2 - p1
        f_p1 = f(p1)
        f_p2 = f(p2)
        d1 = ( f_p1 - f(p0) ) / h1
        d2 = ( f_p2 - f_p1 ) / h2
        d = (d2-d1) / (h2+h1)
        i += 1
    print "Reached maximum number of iterations"
    return p

## TESTING
# Example 3 p. 94

def f(x):
    return 16*x**4 - 40*x**3 + 5*x**2 + 20*x +6

p = muller(f, 0.5, -0.5, 0, 1e-5)

def print_row(lst):
    print ' '.join('%11.5f' % x for x in lst)
 
def romberg(f, a, b, eps = 1E-5):
    R = [[0.5 * (b - a) * (f(a) + f(b))]]  # R[0][0]
    print_row(R[0])
    n = 1
    while True:
        h = float(b-a)/2**n
        R.append((n+1)*[None])  # Add an empty row.
        R[n][0] = 0.5*R[n-1][0] + h*sum(f(a+(2*k-1)*h) for k in range(1, 2**(n-1)+1)) # for proper limits
        for m in range(1, n+1):
            R[n][m] = R[n][m-1] + (R[n][m-1] - R[n-1][m-1]) / (4**m - 1)
        print_row(R[n])
        if abs(R[n][n-1] - R[n][n]) < eps:
            return R[n][n]
        n += 1
from math import *
print romberg(lambda x: (9*x**4-344*x**3+4072*x**2-14752*x+25040)/5120
	, 0, 20)

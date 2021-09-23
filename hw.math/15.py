from math import *
x=5
y = (fabs(x*log1p(x-4))*sqrt(x))*(1/(pow(exp(4*x-1), 1/5)))
print(y)
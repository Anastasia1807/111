from math import *
x=5
y = log1p(sqrt(fabs(2-x))+1.2)*(1/(2+exp(-x)))+pow(2/x , 1/3)
print(y)
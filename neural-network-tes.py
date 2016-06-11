from __future__ import division
import numpy as np
import csv

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
# input dataset
price_tmp = []
for time, price in csv.reader(open("data1.csv")):
    
    price_tmp.append(float(price))

Data = []
for i in range(len(price_tmp)):
    tmp = []
    for j in range(3):
        if i+j< len(price_tmp):
            tmp.append(price_tmp[i+j])
    Data.append( tmp )
X = np.array( Data )

# output dataset
trace = []
for i in range(len(price_tmp)):
    if not (i==0):
        trace.append(int((price_tmp[i]-price_tmp[i-1])> 0))
Y = np.array([trace]).T

print X,Y

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((10,1)) - 1

for iter in xrange(10000):

    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

    # how much did we miss?
    l1_error = y - l1

    # multiply how much we missed by the 
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)

    # update weights
    syn0 += np.dot(l0.T,l1_delta)

print "Output After Training:"
print l1

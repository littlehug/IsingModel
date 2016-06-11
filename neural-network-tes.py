from __future__ import division
import numpy as np
import csv

# sigmoid function
def nonlin(x,deriv=False):
    if deriv == True:
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
# input dataset
price_tmp = []
for time, price in csv.reader(open("data1.csv")):
    price_tmp.append(float(price))

#print "price_tmp", price_tmp
Data = []
for i in range(len(price_tmp)):
    tmp = []
    if i < len(price_tmp)-3:
        for j in range(3):
            if i+j< len(price_tmp):
                tmp.append(price_tmp[i+j])
        Data.append( tmp )
#print "data", Data
X = np.array( Data )

# output dataset
trace = []
for i in range(len(price_tmp)):
    if i > 2:
        trace.append(float(price_tmp[i]))
        #trace.append(float((price_tmp[i]-price_tmp[i-1]) > 0))
Y = np.array([trace]).T

print X
print Y

print len(X)
print len(Y)

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1

for j in xrange(6000000):

    # Feed forward through layers 0, 1, and 2
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))

    # how much did we miss the target value?
    l2_error = Y - l2
    
    if (j% 10000) == 0:
        print "Error:" + str(np.mean(np.abs(l2_error)))
        #print l1
        #print l2
        
    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error*nonlin(l2,deriv=True)

    # how much did each l1 value contribute to the l2 error (according to the weights)?
    l1_error = l2_delta.dot(syn1.T)
    
    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * nonlin(l1,deriv=True)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)
print l2

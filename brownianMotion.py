'''
T: horizon
mu: drift terms (moving average or long-term mean for stock returns)
sigma: volatility per year
S0: initial stock price
dt: step length in years
N_sim: number of simulations
'''

from numpy.random import standard_normal
from numpy import array, zeros, sqrt, shape
from pylab import *


T =1 
mu = 0.025
sigma = 0.1
S0 = 20
dt =0.01
N_Sim = 100

Steps=round(T/dt); # Steps in years (which means divide the trend into several parts)
S = zeros([N_Sim, Steps], dtype=float) # Store the price for each step
x = range(0, int(Steps), 1)

for j in range(0, N_Sim, 1):
        S[j,0] = S0 # All stocks price start at S0(= 20)
        for i in x[:-1]:
                S[j,i+1]=S[j,i]+S[j,i]*(mu-0.5*pow(sigma,2))*dt+sigma*S[j,i]*sqrt(dt)*standard_normal();
                print j, S[j,i+1]
        plot(x, S[j])

title('Simulations %d Steps %d Sigma %.6f Mu %.6f S0 %.6f' % (int(N_Sim), int(Steps), sigma, mu, S0))
xlabel('steps')
ylabel('stock price')
show()

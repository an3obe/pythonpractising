import numpy as np
from math import log
from math import exp
from math import sqrt

def Poisson_distribution (lambdaDouble):
    j1 = np.random.uniform(0,1)                                 # Generate random number between 0 and 1
    k = 0
    L = exp(-lambdaDouble)
    j3 = 0
    while True:
        j2 = L * pow(lambdaDouble, k)
        p = 1
        i6 = 0
        for i6 in range(k+1):
            if i6 == 0: p = 1
            else: p*= i6
        
        j2 /= p
        j3 += j2
        k += 1
        if j1 < j3: break
    
    return k-1

def Normal_distribution (mean, stdev):
    #TO MODEL BASED ON CUMULATIVE DENSITY FUNCTION OF NORMAL DISTRIBUTION BASED ON BOOK OF SHELDON ROSS, Simulation, The polar method, p80.
    
    while True:
        v1 = float(np.random.uniform(0,1000))*2
        v1 /= 10000
        v1 -= 1
        v2 = float(np.random.uniform(0,1000))*2
        v2 /= 10000
        v2 -= 1
        t = v1 * v1 + v2 * v2
        if not(t >= 1 or t == 0): break
    
    multiplier = sqrt(-2*log(t)/t)
    return int(v1 * multiplier * stdev + mean)
    
def Bernouilli_distribution (prob):
    j1 = np.random.uniform(0,1)                                 # Generate random number between 0 and 1
    if j1 < prob: return 0
    else: return 1    

def Uniform_distribution (a, b):
    j1 = np.random.uniform(0,1)                                 # Generate random number between 0 and 1
    return a + (b - a) * j1

def Triangular_distribution(a, b, c): # !!! a, b and c should be INTEGER
    # mean = (a+b+c)/3
    # stdev = sqrt((pow(a,2)+pow(b,2)+pow(c,2)-a*b-a*c-b*c)/18)
    j1 = np.random.uniform(0,1)                                 # Generate random number between 0 and 1
    x = a
    while True:
        if x <= b: L = pow((x-a),2)/((c-a)*(b-a))
        else: L = 1-(pow(c-x,2)/((c-a)*(c-b)))
        x += 1
        if j1 < L: break
    return x-1 

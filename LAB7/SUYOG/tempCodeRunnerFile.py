import numpy as np 

def dct(signal):
    N=len(signal)
    dct_coef =np.zeros(N)
    for k in range (N):
        sum=0
    for n in range (N):
        sum+=signal[n]*np.cos(np.pi*k*(2*n+1)/(2*N))
    dct_coef[k] = sum * np.sqrt(2/N)

    if k==0:
        dct_coef[k]*=sum*np.sqrt[1/2]
    
    return dct_coef
    
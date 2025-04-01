import numpy as np 

def dct(signal):
    N = len(signal)
    dct_coef = np.zeros(N)
    for k in range(N):
        sum_val = 0
        for n in range(N):
            sum_val += signal[n] * np.cos(np.pi * k * (2 * n + 1) / (2 * N))
        dct_coef[k] = sum_val * np.sqrt(2 / N)

    # Adjust the first coefficient
    dct_coef[0] *= np.sqrt(1 / 2)
    
    return dct_coef

signal = [1.0, 2.0, 3.0, 4.0]
coefficients = dct(signal)
print(coefficients)

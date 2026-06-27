import numpy as np

def compare_harmonic_series(n):
    S_n = np.float32(0.0)
    for i in range(1, n + 1):
        S_n += np.float32(1.0 / i)

    s_n = np.float32(0.0)
    for i in range(n, 0, -1):
        s_n += np.float32(1.0 / i)

    difference = s_n - S_n

    return S_n, s_n, difference

S_n, s_n, diff = compare_harmonic_series(100)
print(S_n)
print(s_n)
print(diff)


""" numpy was used here to force 32-bit storage on memory for float
by standard python uses float64 which was have burried decimal error bit to far
in this code we get to see 7 decimal places which would have been 15-17 is it was done normally"""

"""This solution presents the case usually this equation would have been equal in 
standard arithmetics but computationally, due to rounding because of IEEE 754 standard
where 1 bit is given to sign, 8 are given to exponent and 23 to significand
1 + 8 + 23 = 32 bit total """

""" Breaking point for Float32 is 2 to power 24 and for Float64(default) is 2 to power 53
if you try to subtract a number that hits these limits by one you still get the same answer."""

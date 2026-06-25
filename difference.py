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
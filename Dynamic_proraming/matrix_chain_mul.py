import numpy as np

def mcm(p):
    n = len(p)
    m = np.zeros((n, n), dtype=int)
    s = np.zeros((n, n), dtype=int)

    # Perform matrix chain multiplication
    for d in range(1, n - 1):
        for i in range(1, n - d):
            j = d + i
            min_value = float('inf')  # Reset min for each subproblem
            for k in range(i, j):    # `k` should range from `i` to `j-1`
                q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if min_value > q:
                    min_value = q
                    s[i][j] = k
            m[i][j] = min_value

    print("Minimum number of multiplications:", m[1][n-1])
    print("\nValue matrix (m):\n", m)
    print("\nSplit matrix (s):\n", s)

# Test with given dimensions
d = [5, 5, 4, 8, 2]
mcm(d)

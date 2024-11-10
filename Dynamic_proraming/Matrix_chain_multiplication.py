# def matrix_chain_order(dims):
#     # Number of matrices
#     n = len(dims) - 1

#     # m[i][j] will store the minimum cost of multiplying matrices from i to j
#     m = [[0 if i == j else float("inf") for j in range(n)] for i in range(n)]

#     # Fill the table with the minimum cost of multiplying matrices from i to j
#     for chain_length in range(2, n + 1):  # chain_length is the number of matrices in the chain
#         for i in range(n - chain_length + 1):
#             j = i + chain_length - 1
#             for k in range(i, j):
#                 cost = m[i][k] + m[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
#                 if cost < m[i][j]:
#                     m[i][j] = cost

#     return m[0][n - 1]


# # Example matrix dimensions
# dims = [5, 20, 10, 50]
# result = matrix_chain_order(dims)
# print("Minimum number of multiplications:", result)


def matrix_chain_order(dims):
    n = len(dims) - 1  # Number of matrices

    # m[i][j] will store the minimum cost of multiplying matrices from i to j
    m = [[0 if i == j else float("inf") for j in range(n)] for i in range(n)]
    
    # s[i][j] will store the split point k where the optimal split occurred
    s = [[0] * n for _ in range(n)]

    # Fill the table m with the minimum cost of multiplying matrices from i to j
    for chain_length in range(2, n + 1):  # Chain length is the number of matrices in the chain
        for i in range(n - chain_length + 1):
            j = i + chain_length - 1
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k  # Record the split point

    # Function to construct the optimal order
    def get_optimal_order(i, j):
        if i == j:
            return f"M{i+1}"  # Matrix indices start at 1 in this notation
        else:
            k = s[i][j]
            left_order = get_optimal_order(i, k)
            right_order = get_optimal_order(k + 1, j)
            return f"({left_order} x {right_order})"

    optimal_cost = m[0][n - 1]
    optimal_order = get_optimal_order(0, n - 1)
    
    return optimal_cost, optimal_order


# Example matrix dimensions
dims = [5, 20, 10, 50]
cost, order = matrix_chain_order(dims)
print("Minimum number of multiplications:", cost)
print("Optimal multiplication order:", order)

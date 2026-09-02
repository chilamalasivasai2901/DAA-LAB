def matrix_chain_order(p, n):
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n - 1]


n = int(input("Enter number of matrices: "))

p = []

print("Enter dimensions:")

for i in range(n):
    if i == 0:
        rows = int(input("Enter rows of matrix 1: "))
        p.append(rows)

    cols = int(input(f"Enter columns of matrix {i + 1}: "))
    p.append(cols)

result = matrix_chain_order(p, n + 1)

print("Minimum number of scalar multiplications:", result)
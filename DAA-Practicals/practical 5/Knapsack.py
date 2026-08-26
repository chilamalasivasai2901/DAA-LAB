def knapsack(W, wt, val, n):
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    val[i - 1] + dp[i - 1][w - wt[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


n = int(input("Enter number of items: "))

wt = []
val = []

for i in range(n):
    wt.append(int(input(f"Enter weight of item {i + 1}: ")))
    val.append(int(input(f"Enter value of item {i + 1}: ")))

W = int(input("Enter knapsack capacity: "))

result = knapsack(W, wt, val, n)

print("Maximum value:", result)
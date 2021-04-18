def knapsack(n, C, memo):
    if (n, C) in memo:
        return memo[(n, C)]

    if n == 0 or C == 0:
        result = 0
    elif w[n] > C:
        result = knapsack(n - 1, C, memo)
    else:
        #not put the item in knapsack
        tmp1 = knapsack(n - 1, C, memo)

        #put the item in knapsack
        tmp2 = v[n] + knapsack(n - 1, C - w[n], memo)
        result = max(tmp1, tmp2)

    memo[(n, C)] = result
    return result

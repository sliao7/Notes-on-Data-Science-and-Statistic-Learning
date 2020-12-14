import numpy as np
coins = [10,5,1]
n = len(coins)
S = 15
z = np.zeros((n+1, S+1))
for i in range(n):
    for t in range(1,S+1):
        if i == 0:
            z[i+1,t] = 1
        for k in range(0, t // coins[i]):
            z[i+1,t] += z[i-1,t - k * coins[i]]
print(z)

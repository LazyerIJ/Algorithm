N, K = map(int, input().split())
#N!/(K!(N-K)!)

coef = [[0 for _ in range(K+1)] for _ in range(N+1)]
for k in range(K+1):
    coef[k][k] = 1
for n in range(N+1):
    coef[n][0] = 1

for n in range(1, N+1):
    for k in range(1, K+1):
        coef[n][k] = coef[n-1][k] + coef[n-1][k-1]
print(coef[N][K])

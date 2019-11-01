N, K = map(int, input().split())
arr = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(K+1):
    arr[i][i] = 1
for i in range(N+1):
    arr[i][0] = 1

for n in range(1, N+1):
    for k in range(1, K+1):
        arr[n][k] = (arr[n-1][k] + arr[n-1][k-1]) % 10007
print(arr[N][K]%10007)

'''
https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients
(n, k) = nCk = n!/{(n-k)!k!} (0<=k<=n)

(n, k) = (n-1, k) + (n-1, k-1)

1       # choose 0 from []
1 1     # choose 0,1 from [a]
1 2 1   # choose 0,1,2 from [a,b]
1 3 3 1 # choose 0,1,2,3 from [a,b,c]
....

'''
import time
#solution 1 - factorial
def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans
def bino_coef_factorial(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)
print('[*]factorial')
start = time.time()
print(bino_coef_factorial(50, 3))
print('time: {}'.format(time.time() - start))
print()

#solution 2 - dp
def bino_coef(n, k):
    if k == 0 or n == k:
        return 1
    return bino_coef(n-1, k) + bino_coef(n-1, k-1)
print('[*]DP')
start = time.time()
print(bino_coef(50, 3))
print('time: {}'.format(time.time() - start))
print()

#solution 3 - dp. using matrix. cache.
def bino_coef_matrix(n, r):
    cache = [[0 for _ in range(r+1)] for _ in range(n+1)]

    for i in range(n+1):
        cache[i][0] = 1
    for i in range(r+1):
        cache[i][i] = 1

    for i in range(1, n+1):
        for j in range(1, r+1):
            cache[i][j] = cache[i-1][j] + cache[i-1][j-1]

    return cache[n][r]

print('[*]DP - matrix & cache')
start = time.time()
print(bino_coef_matrix(50, 3))
print('time: {}'.format(time.time() - start))
print()

#solution 4 - More Probability Side
def bino_coef_times_got_bottom_up(n, k):
    if k > n:
        return 0

    # 1.
    cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    # 2.
    def choose(times, got):
        # 3.
        if times == n:
            return got == k
        # 4.
        if cache[times][got] != -1:
            return cache[times][got]
	# 5.
        cache[times][got] = 1*choose(times+1, got) + 1*choose(times+1, got+1)
        return cache[times][got]

    # 6.
    return choose(0, 0)

print('[*]Times and Got - bottom up')
start = time.time()
print(bino_coef_times_got_bottom_up(50, 3))
print('time: {}'.format(time.time() - start))
print()

def bino_coef_times_got_top_down(n, k):
    if k > n:
        return 0

    # 1.
    cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    # 2.
    def choose(times, left):
        # 3.
        if times == 0:
            return left == 0
        # 4.
        if cache[times][left] != -1:
            return cache[times][left]
	# 5.
        cache[times][left] = 1*choose(times-1, left) + 1*choose(times-1, left-1)
        return cache[times][left]

    # 6.
    return choose(n, n-k)

print('[*]Times and Got - top down')
start = time.time()
print(bino_coef_times_got_top_down(50, 3))
print('time: {}'.format(time.time() - start))
print()

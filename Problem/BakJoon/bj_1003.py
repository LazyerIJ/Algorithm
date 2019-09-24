MEM = [[1,0], [0,1]]
MEM.extend([[-1,-1]]*39)
def fibonacci(n):
    """fibonacci
    https://www.acmicpc.net/problem/1003
    :param n: fibonacci number index
    """
    if n == 0:
        return MEM[0]
    elif n == 1:
        return MEM[1]

    if MEM[n] == [-1, -1]:
        prev1 = fibonacci(n-1)
        prev2 = fibonacci(n-2)
        MEM[n] = [prev1[0] + prev2[0],
                  prev1[1] + prev2[1]]
        return MEM[n]
    else:
        return MEM[n]

if __name__ == '__main__':
    a = int(input())
    for step in range(a):
        n = int(input())
        rs = fibonacci(n)
        print(rs[0], rs[1])

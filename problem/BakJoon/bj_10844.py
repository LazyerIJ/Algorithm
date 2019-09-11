"""bj_10844.py
https://www.acmicpc.net/problem/10844
"""
def dp(num):
    """dp
    get stairs case

    :param num:input
    """
    total = 9
    for step in range(1, num):
        total = (total-(step))*2 + (step-1)
    return total

if __name__ == '__main__':
    num = int(input())
    print(dp(num)%1000000000)


"""bj_1463.py
https://www.acmicpc.net/problem/1463
"""
def cal_dp(num):
    """cal_dp
    calculate all case num
    1. if X%3==0 : X = X//3
    2. if X%2==0 : X = X//2
    3. X = X - 1
    ... if X== 1 : answer

    :param num:input num
    """
    dp = [0] * (num+1)
    for idx in range(2, num+1):
        candidates = []
        if idx%3 == 0:
            candidates.append(dp[idx//3])
        if idx%2 == 0:
            candidates.append(dp[idx//2])
        candidates.append(dp[idx-1])
        dp[idx] = 1 + min(candidates)
    return dp[-1]
    

if __name__ == '__main__':
    num = int(input())
    print(cal_dp(num))

"""bj_2579
https://www.acmicpc.net/problem/2579"""
def get_point(steps):
    """get_point

    :param steps:steps array
    """
    #index 계단을 밟았을 경우
    #1. index-1 계단을 밟았다.
    #   -> index-3계단을 밟았다.
    #2. index-2 계단을 밟았다.
    #따라서,
    #dp[index]
    # = max(1번, 2번)
    # = max(steps[n] + steps[n-1] + dp[n-3], steps[n] + dp[n-2])
    steps = [0] + steps
    dp = [steps[0], steps[1]]
    for idx in range(2, len(steps), 1):
        prev_1 = max(0, idx - 1)
        prev_2 = max(0, idx - 2)
        prev_3 = max(0, idx - 3)
        dp.append(max(steps[idx] + steps[prev_1] + dp[prev_3],
                      steps[idx] + dp[prev_2]))
    return dp[-1]

if __name__ == '__main__':
    height = int(input())
    steps = []
    for idx in range(height):
        steps.append(int(input()))
    print(get_point(steps))


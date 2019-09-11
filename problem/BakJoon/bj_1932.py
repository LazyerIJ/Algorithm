"""bj_1932

https://www.acmicpc.net/problem/1932
"""
def get_summary(datas):
    summary = [datas.pop(0)]
    for idx1, data in enumerate(datas):
        tmp = []
        for idx2, d in enumerate(data):
            _max = max([summary[idx1][max([0, idx2-1])],
                        summary[idx1][min([idx1, idx2])]])
            tmp.append(_max + d)
        summary.append(tmp)
    return summary[-1]

if __name__ == '__main__':
    HEIGHT = int(input())
    TRIANGLE = list()
    for step in range(HEIGHT):
        _input = input().split(" ")
        TRIANGLE.append(list(map(int, _input)))
    print(max(get_summary(TRIANGLE)))

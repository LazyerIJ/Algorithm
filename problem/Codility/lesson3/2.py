def solution(A):
    return (set(list(range(1, len(A)+2))) - set(A)).pop()


if __name__ == '__main__':
    case1 = list(range(1,10))
    case1.remove(5)
    print(solution(case1))

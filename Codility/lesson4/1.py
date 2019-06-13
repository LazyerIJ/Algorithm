def solution(A):
    rs = 0
    if len(set(A))==len(A)==max(A):
        rs=1
    return rs


if __name__ == '__main__':
    print(solution([4,1,3,2]))
    print(solution([4,1,3]))
    print(solution([4,1,1]))

'''
https://app.codility.com/c/run/training4EEBUQ-C56/
'''

def solution(A, K):
    if len(A)==0:
        return A
    K %= len(A)
    if K != len(A):
        A = A[-K:] + A[:-K]
    return A



if __name__ == '__main__':
    print(solution([3,8,9,7,6], 3))
    print(solution([0,0,0],1))
    print(solution([],1))

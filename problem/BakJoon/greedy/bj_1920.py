'''
https://www.acmicpc.net/problem/1920
'''
import sys
input = sys.stdin.readline

'''
이진탐색
O(NlogM)
516ms
'''
def solution_bin():
    A_SIZE = int(input())
    A = [int(x) for x in input().split()]
    M_SIZE = int(input())
    M = [int(x) for x in input().split()]

    A.sort()
    def binary_search(A, m):
        flag = 0
        left = 0
        right = len(A)
        while left<right:
            mid = (left + right) // 2
            if (left == mid) and (m != A[mid]):
                break
            if m > A[mid]:
                left = mid
            elif m < A[mid]:
                right = mid
            elif m == A[mid]:
                flag = 1
                print(1)
                break
        if flag == 0:
            print(0)
    for m in M:
        binary_search(A, m)

'''
정렬 후 index를 넘겨가며 탐색
O(N)
468ms
'''
def solution():
    A_SIZE = int(input())
    A = [int(x) for x in input().split()]
    M_SIZE = int(input())
    M = [[i, int(x)] for i, x in enumerate(input().split())]
    flag = [0] * M_SIZE
    A.sort()
    M.sort(key=lambda x: x[1])
    idx_a = 0
    idx_m = 0
    while (idx_a<A_SIZE) and (idx_m<M_SIZE):
        val_a = A[idx_a]
        val_m = M[idx_m]
        if A[idx_a] == val_m[1]:
            flag[val_m[0]] = 1
            idx_a += 1
            idx_m += 1
        else:
            while val_a < val_m[1]:
                idx_a += 1
                if idx_a >= A_SIZE:
                    break
                val_a = A[idx_a]
            while val_m[1] < val_a:
                idx_m += 1
                if idx_m >= M_SIZE:
                    break
                val_m = M[idx_m]
    if len(M)>1:
        for i in range(1, len(M)):
            if M[i][1] == M[i-1][1]:
                flag[M[i][0]] = flag[M[i-1][0]]
    for f in flag:
        print(f)
#solution()

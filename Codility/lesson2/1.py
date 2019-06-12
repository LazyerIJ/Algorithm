'''
https://app.codility.com/c/run/trainingVK3VUX-VDH/
'''
def solution(A):
    # correctness : 100 / performance : 50 / score : 77
    '''
    flag = [0] * 1000000
    for num in A:
        flag[num] += 1
        flag[num] %= 2
    return flag.index(1)
    '''
    if len(A) == 1:
        return A[0]

    A = sorted(A)
    for i in range(0, len(A), 2):
        if i+1 == len(A):
            return A[-1]
        if A[i] != A[i+1]:
            return A[i]
    return A[-1]
        

if __name__ == '__main__':
    arr = [9, 3, 9, 3, 9, 7, 9,  7, 1]
    print(solution(arr))
    arr = [42]
    print(solution(arr))

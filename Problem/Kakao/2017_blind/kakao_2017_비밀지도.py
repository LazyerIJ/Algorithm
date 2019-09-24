def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        a = list("{:0b}".format(a).rjust(n, '0'))
        b = list("{:0b}".format(b).rjust(n, '0'))
        answer.append(''.join([' ' if int(a1)+int(b1)==0 else '#'
                       for (a1, b1) in zip(a, b)]))
    return answer


if __name__ == '__main__':
    n=5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))
    

def solution(n, t, m, p):
    #n : 진법
    #t : 숫자 개수
    #m : 참가 인원
    #p : 튜브의 순서
    def n_num(num, n):
        n_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                  'A', 'B', 'C', 'D', 'E', 'F']
        rs = ''
        while num//n != 0:
            tmp = num%n
            rs = n_list[tmp] + rs
            num = num//n
        return n_list[num%n] + rs
    answer = '' 
    n_str = ''.join([n_num(x, n) for x in range(m*t)])
    step = p-1
    for i in range(t):
        answer += n_str[step]
        step += m
    return answer


if __name__ == '__main__':
    n=2
    t=4
    m=2
    p=1
    result="0111"
    print(result, solution(n, t, m, p))


    n=16
    t=16
    m=2
    p=1
    result="02468ACE11111111"
    print(result, solution(n, t, m, p))

    n=16
    t=16
    m=2
    p=2
    result="13579BDF01234567"
    print(result, solution(n, t, m, p))

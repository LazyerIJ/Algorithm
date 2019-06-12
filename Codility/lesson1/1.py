'''
https://app.codility.com/c/run/trainingU64HFX-65S/
'''
def solution(num):
    def intoBinary(number):
        binarynumber=""
        if (number!=0):
            while (number>=1):
                if (number %2==0):
                    binarynumber=binarynumber+"0"
                    number=number/2
                else:
                    binarynumber=binarynumber+"1"
                    number=(number-1)/2

        else:
            binarynumber="0"
        return "".join(reversed(binarynumber))

    bin_num =intoBinary(num) 
    max_count = 0
    count=0
    flag = False
    for idx in bin_num:
        if idx=='1':
            max_count = count if count>max_count else max_count
            count=0
        elif idx=='0':
            count+=1
    return max_count

                

if __name__=='__main__':
    rs = solution(529)
    ans = 4
    print('rs : {} / ans : {}'.format(rs, ans))
    rs = solution(1041)
    ans = 5
    print('rs : {} / ans : {}'.format(rs, ans))

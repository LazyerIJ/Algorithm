'''
TieRopes
https://app.codility.com/c/run/trainingRUNS2T-ADB/
'''
def solution(K, A):
    length = 0
    rs = 0
    for num in A:
        length += num
        if length >= K:
            length=0
            rs+=1
    return rs

if __name__ == '__main__':

    testcase = []
    testcase.append({'K': 4, 'A': [1, 2, 3, 4, 1, 1, 3]})
    rslist = []
    rslist.append([3])
    for case, rs in zip(testcase, rslist):
        myrs = solution(**case)
        print('mine: {}'.format(myrs), end='\t')
        print('ans : {}'.format(rs[0]))


'''
https://www.welcomekakao.com/learn/courses/30/lessons/17682
'''
def solution(dartResult):
    import re
    rs = []
    darts = re.findall(r"[0-9]+[D|S|T]+[#,\*]*", dartResult)
    for idx in range(len(darts)):
        dart = darts[idx]
        flag = None
        if '*' in dart:
            flag = 2
            dart = dart[:-1]
        elif '#' in dart:
            flag = -1
            dart = dart[:-1]
        dart = dart.replace('S','**1').replace('D','**2').replace('T','**3')
        point = eval(''.join(dart))
        if flag==2:
            if rs:
                rs[-1] = rs[-1] * 2
            point = point * 2
        elif flag == -1:
            point = point * -1
        rs.append(point)
    return sum(rs)

def solution(dartResult):
    import re
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer




if __name__ == '__main__':
    dartResult = '1S2D*3T'
    answer = 37
    print(answer, solution(dartResult))
    dartResult = '1D2S#10S'
    answer = 9 
    print(answer, solution(dartResult))
    dartResult = '1D2S0T'
    answer = 3
    print(answer, solution(dartResult))
    dartResult = '1S*2T*3S'
    answer = 23
    print(answer, solution(dartResult))
    dartResult = '1D#2S*3S'
    answer = 5
    print(answer, solution(dartResult))
    dartResult = '1T2D3D#'
    answer = -4
    print(answer, solution(dartResult))
    dartResult = '1D2S3T*'
    answer = 59
    print(answer, solution(dartResult))

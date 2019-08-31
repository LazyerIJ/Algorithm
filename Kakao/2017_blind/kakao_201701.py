'''https://www.welcomekakao.com/learn/courses/30/lessons/17676
트래픽 시작, 종료 지점의 처리량만 비교 > O(n^2)
'''
def solution(lines):

    import datetime
    dates = []
    sec = datetime.timedelta(milliseconds=999)
    for line in lines:
        time = ' '.join(line.split(' ')[:-1])
        micro = float(line.split(' ')[-1][:-1]) * 1000 - 1
        micro = datetime.timedelta(milliseconds=micro)
        end_time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
        dates.append([end_time - micro, end_time])

    rs = 0
    for date_1 in dates:
        traffic_1 = traffic_2 = 0
        for date_2 in dates:
            #date_1의 종료 시간을 기준으로 date_2의 시작 가능 시간과 종료 가능 시간
            if date_2[0]-sec <= date_1[1] <= date_2[1]:
                traffic_1 += 1
            #date_1의 시작 시간을 기준으로 date_2의 시작 가능 시간과 종료 가능 시간
            if date_2[0]-sec <= date_1[0] <= date_2[1]:
                traffic_2 += 1
        traffic = max([traffic_1, traffic_2])
        rs = traffic if traffic>rs else rs
    return rs

if __name__ == '__main__':
    lines1 =  ["2016-09-15 20:59:57.421 0.351s",
                "2016-09-15 20:59:58.233 1.181s",
                "2016-09-15 20:59:58.299 0.8s",
                "2016-09-15 20:59:58.688 1.041s",
                "2016-09-15 20:59:59.591 1.412s",
                "2016-09-15 21:00:00.464 1.466s",
                "2016-09-15 21:00:00.741 1.581s",
                "2016-09-15 21:00:00.748 2.31s",
                "2016-09-15 21:00:00.966 0.381s",
                "2016-09-15 21:00:02.066 2.62s"]

    lines2 = ["2016-09-15 01:00:04.002 2.0s",
              "2016-09-15 01:00:07.000 2s"]

    lines3 = ["2016-09-15 01:00:04.001 2.0s",
              "2016-09-15 01:00:07.000 2s"]

    print(solution(lines1))#7
    print(solution(lines2))#2
    print(solution(lines3))#1

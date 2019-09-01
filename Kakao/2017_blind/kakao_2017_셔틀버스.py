'''
https://www.welcomekakao.com/learn/courses/30/lessons/17678
'''
def solution(n, t, m, timetable):
    '''
    09:00부터 t분 간격으로 n번 m명을 태울 수 있는 버스가 온다.
    timetable의 시간 순서로 크루가 줄을 선다.
    늦어도 몇 시 까지 줄을 서야 하는가

    for문을 벗어나서 마지막에 return에 if처리를 하지않아 골먹었음.
    '''
    from datetime import datetime, timedelta

    def add_time(time):
        time = datetime.strptime('09:00', '%H:%M') + timedelta(milliseconds=time*60*1000)
        return "{:0>2}:{:0>2}".format(time.hour, time.minute)
    def minus_one(time):
        time = datetime.strptime('{}:{}'.format(time[:2], time[-2:]), '%H:%M')
        time = time - timedelta(milliseconds=60*1000)
        return "{:0>2}:{:0>2}".format(time.hour, time.minute)

    last_bus = add_time(t*(n-1))
    timetable = sorted([x for x in timetable if x<=last_bus])

    if len(timetable)==0:
        return last_bus

    for idx in range(n):  # 버스가 오는 수
        max_people = (n-idx)*m
        crue = 0  # 탑승한 크루 수
        cur_time = add_time(t*idx)
        while crue < m and timetable[0]<=cur_time:
            last_crue = timetable.pop(0)
            crue += 1  # 탑승자 + 1
            max_people -= 1 # 총 탑승 가능 수 -1
            if len(timetable)==0:
                if max_people>0:
                    return last_bus
                return minus_one(last_crue)
    if max_people>0:
        return last_bus
    return minus_one(last_crue)


if __name__ == '__main__':
    n = 2
    t = 10
    m = 1
    timetable = ["08:00"]
    rs = "09:10"
    print('case1>>', rs, solution(n, t, m, timetable))

    n = 2
    t = 10
    m = 2
    timetable = ["09:10", "09:09", "08:00"]
    rs = "09:09"
    print('case2>>', rs, solution(n, t, m, timetable))

    n = 2
    t = 1
    m = 2
    timetable = ["09:00", "09:00", "09:00", "09:00"]
    rs = "08:59"
    print('case3>>', rs, solution(n, t, m, timetable))

    n = 1
    t = 1
    m = 5
    timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]	
    rs = "00:00"
    print('case4>>', rs, solution(n, t, m, timetable))

    n = 1
    t = 1
    m = 1
    timetable = ["23:59"]
    rs = "09:00"
    print('case5>>', rs, solution(n, t, m, timetable))

    n = 10
    t = 60
    m = 45
    timetable = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                 "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                 "23:59", "23:59", "23:59", "23:59", ]
    rs = "18:00"
    print('case6>>', rs, solution(n, t, m, timetable))

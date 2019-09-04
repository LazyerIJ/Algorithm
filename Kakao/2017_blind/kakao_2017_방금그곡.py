def solution(m, musicinfos):
    from datetime import datetime
    def replace_music(m):
        m = m.replace('C#', 'Z').replace('D#', 'Y').replace('F#', 'X')
        m = m.replace('G#', 'W').replace('A#', 'U')
        return m
    rs_title = []
    rs_time = []
    for info in musicinfos:
        split_str = info.split(',')
        s_time = split_str[0]
        e_time = split_str[1]
        title = split_str[2]
        music = replace_music(split_str[3])
        music_len = (datetime.strptime(e_time, '%H:%M')\
                     - datetime.strptime(s_time, '%H:%M')).seconds//60
        total_music = (music_len//len(music))*music + music[0:music_len%len(music)]

        if replace_music(m) in total_music:
            rs_title.append(title)
            rs_time.append(music_len)

    if len(rs_title)>0:
        return rs_title[rs_time.index(max(rs_time))]
    return "(None)"


if __name__ == '__main__':
    m = 'ABCDEFG'
    musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    rs = "HELLO"
    print(rs, solution(m, musicinfos))

    m = "CC#BCC#BCC#BCC#B"
    musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
    rs = "FOO"
    print(rs, solution(m, musicinfos))

    m = "ABC"
    musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]	
    rs = 'WORLD'
    print(rs, solution(m, musicinfos))


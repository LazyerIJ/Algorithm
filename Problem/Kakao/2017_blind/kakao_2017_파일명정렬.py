def solution(files):
    # sort and get index: [i[0] for i in sorted(enumerate(myList), key=lambda x:x[1])]
    import re
    rs = []
    r = re.compile('(\d+)')
    key = None
    for file in files:
        tmp = []
        for i, t in enumerate(re.split(r, file)):
            if t.isdigit():  # save key
                key = i
                tmp.append(int(t))
            else:
                if key!=None and i>key:  # save tail
                    tmp.append(i)
                    #파일마다 re.split의 길이가 다를 수 있으므로 tail 확인 후 break 필요 
                    break
                else:
                    tmp.append(t.lower())  # save head
        rs.append(tmp)
        index = [i[0] for i in sorted(enumerate(rs), key=lambda x:x[1])]
    answer = [files[x] for x in index]
    return answer


if __name__ == '__main__':
    files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    print(solution(files))

    files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
    print(solution(files))

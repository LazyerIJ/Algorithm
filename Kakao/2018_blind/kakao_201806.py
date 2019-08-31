'''
https://www.welcomekakao.com/learn/courses/30/lessons/42893?language=python3
매칭 점수
- 문제의 조건을 잘 확인하자
1. 모든 url 은 https://로 시작한다 -> 제대로 된 url이 존재하지 않을 수 있다.
2. 한 웹 페이지 문자열의 길이는 1이상 1500이하이다 -> head, body가 없을 수 있다.
...
'''
def solution(word, pages):
    import re
    points = {}
    index_pages = []  #head 파싱하여 해당 page url을 저장, index 순서
    index_points = [] #page url에 따른 포인트, index 순서

    def find_url(sentence):
        group = re.search('<meta property="og:url" content="https://((.|\n)*?)"/>', sentence)
        if group:
            return group.group(1)
        return None
    
    def find_link(sentence):
        group = re.findall('<a href="https://((.|\n)*?)">', sentence)
        return group

    def find_word(target, sentence):
        target = target.lower()
        count = 0
        for word in re.split('[^a-zA-Z]', sentence):
            if word.lower() == target:
                count+=1
        return count

    def find_body_head(page, key):
        group = re.search('<{}>((.|\n)*?)<\/{}>'.format(key, key), page)
        if group:
            return group.group(1)
        return None

    def cleanhtml(raw_html):
        return re.sub(re.compile('<.*?>'), '', raw_html)

    for idx, page in enumerate(pages):
         
        #process body
        body = find_body_head(page, key='body')
        word_count = 0

        #if body exist
        if body:
            #check word&link count
            word_count = find_word(word, cleanhtml(body))
            #process point. add link point(=base point / link count) to link
            groups = find_link(body)
            for group in groups:
                point = points.get(group[0], 0)
                points[group[0]] = point + word_count/len(groups)

        #process head
        head = find_body_head(page, key='head')
        url = None
        if head:
            url = find_url(head)
        index_pages.append(url)
        if url:
            point = points.get(url, 0)
            points[url] = point + word_count

    #find max point page
    if len(index_pages)<1:
        return 0
    for page in index_pages:
        point = 0
        if page != None:
            point = points[page]
        index_points.append(point)
    max_point = max(index_points)
    return index_points.index(max_point)

if __name__ == '__main__':
    word = 'Muzi'
    pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

    print(solution(word, pages))
    


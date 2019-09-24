def solution(words, queries):
    words = sorted(list(set(words)))
    answer = []
    import re
    for query in queries:
        count=0
        #query = query.replace('?','[a-z]+')
        r = re.compile(query.replace('?','[a-z]'))
        for word in words:
            if r.match(word) and len(query)==len(word):
                count+=1
            if len(word)>len(query):
                continue
        answer.append(count)
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]	
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print([3, 2, 4, 1, 0], solution(words, queries))

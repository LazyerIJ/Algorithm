def solution(cacheSize, cities):
    cache = [None for x in range(cacheSize)]
    runtime = 0
    if cacheSize==0:
        return len(cities)*5
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            runtime += 1
        else:
            cache = cache[1:] + [city]
            runtime += 5
    return runtime

if __name__ == '__main__':
    cacheSize=3
    cities=["Jeju", "Pangyo", "Seoul", "NewYork",
            "LA", "Jeju", "Pangyo", "Seoul",
            "NewYork", "LA"]
    rs=50
    print(rs, solution(cacheSize, cities))


    cacheSize=3
    cities=["Jeju", "Pangyo", "Seoul", "Jeju",
            "Pangyo", "Seoul", "Jeju", "Pangyo",
            "Seoul"]	
    rs=21
    print(rs, solution(cacheSize, cities))

    cacheSize=2
    cities=["Jeju", "Pangyo", "Seoul", "NewYork",
            "LA", "SanFrancisco", "Seoul", "Rome",
            "Paris", "Jeju", "NewYork", "Rome"]	
    rs=60
    print(rs, solution(cacheSize, cities))

    cacheSize=5
    cities=["Jeju", "Pangyo", "Seoul", "NewYork",
            "LA", "SanFrancisco", "Seoul", "Rome",
            "Paris", "Jeju", "NewYork", "Rome"]	
    rs=52
    print(rs, solution(cacheSize, cities))

    cacheSize=2
    cities=["Jeju", "Pangyo", "NewYork", "newyork"]	
    rs=16
    print(rs, solution(cacheSize, cities))

    cacheSize=0
    cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	
    rs=25
    print(rs, solution(cacheSize, cities))

    cacheSize=0
    cities=[]	
    rs=0
    print(rs, solution(cacheSize, cities))


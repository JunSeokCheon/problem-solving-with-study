# 찾으려는 데이터가 이미 캐시돼있다면 cache hit이 발생한다. 즉 메인 메모리를 거치지 않고 빠르게 데이터를 불러올 수 있다.
# 반대로 캐시돼있지 않다면 cache miss가 발생한다. 최악의 경우 메인 메모리에서 데이터를 가져와야 한다.

def solution(cacheSize, cities):
    cache = []
    cities = [city.lower() for city in cities]
    answer = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        if not city in cache:
            if len(cache) < cacheSize:
                cache.append(city)
                answer += 5
            else:
                cache.pop(0)
                cache.append(city)
                answer += 5
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer += 1
    return answer

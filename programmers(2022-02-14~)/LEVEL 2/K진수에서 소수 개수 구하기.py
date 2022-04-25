def solution(n, k):
    word=''

    while n:
        word += str(n%k)
        n = n//k

    word = word[::-1]

    li=word.split('0')
    lis=[]
    for i in li:
        if len(i)>0:
            lis.append(i)
    li=list(map(int,lis))

    count=0
    for i in li:
        prime=True
        if i < 2:
            continue
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                prime=False
                break
        if prime:
            count+=1

    return count
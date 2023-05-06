import sys
# #1로만 이루어진 n의 배수 (n:3, 111)

# num = list(map(int, sys.stdin.readline().split()))

# #자릿수 비교하면서 나눠서 0나오면 값 리스트에? 저장
# #반복

# #onelist = list(map(1+*10))

# #1, 11(10), 111(100), 1111(1000)
# #for (if(len(num) ==)


# print(list(map(len(str(onelist)))))

#반복문을 여러줄로 입력받아야 할 때 시간초과 방지를 위해 input대신에 사용
#sys.stdin.readline().strip()



#나머지 연산 이용하기
#https://merry555.tistory.com/m/13
#https://codingwonny.tistory.com/207
while True: #무한루프
    try:
        n = int(input())
    except:
        break
    num = 1
    cnt = 1
    while True:
        if num %n != 0:
            num = num*10+1 
            cnt += 1
        else:
            break
    print(cnt)

#나머지 연산은 자주 나옴
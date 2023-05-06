#약수
#주어진 약수로 n구하기
#n: 약수를 찾게되는 부모숫자, sub: 약수, cnt:약수의 개수

#<1>
sub = []   
cnt = int(input())
sub = list(map(int, input().split())) 
sub.sort()
#N찾기
def find_n(sub, cnt):
    #리스트의 처음값과 끝값의 곱이 N, 약수 개수가 1개면 그 값 제곱한게 N    
    if(cnt == 1):
        n = sub[0]*sub[0]
    else:
        n = sub[0] * sub[cnt-1]
    print(n)
find_n(sub, cnt)
#제출하면 틀렸습니다 뜸..왜? 정렬해주고 다시 돌려보기
#list [0] = list[-1] 한 개 값만 있을 때

#<2>
# n = int(input())
# a = list(map(int, input().split()))
# a_max = max(a)
# a_min = min(a)
# print(a_max*a_min)

#split - 여러 개의 input 받을 수 있게 해줌
#map함수 - 리스트에 사용하는 함수, for대신 사용하기 좋음
#함수 두 개 쓰는 것 vs 하나에 몰아 쓰는 것 시간 더 짧은 것은? 함수를 나누면 성능 올라감

#퇴사
#N+1일째 퇴사 - 1일째의 일은 피할 수 없나?oo
#마지막 N번째 t == 1일 경우만 일 수행
#최대 P구하기
#https://dojang.io/mod/page/view.php?id=2179 입력 값을 변수 두 개에 저장하기
import sys

tp = 0
t_list = []  
p_list = []
n = int(input())
for _ in range(n):
    t, p =  map(int, input().split())
    t_list.append(t)
    p_list.append(p)
    #t, p = input().split()같은 식
    #t = int(t)
    #p = int(p)
i = 0
while(i < n):
    if t_list[i] > n-i+1:
        break
    else:
        tp += p_list[i]

        i += t_list[i]        

print(tp)
           



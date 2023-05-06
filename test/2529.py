#부등호
#23.05.04
#1. 문자열로 들어오는 부등호 판별하기
#2. 0-9까지 숫자 순서대로 다 대입하여 1의 조건 맞는 애들 뽑아서 리스트에 넣기
#3. 중복 피해서 max, min값 추출하기 (0-9 순서로 순서를 받으므로 첫번째가 min 마지막이 max가 된다)
#https://data-flower.tistory.com/76

num = int(input())
sign = list(input().split())
max_r, min_r = "", ""
visited = [False]*10

def check(i, j, k):
    if k == "<":
        return i < j
    else:
        return i > j
    #return True #?
    
def sort_by_str(cnt, r):
    global max_r, min_r  #이렇게 global 해줘야 하는 이유
    if cnt == num+1:
        if not len(min_r):
            min_r = r
        else:
            max_r = r
        return
    
    for i in range(10):
        if not visited[i]:#아직 방문 안헀다면
            if cnt == 0 or check (r[-1], str(i), sign[cnt-1]):
                visited[i] = True 
                sort_by_str(cnt+1, r +str(i)) #r 문자열 개수 한개 추가
                visited[i] = False

sort_by_str(0, "")
print(max_r)
print(min_r)
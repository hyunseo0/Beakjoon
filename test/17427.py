#약수의 합
#숫자 n입력 -> n이하 각 자연수의 약수 값들의 합(재귀?)
# g(n) = 1*(n/1) + 2*(n/2) ...+n*(n/n)
#https://data-flower.tistory.com/95https://data-flower.tistory.com/95

n = int(input())
sum = 0

#파이썬은 반복문에서 i초기값 설정 필요없음 range뒤에 범위 지정하기 때문에
for i in range(1, n+1):
    sum+= (n//i)*i
print(sum)

     

#RecursionError: maximum recursion depth exceeded in comparison
#파이썬에서는 재귀한도가 정해져 있음, 시스템의 안정을 위해 
#재귀한도 풀어주는 코드 찾아보기


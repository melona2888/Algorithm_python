# Input Values
# N, M, K
# N : 배열의 크기
# M : 덧셈 횟수
# K : 동일 숫자 덧셈 횟수

n, m, k = map(int, input().split())
array_data = list(map(int, input().split()))

array_data.sort()
no1 = array_data[-1]
no2 = array_data[-2]
res = 0

# 검증
if len(array_data) != n:
    print(len(array_data), n, "dismatch")
    exit()

# Math
quot = m // (k+1)
remain = m % (k+1)
print ("quot : ", quot, ", remain : ", remain)

# Calculate
quot_calc =  quot * ((no1 * k) + no2)
remain_calc = remain * no1 

result = quot_calc + remain_calc

print(result)
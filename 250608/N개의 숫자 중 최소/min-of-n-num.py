n = int(input())
a = list(map(int, input().split()))

# 최소값 구하기
min_value = min(a)

# 최소값 개수 세기
count = a.count(min_value)

# 출력
print(min_value, count)

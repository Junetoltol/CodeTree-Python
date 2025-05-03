# 입력
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# M이 몇 번 나오는지 count 함수 사용
count = numbers.count(M)

# 출력
print(count)

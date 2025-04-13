N = int(input())
result = []

# 1부터 시작해서 N보다 큰 N의 배수를 찾음
for i in range(1, 6):  # 5개만 필요하니까 1부터 5까지
    result.append(N * (i))  # i+1을 곱하면 N보다 큰 배수

# 출력
print(" ".join(map(str, result)))

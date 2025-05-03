# 입력받기
numbers = list(map(int, input().split()))

# 인덱스는 0부터 시작하므로 2, 4, 9번째 요소 선택
result = numbers[2] + numbers[4] + numbers[9]

# 출력
print(result)

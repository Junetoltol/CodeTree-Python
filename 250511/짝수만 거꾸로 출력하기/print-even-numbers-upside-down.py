N = int(input())
numbers = list(map(int, input().split()))

# 입력의 역순으로 뒤집고 짝수만 선택
for num in reversed(numbers):
    if num % 2 == 0:
        print(num, end=' ')

N = int(input())  # 입력 받기

num = 1  # 시작 숫자

for i in range(1, N + 1):
    for _ in range(i):
        print(num, end=' ')
        num += 1
    print()  # 줄 바꿈

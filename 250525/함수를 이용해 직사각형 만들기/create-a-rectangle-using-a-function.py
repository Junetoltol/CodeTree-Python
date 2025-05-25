n, m = map(int, input().split())

# Please write your code here.
def print_rectangle(n, m):
    for _ in range(n):            # n번 반복
        print('1' * m)            # 한 줄에 1을 m개 출력

# 사용자 입력 받기

print_rectangle(n, m)

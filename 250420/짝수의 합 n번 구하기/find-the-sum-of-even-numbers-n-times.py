N = int(input())  # 테스트 케이스 수

for _ in range(N):
    a, b = map(int, input().split())
    even_sum = sum(i for i in range(a, b + 1) if i % 2 == 0)
    print(even_sum)

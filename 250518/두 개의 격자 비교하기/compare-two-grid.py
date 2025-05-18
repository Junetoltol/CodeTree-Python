# 입력 받기
N, M = map(int, input().split())

# 첫 번째 격자 A 입력
A = [list(map(int, input().split())) for _ in range(N)]

# 두 번째 격자 B 입력
B = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
for i in range(N):
    for j in range(M):
        if A[i][j] == B[i][j]:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()

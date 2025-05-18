# 4x4 배열 입력 받기
arr = [list(map(int, input().split())) for _ in range(4)]

# 특정 영역 합 계산: 행 1~3, 열 0~2
total = 0
for i in range(1, 4):         # 1행~3행 (index 1~3)
    for j in range(0, 3):     # 0열~2열 (index 0~2)
        total += arr[i][j]

print(total)

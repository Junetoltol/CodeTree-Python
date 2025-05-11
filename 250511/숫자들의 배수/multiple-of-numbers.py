arr = []
count_5 = 0

while True:
    n = int(input())
    if n < 10 or n > 100:
        continue  # 조건에 맞지 않으면 다시 입력

    arr.append(n)

    if n % 5 == 0:
        count_5 += 1

    if count_5 == 2:
        break

print(*arr)

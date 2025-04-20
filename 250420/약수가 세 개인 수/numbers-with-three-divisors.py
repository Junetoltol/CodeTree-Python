import math

# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 입력
start, end = map(int, input().split())

count = 0
for i in range(start, end + 1):
    root = int(math.isqrt(i))
    if root * root == i and is_prime(root):
        count += 1

print(count)

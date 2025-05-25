n = int(input())

# Please write your code here.
def sum_div_10(n):
    total = sum(range(1, n + 1))   # 1부터 n까지의 합
    return total // 10            # 10으로 나눈 몫 반환

print(sum_div_10(n))

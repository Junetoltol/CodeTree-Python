n = int(input())

# Please write your code here.
def check_number(n):
    if n % 2 == 0:  # 짝수 여부 확인
        digit_sum = sum(int(d) for d in str(n))  # 각 자리수 합
        if digit_sum % 5 == 0:
            return "Yes"
    return "No"

# 입력 받기
print(check_number(n))

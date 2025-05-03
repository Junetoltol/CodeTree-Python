# 입력
a, b = map(int, input().split())

# 초기 리스트
sequence = [a, b]

# 총 10개 숫자가 될 때까지 반복
while len(sequence) < 10:
    next_num = (sequence[-1] + sequence[-2]) % 10  # 앞 두 수의 합의 일의 자리
    sequence.append(next_num)

# 출력
print(' '.join(map(str, sequence)))

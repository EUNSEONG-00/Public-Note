# 자리수 합 리턴
def sum_digit(num):
    # 여기에 코드를 작성하세요
    total = 0
    str_num = str(num)

    for i in range(len(str_num)):
        num = str_num[i]
        total += int(num)

    return total


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 여기에 코드를 작성하세요
digit_total = 0
for i in range(1, 1001):
    digit_total += sum_digit(i)

print(digit_total)
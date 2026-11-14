startgop = int(input("시작곱의 숫자를 입력하시오"))
endgop = int(input("마지막곱의 숫자를 입력하시오"))
start = startgop
while start <= endgop:
    print(f"8 * {start} = {start * 8}")
    start += 1
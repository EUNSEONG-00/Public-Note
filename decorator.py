def add_print_to(original):
    # 데코레이팅 함수라고 함
    def wrapper():
        print('함수 시작')
        original()
        print('함수 끝')
    return wrapper

@add_print_to
def print_hello():
    print("안녕하세요!")

print_hello()


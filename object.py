class User:
    count = 0
    # 클래스 변수: 같은 클래스의 인스턴스들이 서로 공유하는 값
    # 클래스 변수를 설정할 때는 꼭 클래스 이름(변수)를 통해서만 해야함 -> 헷갈릴 소지가 있음.

    def __init__(self, name, email, password):
        # __xx__: 이런 형태를 magic method(특수메소드) 또는 special method 라고 한다.
        # 인스턴스가 생성될 때 자동으로 호출
        self.name = name
        self.email = email
        self.password = password

        User.count += 1

    def __str__(self):
        #던더 메소드: print()함수를 호출할 때 자동으로 실행됨. 던더 str의 return 값이 호출됨.
        return "사용자: {}, 이메일: {}, 비밀번호: *****".format(self.name, self.email)


user1 = User("Young", "young@codeit.kr", "123456")

user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User("Taeho", "taeho@codeit.kr", "123abc")

user4 = User("Lisa", "lisa@codeit.kr", "abc123")

print(user1.email)
print(user2.name)
print(user3.password)
print(user4.email)

print(user1)
print(user2)

print(User.count)


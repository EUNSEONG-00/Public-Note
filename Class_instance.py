class User:
    def say_hello(self):
        # 인사 메세지 출력 메소드(인스턴스 메소드)
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def login(self, my_email, my_password):
        # 로그인 메소드
        if (self.email == my_email and self.password == my_password):
            print("로그인 성공, 환영합니다")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

    def check_name(self, name):
        # 파라미터로 받는 name이 유저의 이름과 같은지 불린으로 리턴하는 메소드
        # 인스턴스 변수와 같은 이름을 갖는 파라미터지만 코드상 문제는 없음
        return self.name == name

# 인스턴스 메소드의 특별한 규칙: 첫 번째 파라미터의 이름은 꼭 self로 쓰기

user1 = User()
user2 = User()
user3 = User()

# 인스턴스 변수: 인스턴스가 각자 개인적으로 갖고 있는 속성

user1.name = "김대휘"
user1.email = "caption@codeit.kr"
user1.password = "12345"

user2.name = "강영훈"
user2.email = "younghoon@codeit.kr"
user2.password = "98765"

user3.name = "최지웅"
user3.email = "jiwoong@codeit.kr"
user3.password = "78945"

print(user1.email)
print(user2.password)

# 파이썬에서 객체의 행동은 함수로 나타냄 -> 메소드를 정의하는 일임
# 메소드의 종류
# 1. 인스턴스 메소드: 인스턴스 변수의 값을 읽거나 설정하는 메소드
# 2. 클래스 메소드: 클래스 변수의 값을 읽거나 설정하는 메소드
# 3. 정적 메소드

User.say_hello(user1)
User.say_hello(user2)
User.say_hello(user3)
user1.say_hello()
user2.say_hello()
user3.say_hello()

User.login(user1, "caption@codeit.kr", "12345")
user1.login("caption@codeit.kr", "12345")

print(user1.check_name("김대휘"))

print(user1.check_name("강영훈"))


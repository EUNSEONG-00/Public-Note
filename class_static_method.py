class User:
    count = 0

    def __init__(self, name, email, password):

        self.name = name
        self.email = email
        self.password = password

        User.count += 1

    def say_hello(self):
        print("안녕하세요! 저는{}입니다!".format(self.name))

    def __str__(self):
        #던더 메소드
        return "사용자: {}, 이메일: {}, 비밀번호: *****".format(self.name, self.email)

    @classmethod
    def number_of_users(cls):
        print("총 유저 수는: {}입니다".format(cls.count))

    # 정적 메소드: is_valid_email 메소드는 파라미터 email_address로 받은 문자열에 @가 있는지 체크
    # 정적 메소드는 인스턴스 메소드의 self, 클래스 메소드의 cls 같은 자동 전달되는 파라미터가 없음
    # 정적 메소드는 아래 코드처럼 인스턴스, 클래스 두 가지 모두를 통해 사용 가능
    @staticmethod
    def is_valid_email(email_address):
        return "@" in email_address

user1 = User("taehosung", "taehosung@codeit.kr", "12345")


print(User.is_valid_email("taehosung"))
print(User.is_valid_email("taehosung@codeit.kr"))

print(user1.is_valid_email("taehosung"))
print(user1.is_valid_email("taehosung@codeit.kr"))

# User 클래스에는 인스턴스 메소드, 클래스 메소드, 정적 메소드가 있습니다.

# 인스턴스 메소드 __str__는 인스턴스 변수인 self.name, self.email을 사용하고,
# 클래스 메소드 number_of_user는 클래스 변수인 cls.count를 사용합니다.
# 하지만 is_valid_email 메소드에선 아무 변수도 사용하고 있지 않네요.
# 인스턴스 변수나 클래스 변수 중 아무것도 사용하지 않을 메소드라면 정적 메소드로 만들면 됩니다.
# 그러니까 어떤 속성을 다루지 않고, 단지 기능(행동)적인 역할만 하는 메소드를 정의할 때
# 정적 메소드로 정의하면 됩니다.

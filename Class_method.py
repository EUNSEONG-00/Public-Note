class User:
    count = 0
    # 클래스 변수: 같은 클래스의 인스턴스들이 서로 공유하는 값
    # 클래스 변수를 설정할 때는 꼭 클래스 이름(변수)를 통해서만 해야함 -> 헷갈릴 소지가 있음.

    def __init__(self, name, email, password):
        # __xx__: 이런 형태를 magic method(특수메소드) 또는 special method 라고 한다.
        # 인스턴스가 생성될 떄 자동으로 호출
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
# 클래스 메소드의 특별한 규칙: 첫 번째 파라미터의 이름은 꼭 cls로 쓴다.
# 인스턴스가 하나도 없을 때에도 사용할 가능성이 있으면 그때는 클래스 메소드를 사용함. 
    def number_of_users(cls):
        print("총 유저 수는: {}입니다.".format(cls.count))
    # 인스턴스 메소드를 사용
    # def number_of_users(self):
    #     print("총 유저 수는: {}입니다.".format(User.count))

user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "abcdef")
user3 = User("서혜린", "hyelin@codeit.kr", "123abc")

# 클래스 메소드 사용
# 클래스로 호출
User.number_of_users()
# 인스턴스로 호출
user1.number_of_users()

# 인스턴스 메소드 사용
# User.number_of_users(user1)
# user1.number_of_users()
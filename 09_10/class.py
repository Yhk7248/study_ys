""" 일반적인 클래스 정의 """


class Person:
    def __init__(self, age, phone_number, address, birth, name):
        self.age = age
        self.phone_number = phone_number
        self.address = address
        self.birth = birth
        self.name = name

    # def print_age(self):

    # def print_name(self):


if __name__ == "__main__":
    # 인스턴스 변수 선언 클래스 초기화
    person = Person(
        age=14,
        phone_number="010-1234-5678",
        address="서울시 송파구 문정동",
        birth="2010-03-29",
        name="홍길동"
    )

    # person.print_age()
    # person.print_name()

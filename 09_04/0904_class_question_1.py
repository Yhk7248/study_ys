"""
클래스 문제 1)
    자동차가 있다. 자동차에는 바퀴, 창문, 썬루프, 문 네 가지가 있다고 할 때
    바퀴를 굴러가게하는 함수, 창문을 여는 함수, 썬루프를 여는 함수, 문을 여는 함수
    네 가지를 멤버 함수로 한 class 를 작성하라.

#####################################################################
def cars(wheels, window, door, sunroof):
    if wheels == 1 and window == 1 and door == 1 and sunroof == 1:
        print("open")
    else:
        print("close")
#####################################################################

FeedBack
    1. 객체가 정의 되지 않았다.
    2. 조건문이 and 로 연결 되어 있다. (and 조건은 모두 True 일 때만 동작.)

"""

class Car:
    def __init__(self, wheel, window, sun_roof, door):
        self.wheel = wheel
        self.window = window
        self.sun_roof = sun_roof
        self.door = door

    def open_door(self):
        print("문이 열렸습니다.")
        self.door = True

    def open_sun_roof(self):
        print("썬루프가 열렸습니다.")
        self.sun_roof = True

    def open_window(self):
        print("창문이 열렸습니다.")
        self.window = True

    def rolling_wheel(self):
        print("바퀴가 굴러가고 있습니다.")
        self.wheel = True


if __name__ == '__main__':
    younghyun_car = Car(wheel=False, window=False, sun_roof=False, door=False)
    younghyun_car.rolling_wheel()
    younghyun_car.open_window()
    younghyun_car.open_door()
    younghyun_car.open_sun_roof()

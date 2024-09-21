"""
클래스 문제 2)
    컴퓨터가 있다. 컴퓨터에는 cpu, ram, monitor 세가지가 있다.
    세 가지 함수가 있다. 컴퓨터의 동작에는 cpu를 구동시키는 함수, ram 을 비우는 함수, monitor가 켜졌는지 꺼졌는지 알 수 있는 함수.
##########################################################
class computer:
    def __init__(self, cpu, ram, moniter):
        self.cpu = cpu
        self.ram = ram
        self.moniter = moniter

    def cpu_r(self):
        if self.cpu:
            print("동작되었습니다.")

    def ram_e(self):
        if not self.ram:
            print("ram이 지워졌습니다.")

    def moniter_o(self):
        if self.moniter:
            print("power On")
        else:
            print("power Off")
###########################################################
FeedBack
    1. 전체적인 구조는 나쁘지 않음.
    2. moniter_o 함수의 내부에는 else 처리까지 하였지만 다른 함수들은 처리하지 않음 (일관적인 것이 좋음)
    3. 함수의 이름에서 명확한 함수의 동작을 알 수 없음. 네이밍을 조금 더 자세하게.
    4. 스네이크 케이스, 카멜케이스에 대해 보충이 필요해보임.
"""


class Computer:
    def __init__(self, cpu, ram, monitor):
        self.cpu = cpu
        self.ram = ram
        self.monitor = monitor

    def run_cpu(self):
        if self.cpu:
            print("cpu 가 이미 구동중입니다.")
        else:
            print("cpu 를 동작시킵니다.")
            self.cpu = True

    def clear_ram(self):
        print("ram 을 비웁니다.")
        self.ram = 0

    def is_using_monitor(self):
        if self.monitor:
            print("모니터 켜져있습니다.")
        else:
            print("모니터가 꺼져있습니다.")


if __name__ == "__main__":
    my_computer = Computer(cpu=False, ram=100, monitor=True)
    my_computer.is_using_monitor()

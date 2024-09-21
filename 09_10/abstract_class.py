""" 인터페이스 정의 """

from abc import ABC, abstractmethod


# abstract class (interface)
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

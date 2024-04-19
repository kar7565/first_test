Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 2번 문제
>>> class Car :
	def __init__(self, name = "", speed = 0) :
		self.color = color
		self.speed = speed
		
	def upSpeed(self, value) :
		self.speed+= value

>>> # 4번 문제
>>> class Horse:
    speed = 0

    def __init__(self):
        self.speed = 50

        
>>> horse = Horse()
>>> print(horse.speed)
50
>>> # 6번 문제
>>> class Car:
    def method(self):
        print("슈퍼 클래스")

        
>>> class Sedan(Car):
    def method(self):
        print("서브 클래스")

        
>>> myCar = Car()
>>> mySedan = Sedan()
>>> myCar.method()
슈퍼 클래스
>>> mySedan.method()
서브 클래스
>>> # 답: 3번
>>> 
>>> # 7번 문제
>>> class Car:
    speed = 0

    def upSpeed(self, value) :
        self.speed = self.speed + value

        
>>> class RVCar(Car) :
    seatNum = 0

    def getSeatNum(self) :
        return self.seatNum

>>> 

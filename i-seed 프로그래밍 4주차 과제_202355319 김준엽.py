Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 5번 문제
>>> ss = 'Python'
>>> for i in range(0, 6) :
	print(ss[i]+'$', end = '')

	
P$y$t$h$o$n$
>>> # 답: (1) for, (2) 6, (3) ss[i]
>>> 
>>> # 11번 문제
>>> bb = '파이썬 ### CookBook $$$ @@@ 열공중 1234'
>>> import re
>>> answer = re.sub(r'[^a-zA-Z가-힣]', '', bb)
>>> print(answer)
파이썬CookBook열공중
>>> 
>>> # 9번 문제
>>> inStr, outStr = "Python", ""
>>> StrLen = len(inStr)
>>> for i in range(0, StrLen) :
	outStr += inStr[StrLen-1-i]

	
>>> print(outStr)
nohtyP
>>> # 답: inStr[StrLen-1-i]
>>> 
>>> # 13   심화문제
>>> import turtle
>>> import math
>>> screen = turtle.Screen()
>>> screen.setup(width=500, height=500)
>>> screen.bgcolor("white")
>>> 
>>> t = turtle.Turtle()
>>> t.speed(0)
>>> t.penup()
>>> t.goto(200, 0)
>>> t.pendown()
>>> text = input("나선형으로 쓸 문자열을 입력하세요: ")
나선형으로 쓸 문자열을 입력하세요: 나 보기가 역겨워 가실 때에는 말없이 고이 보내 드리오리다 나 보기가 역겨워 가실 때에는 죽어도 아니 눈물 흘리오리다 날 떠나 행복한지 이젠 그대 아닌지 그댈 바라보며 살아온 내가 그녀 뒤에 가렸는지 사랑 그 아픔이 너무커 숨을 쉴 수가 없어 그대 행복하길 빌어줄께요 내 영혼으로 빌어줄께요 나 보기가 역겨워 가실 때에는 말없이 고이 보내 드리오리다 영변에 약산 진달래꽃 아름따다 가실 길에 뿌리오리다 가시는 걸음 놓인 그 꽃을 사뿐히 즈려 밟고 가시옵소서 나 보기가 역겨워 가실 때에는 죽어도 아니 눈물 흘리오리다
>>> angle = 360 * 2 / len(text)
>>> radius = 200
>>> for i in range(len(text)):
    t.write(text[i], align="center", font=("Arial", 20))
    angle_rad = math.radians(i * angle)
    x = radius * math.cos(angle_rad)
    y = radius * math.sin(angle_rad)
    t.goto(x, y)

    
>>> turtle.done()
>>> 
>>> # 3번 문제
>>> def plus(v1, v2, v3):
	result = 0
	result = v1 + v2 + v3
	return result

>>> hap = plus(100, 200, 300)
>>> print(hap)
600
>>> 
>>> # 4번 문제
>>> def f1():
	print(var)

	
>>> def f2() :
	var = 10
	print(var)

	
>>> var = 100
>>> f1()
100
>>> f2()
10
>>> 
>>> # 11번 문제
>>> def addNumber(num):
	if num == 1 :
		return 1
	else :
		return num + addNumber(num - 1)

	
>>> print(addNumber(100))
5050
>>> 
>>> # 8번 문제
>>> def myFunc(p1=2, p2=2, p3=2):
	ret = p1 + p2 + p3
	return ret

>>> print("매개변수 없이 호출⇒", myFunc())
매개변수 없이 호출⇒ 6
>>> print("매개변수가 1개로 호출 =>", myFunc(1))
매개변수가 1개로 호출 => 5
>>> print("매개변수가 2개로 호출", myFunc(1, 2))
매개변수가 2개로 호출 5
>>> print("매개변수가 3개로 호출 ==> ", myFunc(1, 2, 3))
매개변수가 3개로 호출 ==>  6
>>> #답: p1=2, p2=2, p3=2, -> 6, 6, 6, 6 이 나오려면 다른 조건문이 추가되어야 가능하지 않을까 생각됩니다.
>>> 

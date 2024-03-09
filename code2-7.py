Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> import random
>>> def screenLeftClick(x, y) :
	global r, g, b
	turtle.pencolor((r, g, b))
	turtle.pendown()
	turtle.goto(x, y)

	
>>> def screenRightClick(x, y) :
	turtle.penup()
	turtle.goto(x, y)

	
>>> def screenMidClick(x, y) :
	global r, g, b
	tSize = random.randrange(1, 10)
	turtle.shapesize(tSize)
	r = random.random()
	g = random.random()
	b = random.random()

	
>>> pSize = 10
>>> r, g, b = 0.0, 0.0, 0.0
>>> 
>>> turtle.title('거북이로 그림 그리기')
>>> turtle.shape('turtle')
>>> turtle.pensize(pSize)
>>> 
>>> turtle.onscreenclick(screenLeftClick, 1)
>>> turtle.onscreenclick(screenMidClick, 2)
>>> turtle.onscreenclick(screenRightClick, 3)
>>> 
>>> turtle.done()

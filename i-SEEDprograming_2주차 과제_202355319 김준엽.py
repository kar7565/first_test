Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 연습문제 1
>>> print("100"), print(100), print(50+50), print("50+50")
100
100
100
50+50
(None, None, None, None)
>>> # 답: 4번
>>> 
>>> # 연습문제 2
>>> print('%d / %d = %d' % (5, 10, 5/10))
5 / 10 = 0
>>> #답: 3번
>>> 
>>> #연습문제 3
>>> print("%04d" % 876), print("%5s" % "CookBook"), print("%1.1f % 123.45")
0876
CookBook
%1.1f % 123.45
(None, None, None)
>>> 
>>> #연습문제 4
>>> print("{2:d} {0:d} {1:d}".format(111, 222, 333))
333 111 222
>>> #답: 3번
>>> 
>>> # 연습문제 11
>>> # (1)
>>> a = int("1011", 2)
>>> print(a)
11
>>> # (2)
>>> b = int("1A", 16)
>>> print(b)
26
>>> 
>>> #연습문제 13
>>> #(1)
>>> int('1002', 2)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int('1002', 2)
ValueError: invalid literal for int() with base 2: '1002'
>>> #(2)
>>> int('1008', 8)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int('1008', 8)
ValueError: invalid literal for int() with base 8: '1008'
>>> #(3)
>>> int('AAFG', 16)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int('AAFG', 16)
ValueError: invalid literal for int() with base 16: 'AAFG'
>>> #답: (1) 2진수는 0과 1로만 구성되기 때문에 2는 포함될 수 없다. (2) 8진수는 0~7까지의 숫자만 사용한다. 8은 포함될 수 없다. (3) 16진수는 0~9, A~F만을 사용한다. G는 포함될 수 없다.
>>> 
>>> #연습문제 15
>>> num = 12345678
>>> #답
>>> hex_num = hex(num)
>>> oct_num = oct(num)
>>> bin_num = bin(num)
>>> # 출력
>>> print("10진수 ==> ", num)
10진수 ==>  12345678
>>> print("16진수 ==> ", hex_num)
16진수 ==>  0xbc614e
>>> print("8진수 ==> ", oct_num)
8진수 ==>  0o57060516
>>> print("2진수 ==> ", bin_num)
2진수 ==>  0b101111000110000101001110
>>> 

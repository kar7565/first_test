Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 1번 문제
>>> # 입력과 관련된 함수: input(), read(), readline(), readlines()
>>> # 출력과 관련된 함수: print(), write(), writeline()
>>> 
>>> # 2번 문제
>>> # (1) A: 파일 열기, (2) C: 파일 읽기, (3) B: 파일 쓰기, (4) D: 파일 닫기
>>> # 답: 1번(A→C→B→D)
>>> 
>>> # 3번 문제
>>> # 답: 1, 6번
>>> # (1): 열기 모드를 생략하면 쓰기 모드가 기본으로 설정됨, (6): tb는 존재하지 않는 모드이다.
>>> 
>>> # 4번 문제
>>> # inFp = open("C:/Temp/data1.txt", "r")
>>> # inStr = inFp.readline()
>>> # print(inStr, end = "")
>>> # inFp.close()
>>> 
>>> #6번 문제
>>> # inFp = open("C:/Windows/win.ini", "r")
>>> # outFp = open("C:/Temp/data3.txt", "w")
>>> 
>>> # inList = inFp.readlines()
>>> # for inStr in inList:
>>> #   outFp.write(inStr)
>>> 
>>> # inFp.close()
>>> # outFp.close()
>>> 

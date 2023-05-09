#--------------------------------------
# 함수를 불러서 사용한다 --> 함수 호출
# 함수에 return 이 있는 경우 변수에 바인딩에 사용할 수 있다.
#--------------------------------------
#PycharmProjects.pythonProject.venv.test.lec04_파일입출력함수
#--------------------------------------
# 1. from   : 패키지명.모듈명
# 2. import : 클래스명, 모듈명, 함수명
# 3. 모듈명은 일반적으로 별칭(alias)를 사용한다
# 4. import 함수명1, 함수명2 이 길어지면 import 모듈명으로 한다
#
#       ex) from 패키지명.모듈명 import 클래스명
#       ex) from 패키지명.모듈명 import 함수명1, 함수명2 ...
#       ex) from 패키지명       import 모듈명 as 별명
#---------------------------------------------------------
from test.lec04_파일입출력함수 import CacClass
from test.lec04_파일입출력함수 import MemberClass
from test.lec04_파일입출력함수 import myprint, uprint


a= CacClass.add(1,5)
print(a)
print(CacClass.add(1,5))

MemberClass.add("kim",30)
myprint(5)
uprint(5)

#--------------------------------------
from test import lec04_파일입출력함수, lec04_파일입출력함수 as lkh

#--------------------------------------
lec04_파일입출력함수.uprint(55)
lec04_파일입출력함수.MemberClass.add("park", 29)  #----비추

#--------------------------------------
#--------------------------------------
lkh.uprint(55)

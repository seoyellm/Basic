#--------------------------------------
# 패키지   모듈     클래스   함수
# 폴더   .py파일   class   def
#--------------------------------------
# 함수   : 공통의 기능을 정의해 놓음
# 클래스 : 함수들을 관리하기 위한 큰 틀

class CacClass :
    def add(n1,n2):
        res = n1 + n2
        return res

class MemberClass:
    def add(name, age):
        print(name,"저장")

def myprint(n):
    print(n,"입력되었습니다")

def uprint(n):
    print(n,"입력되었습니다2222")
#--------------------------------------
# 함수를 불러서 사용한다 --> 함수 호출
# 함수에 return 이 있는 경우 변수에 바인딩에 사용할 수 있다.
#--------------------------------------
a= CacClass.add(1,5)
print(a)
print(CacClass.add(1,5))

MemberClass.add("kim",30)

myprint(5)
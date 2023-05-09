# for 조건식 :
#     반복실행문
# while(조건식) :
#     반복실행문
#-----------------------------------------
# do :              -->파이썬에는 없음
#     반복실행문
# while(조건식)
#-----------------------------------------
emp = [7788,7799,7800]
# empno = emp[0]
# empno = emp[1]
# empno = emp[2]

for empno in emp:  #emp 안에 있는 것 중에 하나만 꺼내어 empno에 담아라
    print(empno)

#-----------------------------------------
# range(시작번호 이상, 끝번호 미만, 증감분)
# 끝번호 미만*******
# 증감분 기본 값 : 1
#-----------------------------------------
print ( list (range(1,6) ) ) #[1, 2, 3, 4, 5]
#list : 값을 담고 있는 객체
print ( list (range(1,11,2) ) ) #[1, 3, 5, 7, 9]
print ( list (range(10,0,-1) ) ) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#for 문 range 이용 1~10 출력
for i in range(1,11):
    print(i, end="\t")

print()

#------------중첩 for문
for i in range(100,600,100):
    print(i)
    for j in range (1,4):
        print(j, end="\t")
    print()

#----------------구구단
dan = 2
gob = 3
print(dan,"*",gob,"=", dan*gob)

# 2단
# 2*1=2 2*2=4 ..... 2*9=18
# 3단
# 3*1=3 3*2=6 ..... 3*9=27


for dan in range(2,10):
    print()
    print(dan,"단")
    for gob in range(1,10):
        print(dan,"*",gob,"=",dan*gob, end="\t")
    print()


#2,4,6,8단 *5
for dan in range(2,9,2):
    print()
    print(dan,"단")
    for gob in range(1,6):
        print(dan,"*",gob,"=",dan*gob, end="\t")
    print()

#9,7,5,3단  * 9 *8 *7 *6 *5
for dan in range(9,2,-2):
    print()
    print(dan,"단")
    for gob in range(9,4,-1):
        print(dan,"*",gob,"=",dan*gob, end="\t")
    print()


#------------중첩 for 별찍기

# *
# ***
# *****
for g in range(2,-1, -1):
    print(" "*g, end="")
    for i in range(1, 6, 2):
        print("*" * i)

print()

#   *
#  ***
# *****
for i in range(3):
    print(' ' * (2-i), end='')
    print((i * 2 + 1) * '*')


for n in range(3):
    for space in range(2-n):
        print(' ', end='')
    for star in range(1+n*2):
        print('*', end='')
    print()

print()


# ****
#  ***
#   **
#    *
for j in range(1,5):
    for k in range(1,5):
        #if j=1  k=1 2 3 4
        if j <= k :
            print("*", end ="")
        else :
            print(" ",end = "")
    print()

print()

#    *
#   **
#  ***
# ****
for j in range(1,5): #행
    for k in range(4,0,-1): #칸
        #if j=1  k=4 3 2 1
        if j < k :
            print(" ", end ="")
        else :
            print("*",end = "")
    print()

print()


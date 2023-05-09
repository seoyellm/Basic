num = 5
while(num < 10) :
    print("그렇다" , num)
    num=num+1

# 그렇다 5
# 그렇다 6
# 그렇다 7
# 그렇다 8
# 그렇다 9

#while문으로 구구단
dan=2

while(dan<10):
    print(dan,"단")
    gob = 1
    while(gob<10):
        print(dan,"*",gob,"=",dan*gob)
        gob+=1
    dan += 1
    print()
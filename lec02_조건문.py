# if 조건식:
#     실행1
# elif 조건식:
#     실행2
# elif 조건식:
#     실행3
# else :
#     실행4

#----------------------------------------
#인덴테이션(들여쓰기) 주의-->Python

#90이상이면 A   80이상이면 B    아니면 C
score = 80

if score >=90:
    print("A")
elif score >=80:
    print("B")
else:
    print("C")

#중첩 if
#90이상이면서 성별이 남성이면 1 여성이면 2
#80이상이면서 성별이 남성이면 11 여성이면 22
#아니면 0

score = 80
gen = "남"

#1)중첩 if
if score >=90:
    if gen == "남" :
        print("1")
    else:
        print("2")
elif score >=80:
    if gen == "남":
        print("11")
    else:
        print("22")
else:
    print("0")

#2)and로 연결
if score >=90 and gen == "남" :
        print("1")
if score >= 90 and gen == "여":
            print("2")
elif score >=80 and gen == "남":
        print("11")
elif score >=80 and gen == "여":
        print("22")
else:
    print("0")


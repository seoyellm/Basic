addr_list = [ {"name":"홍길동",  "tel":"010"},
              {"name":"홍길동",  "tel":"555"},
              {"name":"아무개",  "tel":"111"}
            ]
def addr_file_write():
    with open(file="C:\\AI\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\address.txt", mode='w', encoding = "utf-8") as f:
        f.write("name   tel\n")
        for addr_dic in addr_list:
            temp =addr_dic["name"]+"\t"+addr_dic["tel"]+"\n"
            f.write(temp)

def menu_print():
    print("====================================")
    print("1.입력", end="\t")
    print("2.조회", end="\t")
    print("3.전체", end="\t")
    print("4.삭제", end="\t")
    print("5.수정", end="\t")
    print("6.종료")
    print("====================================")

def add_input():
    name = input("이름 : ")
    tel = input("전화번호 : ")
    addr_list.append({"name": name, "tel": tel})

def add_search_all():
    print("총", len(addr_list), "건")
    for addr_dic in addr_list:
        print(addr_dic["name"], "\t", addr_dic["tel"])

def add_search() :
    fd_name = input("찾을 이름 : ")
    search_list = []
    for fd in addr_list:
        if fd["name"] == fd_name:
            search_list.append(fd["tel"])
    if len(search_list) <= 0:
        print("찾는 이름이 없습니다")
    else:
        for search_tel in search_list:
            print(search_tel)

def add_del():
    isdel = False
    search_tel = input("삭제 전화번호:")
    for i, addr_dic in enumerate(addr_list):
        if addr_dic["tel"] == search_tel:
            yn = input("정말 삭제하시겠습니까?(Y/N)")
            if yn.upper() == "Y":
                addr_list.pop(i)
                isdel = True

    if isdel == True:
        print("삭제되었습니다")
    elif isdel == False:
        print("검색 결과가 없습니다")

def add_update():
    isud = False
    search_tel = input("수정할 대상의 전화번호 : ")
    for addr_dic in addr_list:
        if addr_dic["tel"] == search_tel:
            ud_tel = input("수정 전화번호 : ")
            addr_dic["tel"] = ud_tel
            print(addr_dic)
            isud = True

    if isud == True:
        print("수정되었습니다")
    elif isud == False:
        print("검색 결과가 없습니다")


#addr_list = []

while(1):
    menu_print()

    cmd = input("명령어입력 : ")

    if cmd=="1" :
        add_input()

    elif cmd == "2":
        add_search()

    elif cmd=="3":
        add_search_all()

    elif cmd =="4":
        add_del()

    elif cmd == "5":
        add_update()

    elif cmd == "6":
        break

#----------------------------------------------------
def run():
    while (1):
        menu_print()

        cmd = input("명령어입력 : ")

        if cmd == "1":
            add_input()
            addr_file_write()

        elif cmd == "2":
            add_search()

        elif cmd == "3":
            add_search_all()

        elif cmd == "4":
            add_del()
            addr_file_write()

        elif cmd == "5":
            add_update()
            addr_file_write()

        elif cmd == "6":
            break

#__ : 특수기능 내부 함수
#현재 파일에서 직접 돌렸다, 다른 모듈에서도 호출될 경우 어디에서 실행되는 것인지 알고자 할때 사용
if __name__ == "__main__":
    print("직접돌려보기")
    run()


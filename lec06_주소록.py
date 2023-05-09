def menu_print():
    print("====================================")
    print("1.입력", end="\t")
    print("2.조회", end="\t")
    print("3.전체", end="\t")
    print("4.삭제", end="\t")
    print("5.수정", end="\t")
    print("6.종료")
    print("====================================")


#addr_list = []
addr_list = [ {"name":"홍길동",  "tel":"010"},
              {"name":"홍길동",  "tel":"555"},
              {"name":"아무개",  "tel":"111"}
            ]
while(1):
    menu_print()
    # 입력명령받기
    cmd = input("명령어입력 : ")

    if cmd=="6" :
        break

    elif cmd=="1" :
        name = input("이름 : ")
        tel = input("전화번호 : ")
        addr_list.append({"name":name,"tel":tel})

    elif cmd=="3":
        print("총",len(addr_list),"건")
        for addr_dic in addr_list:
            print(addr_dic["name"],"\t",addr_dic["tel"] )

    elif cmd=="2":
        fd_name = input("찾을 이름 : ")
        search_list = []
        for fd in addr_list:
            if fd["name"] == fd_name:
                search_list .append(fd["tel"])
        if len(search_list )<=0:
            print("찾는 이름이 없습니다")
        else :
            for search_tel in search_list  :
             print(search_tel)

    elif cmd =="4":
        search_tel= input("삭제할 전화번호 :")
        #--1)
        for addr_dic  in addr_list:
            if addr_dic["tel"] == search_tel:
                # del dl["tel"]
                addr_list.remove(addr_dic )
                print("삭제되었습니다")
        #--2)
        # for addr_dic in addr_list:
        #     if addr_dic["tel"] == search_tel:
        #         addr_list.remove(addr_dic)

        #--3)
        # -----------------------------------------------------------------------------
        # addr_list = [1, 2 , 3 ,'AA', {"name":"홍길동", "tel":123}]
        # # addr_list.pop(0)        #index삭제, 그냥은 맨뒤삭제
        # # addr_list.remove( {"name":"홍길동", "tel":123} )  #AA라는값삭제
        # # del addr_list[0]
        #
        # for i, val in enumerate(addr_list): #enumerate() : 값이 몇번재 값인지 알려줌
                                              # for 몇번째인지 알려줄 변수, 변수(값) in enumerate(list)
        #     print(i, val)
        #     if val == "AA":
        #         del addr_list[i]
        # print(addr_list)
        # -----------------------------------------------------------------------------
        # for i, addr_dic in enumerate(addr_list):  # enumerate() : 값이 몇번재 값인지 알려줌
        #     if addr_dic["tel"] == search_tel:
        #         addr_list.pop(i)

        #--4)
        # for i in range(len(addr_list)):
        #     if addr_list[i]["tel"] == del_tel:
        #         addr_list.pop[i]["tel"]

        # --5)
        # isdel = False
        # search_tel = input("삭제 전화번호:")
        # for i, addr_dic in enumerate(addr_list):
        #     if addr_dic["tel"] == search_tel:
        #         yn = input("정말 삭제하시겠습니까?(Y/N)")
        #         if yn.upper() == "Y":
        #             # del addr_list[i]
        #             addr_list.pop(i)
        #             isdel = True
        #
        # if isdel == True:
        #     print("삭제되었습니다")
        # elif isdel == False:
        #     print("검색 결과가 없습니다")

    elif cmd == "5":
            isud = False
            search_tel=input("수정할 대상의 전화번호 : ")
            for addr_dic  in addr_list:
                if addr_dic["tel"] == search_tel:
                    ud_tel = input("수정 전화번호 : ")
                    addr_dic["tel"] = ud_tel
                    print(addr_dic)
                    isud = True

            if isud == True:
                print("수정되었습니다")
            elif isud == False:
                print("검색 결과가 없습니다")





# pip install cx_Oracle

import cx_Oracle

# with cx_Oracle.connect("ai","0000", "localhost:1521/XE") as conn:
#     if bool(conn):
#         print("연결성공")
#     else:
#         print("연결실패")
#
#     with conn.cursor() as cur:
#         cur.execute("select * from emp")
#         for row in cur:
#             print(list(row))
            # cur.close()
#conn.close()

#------------------------------------------------------------
#연결
#------------------------------------------------------------
conn= cx_Oracle.connect("ai","0000", "localhost:1521/XE")
if bool(conn):
    print("연결성공")
else:
    print("연결실패")

#------------------------------------------------------------
# SELECT
#------------------------------------------------------------
# cur=conn.cursor()
# cur.execute("select * from addr")
# for row in cur:
#     print(list(row))
# cur.close()
# conn.close()

conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
sql = "select * from addr where seq = :1 or seq = :2"
cur = conn.cursor()
cur.execute(sql, [5, 1])
for row in cur:
    print( list(row)  )
cur.close()
conn.close()

#--------------------------------------------------
# UPDATE
# update addr set name='홍길순', tel='999' where seq=1
#--------------------------------------------------
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "update addr set name=:1, tel=:2 where seq=:3"
# cur = conn.cursor()
# cur.execute(sql, ['홍길순', '999', 1])
# conn.commit()
# cur.close()
# conn.close()

#------------------------------------------------------------
# INSERT : 1 row
# INSERT INTO ADDR VALUES(ADDR_SEQ.NEXTVAL,'홍길동', '000')
#------------------------------------------------------------
#--1)
# conn= cx_Oracle.connect("ai","0000", "localhost:1521/XE")
# sql ="INSERT INTO ADDR VALUES(ADDR_SEQ.NEXTVAL, :1, :2)" # :1,:2 -->받아야 할 값 1,2
# cur= conn.cursor()
# cur.execute(sql, ['아무개','555']) #값 두개를 넣을 때는 리스트로 넣어야 함
# cur.execute(sql, ['함소영','2525'])
# conn.commit()
# cur.close()
# conn.close()

#--2)
# conn= cx_Oracle.connect("ai","0000", "localhost:1521/XE")
# #sql ="INSERT INTO ADDR VALUES(ADDR_SEQ.NEXTVAL, :1, :2)" # :1,:2 -->받아야 할 값 1,2
# sql ="INSERT INTO ADDR VALUES(ADDR_SEQ.NEXTVAL, :vnm, :vtel)" #--> 변수로 받아도 됨
# cur= conn.cursor()
# vnm="나변수"
# vtel="999"
# cur.execute(sql, [vnm,vtel])
# conn.commit()
# cur.close()
# conn.close()

#--3)
# conn= cx_Oracle.connect("ai","0000", "localhost:1521/XE")
# sql ="INSERT INTO ADDR VALUES(ADDR_SEQ.NEXTVAL, :vnm, :vtel)"
# cur= conn.cursor()
# cur.execute(sql, {"vnm":"나변수2","vtel":"8989"}) #딕셔너리로 삽입 가능
# conn.commit()
# cur.close()
# conn.close()

#------------------------------------------------------------
# INSERT : multi rows
#------------------------------------------------------------
#--1)
# datas = [{"vnm":"나이름1","vtel":"111"},
#          {"vnm":"나이름2","vtel":"222"},
#          {"vnm":"나이름3","vtel":"333"}
#          ]
#
# conn= cx_Oracle.connect("ai","0000", "localhost:1521/XE")
# sql ="INSERT INTO ADDR VALUES(ADDR_SEQ.NEXTVAL, :vnm, :vtel)"
# cur= conn.cursor()
# cur.executemany(sql, datas) #딕셔너리로 삽입 가능
# conn.commit()
# cur.close()
# conn.close()


#--2)
# datas = [["리스트1","6666"],
#          ["리스트2","8888"],
#          ["리스트3","9999"]
#          ]
#
# conn= cx_Oracle.connect("ai","0000", "localhost:1521/XE")
# sql ="INSERT INTO ADDR VALUES(ADDR_SEQ.NEXTVAL, :1, :2)"
# cur= conn.cursor()
# cur.executemany(sql, datas) #딕셔너리로 삽입 가능
# conn.commit()
# cur.close()
# conn.close()

#------------------------------------------------------------
# DELETE
# delete from addr where name like '%나이름%' or name like '%리스트%';
#------------------------------------------------------------
# conn= cx_Oracle.connect("ai","0000", "localhost:1521/XE")
# sql ="delete from addr where name like :1 or name like :2"
# cur= conn.cursor()
# cur.execute(sql, ['%나이름%','%리스트%'])
# conn.commit()
# cur.close()
# conn.close()


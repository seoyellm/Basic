#NoSQL : 빅데이터 다루는 DB, HBase, Mongo   ->면접시 사용해보지는 않았지만 알고는 있다고 대답
#   --> 파일로 저장, JOB 스케줄러 관리(파일 분산 처리)
#   --> HADOOP(HDFS) : 분산 파일 서버(고가용 서버)
#   --> DFS
#RDB : orcle, maia, MS-SQL ->2G
#FDB(파일)
#MDB(메모리)

#스트림(stream) : 데이터가 이동되는 경로

#----------------------------------------------------------
# 1. 파일 생성
#----------------------------------------------------------
# open(파일경로, 모드)
# 모드 : r(읽기) w(쓰기) a(추가)
# 리눅스&유닉스(슬러시)  : /etc/guest/aa.txt
# 윈도우(역슬러시)      : C:\aaa\bb.txt
# 파이썬 프로그래밍     :  C:\\aaa\\bb.txt   or     C:/aaa/bb.txt

f = open(file="C:\\Users\\ASIA\PycharmProjects\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\memo_ansi.txt"
         , mode='r')
f.close()

#----------------------------------------------------------
#파일 읽기/쓰기
#읽기
#ANSI   ASCII
#CP949  UTF-8
#----------------------------------------------------------
#readline()     : 라인 1줄
#----------------------------------------------------------
f = open(file="C:\\Users\\ASIA\PycharmProjects\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\memo_ansi.txt"
         , mode='r')
txt=f.readline()
print(txt)
f.close()

f = open(file="C:\\Users\\ASIA\PycharmProjects\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\memo_utf8.txt"
         , mode='r'
         ,encoding="utf-8")
txt=f.readline()
print(txt)
f.close()


f = open(file="C:\\Users\\ASIA\PycharmProjects\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\memo_utf8.txt"
         , mode='r'
         ,encoding="utf-8")

while(True): #조건이 만족하면 while 가동
    txt=f.readline()
    if not txt: #txt에 더이상 읽을 것이 없으면
        break
    print(txt, end="")
f.close()

print("\n","--"*40)
#----------------------------------------------------------
# read(), readlines()   :전체
# 리스트로 반환
#----------------------------------------------------------
f = open(file="C:\\Users\\ASIA\PycharmProjects\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\memo_utf8.txt"
         , mode='r'
         ,encoding="utf-8")

txt_list =f.readlines() #['동해물과 \n', '백두산이 \n', '마르고 닳도록']
for txt in txt_list:
    txt=txt.strip() #공백제거&개행(줄바꿈)제거
    print(txt, end="")
f.close()

print("\n","--"*40)

f = open(file="C:\\Users\\ASIA\PycharmProjects\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\memo_utf8.txt"
         , mode='r'
         ,encoding="utf-8")

txts = f.read()
print(txts)
f.close()
#----------------------------------------------------------
# with open() as f : 들여쓰기 라인이 모두 실행 되면 자동으로 close()
#----------------------------------------------------------
with open(file="C:\\Users\\ASIA\PycharmProjects\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\memo_utf8.txt"
         , mode='r'
         ,encoding="utf-8") as f:
    txts = f.read()
    print(txts)
#----------------------------------------------------------
#파일쓰기
#with open(file="파일경로", mode='w') as f :
with open("C:\\Users\\ASIA\\PycharmProjects\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\memo_write.txt",mode='w') as f :
    f.write(str(1)+"\n")
    f.write("2\n")
print("===done===")


with open(file="C:\\Users\\ASIA\\PycharmProjects\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\memo_write.txt",mode='w') as f:
    for i in range(1, 11):
        f.write(str(i) + "\n")
print("===done===")

#----------------------------------------------------------
#파일 복사(copy)
#memo_utf8.txt 파일을 memo_write.txt에 복사
fr=open(file="C:\\Users\\ASIA\\PycharmProjects\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\memo_utf8.txt",encoding='utf-8',mode='r')
fw=open(file="C:\\Users\\ASIA\\PycharmProjects\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\memo_write.txt",encoding='utf-8',mode='a')


txt_list=fr.readlines()
for txt in txt_list:
    fw.write(txt)
fr.close()
fw.close()

# ----------------------------------------------------------
#파일/디렉토리 관리
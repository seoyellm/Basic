#---------------------------------------------
#파일 복사(copy)
#memo_utf8.txt 파일을 memo_write.txt에 복사
#---------------------------------------------
import datetime as datetime

fr=open(file="C:\\AI\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\memo_utf8.txt"
        ,encoding='utf-8',mode='r')
fw=open(file="C:\\AI\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\memo_utf8.txt"
        ,encoding='utf-8',mode='a')


txt_list=fr.readlines()
for txt in txt_list:
    fw.write(txt)
fr.close()
fw.close()

print("==== copy done====")
with open(file="C:\\AI\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\memo_write.txt"
        , encoding='utf-8',mode='r') as f:
    print(f.read())

#---------------------------------------------
from shutil import copy,copy2,copyfile
#---------------------------------------------
# copy(원본파일경로, 타켓파일경로)
# copy ("/etc/memo/a.txt", "/etc/memo2/b.txt")
# copy2("/etc/memo/a.txt", "/etc/memo2")  --> /etc/memo2/a.txt

orig="C:\\AI\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\memo_utf8.txt"
dest="C:\\AI\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\memo_write.txt"

copyfile(orig,dest)
#---------------------------------------------
# 파일&디렉토리 내장 함수
# 절대 경로(Absulte Path)  : C:\\Users\\ASIA\\PycharmProjects\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test
# 상대 경로(Relative Path) : 상대적으로 내가 위치한 폴더를 기준으로하는 경로
#       .  : 현재폴더
#       .. : 상위폴더
#       /  : 아래
#---------------------------------------------
import os
from os.path import isfile, isdir, join

print(os.getcwd()) # os.getcwd():파일 경로 출력

print(os.listdir("C:\\AI\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test"))
print(os.listdir(os.getcwd())) #현재 위치의 모든 디렉토리의 정보 출력

pwd = os.getcwd()
print(os.listdir(pwd))

print("\n","--"*40)
#---------------------------------------------
#os.listdir(pwd)로 출력되는 디렉토리(폴더)들에 파일 경로 붙이기
for f in os.listdir(pwd):
    print(join (os.getcwd(),f))

print( join ("/aa","\bb.txt"))   #경로 합치기

print("\n","--"*40)

#-----------------------------------------------------------
#os.listdir
# os.isdir()
# os.isfile()
# os.path.join
#-----------------------------------------------------------번외
for f in os.listdir("C:\\") :
    path = join( "C:\\" , f) # join 걸지 않으면 현재 위치에서 파일을 찾음
    if os.path.isdir(path) : #isdir() : 해당 디렉토리 존재 여부
        if f == "AI" :
            subpath = join("C:\\", f)   #C:\\AI
            for sf in os.listdir(subpath):
                fullname = join(subpath, sf)    #C:\\AI\\python38
                if os.path.isdir(fullname):
                    print("------", sf)
                elif os.path.isfile(fullname):
                    print("------", sf)
        else :
            print("[D]", f)
    elif os.path.isfile(path) : #isfile() : 해당 파일 존재 여부
        print("\t", f)

#---------------------------------------------------------------
#from 패키지(폴더)/datetime.py import strftime()
#from datetime import datetime
#datetime.strftime()

#from datetime.datetime import strftime
#strftime(datetime타입, "포맷")

#datetime.datetime.strftime()
#  모듈     클래스   함수
#---------------------------------------------------------------
import datetime as dt

float_mm = os.path.getmtime("C://Setup.log")   #1541654654.456464465
print( type(float_mm),   float_mm)

time_mm = dt.datetime.fromtimestamp(float_mm) #시간형태로 변환
print( type(time_mm),   time_mm)

str_mm =  dt.datetime.strftime(time_mm,  "%Y-%m-%d %H:%M:%S")
print(  type(str_mm),  str_mm )

#datetime.py
#   class date
#   class datetime
#   class datedelta
#   class ...
#---------------------------------------------------------------
for f in os.listdir("C:\\") :
    path = join( "C:\\" , f)

    # ------------------------ 수정날짜 구하기 ---------------------
    float_mm = os.path.getmtime(path)  # 1541654654.456464465
    time_mm  = dt.datetime.fromtimestamp(float_mm)
    str_mm   = dt.datetime.strftime(time_mm, "%Y-%m-%d %H:%M:%S")
    #---------------------------------------------------------------
    if os.path.isdir(path) :
        print(f, "\t\t\t", "파일폴더", "\t\t", str_mm)
    elif os.path.isfile(path) :
        fsize = os.path.getsize(path)   #byte Kbyte
        print(f, "\t\t\t", "텍스트문서", "\t\t", str_mm, "\t\t", fsize/1024, "KB")


#--------------------------------------------------------glob.py
#   /etc/*.txt
#   /etc/*c/a*.log
#---------------------------------------------------------------
import glob

print(glob.glob("C:\\P*"))
print(glob.glob("C:\\P*\\M*"))
print(glob.glob("C:\\AI\\pythonProject\\PycharmProjects\\pythonProject\\venv\\test\\lec*"))

module_list=[]
glist=glob.glob("C:\\AI\\pythonProject\\PycharmProjects\\pythonProject\\venv\test\\lec*")
for f in glist:
    module_list.append(f.split("\\")[-1])
    #module_list.append(f)
print(module_list)

#module_list=glist


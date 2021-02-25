### OS모듈
import os
print(os.access('.',os.W_OK|os.X_OK|os.R_OK))
print(os.environ.get("path"))
print(os.environ.get("systemroot"))
print(os.getcwd())
#print(sys.argv)
print("\n-------파일 입출력-----------\n")
### 파일 입출력

# f = open('c:\\test\\data.txt','r')
# print(f.read())
# f.close()
print("\n-------파일 읽기쓰기-----------\n")
f = open('c:\\test\\data.txt','r')
str = f.read()
print(str)

f.seek(0)
while(1):
    l = f.readline()
    if(l):
        print(l)
    else:
        break
f.seek(0)
ls = f.readlines()
print(ls)
print(ls[3][2])
print(f.tell())
f.close()
print("\n-------구구단출력-----------\n")
# import os
# def m_Write():
#     fo = open('c:\\test\\구구단.txt','w')
#     for x in range(2, 10):
#         fo.write("\n")
#         for y in range(1,10):
#             data = "%2d * %2d = %2d | " %(x,y,(x*y))
#             fo.write(data)
#     fo.close()
# def m_Read():
#     try:
#         f = open('c:\\test\\구구단.txt','r')
#         for row in f :
#             print(row)
#     except IOError as e:
#         print(e)
#     finally:
#         f.close()

# if __name__ == "__main__":
#     m_Write()
#     m_Read()

 print("\n-------과제 : 디렉토리에 파일만들기-----------\n")   

import os
import shutil

def showDir(path)
    print('---------------------------')
    for dirpath,dirnames,filenames in os.walk(path):
        for dirname in dirnames:
            print(os.path.join(dirpath,dirname))


 if __name__ == "__main__":
     filepath = "c:\TEST"
     if os.path.exists(filepath):
         print("지정된 경로에 파일 또는 디렉토리가 존재하지 않음")
         if os.path.isfile(filepath):
             print("파일이 없음")
         if os.path.isdir(filepath):
             print("디렉토리가 존재함")
     else:
         print("존재하지 않음")

    tmpdir = "C:\Test"
    os.mkdir(tmpdir)
    os.makedirs("c:\TEST\python\tmp\mkdir1\mkdir2\mkdir3")
    showDir(tmpdir)

    os.rmdir("c:\TEST\python\tmp\mkdir1\mkdir2\mkdir3")
    showDir(tmpdir)
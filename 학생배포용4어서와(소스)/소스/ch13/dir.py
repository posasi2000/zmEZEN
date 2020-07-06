import os

def calcDirSize(name):
    totalSize = 0 

    if os.path.isfile(name):
        totalSize += os.path.getsize(name) 
    else: 
        fileList = os.listdir(name) 
        # 서브 디렉토리의 용량을 계산하여 모두 합한다.  
        for subDir in fileList:
            totalSize += calcDirSize(name + "\\" + subDir)

    return totalSize

name = input("디렉터리 이름을  입력하시오:")
print(calcDirSize(name))

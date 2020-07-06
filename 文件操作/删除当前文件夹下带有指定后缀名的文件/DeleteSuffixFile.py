# encoding:utf-8
import os
import sys
import os.path
# 获取当前路径


def fileDir():
    path = sys.path[0]
    # 返回路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

# 获取文件后缀名


def suffix(file, *suffixName):
    arr = map(file.endswith, suffixName)
    if True in arr:
        return True
    else:
        return False

# 删除目录下扩展名为 .txt .docx 的文件


def deleteFile():
    targetDir = fileDir()
    for file in os.listdir(targetDir):
        targetFile = os.path.join(targetDir, file)
        if(suffix(file, '.txt', '.docx')):
            os.remove(targetFile)

deleteFile()

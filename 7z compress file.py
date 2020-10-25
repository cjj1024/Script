# coding=utf8

# 批量压缩文件夹中的文件，每个文件都单独压缩，压缩格式为7z

import os

path = os.getcwd()
fileNames = os.listdir(path)

for fileName in fileNames:
    if os.path.isdir(fileName):
        name = fileName
    else:
        fn = fileName.split('.')
        if len(fn) == 1:
            name = fileName
        else:
            name = ''.join(fn[ : -1])
    cmd = '7z a ' + '\"' + name + '.7z' + '\"' + " " + "-pxhq021620" + " " + "-mmt2" + " " + '\"' + fileName + '\"'
    os.system(cmd)

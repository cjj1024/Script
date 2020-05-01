# coding=utf8

# 批量压缩文件夹中的文件，每个文件都单独压缩，压缩格式为7z

import os

path = os.getcwd()
fileNames = os.listdir(path)

for fileName in fileNames:
    fn1, fn2 = fileName.split('.')
    cmd = '7z a ' + '\"' + fn1 + '.7z' + '\"' + " " + '\"' + fileName + '\"'
    print cmd
    os.system(cmd)
# -*- coding:utf-8 -*-
import os
import nltk
from bs4 import BeautifulSoup

# root_dir为要读取文件的根目录
root_dir = r"C:\\Users\\hp\\Desktop\\novels"  #C:\Users\hp\Desktop\novels

# 依次读取根目录下的每一个文件
for file in os.listdir(root_dir):
    file_name = root_dir + "\\" + file
    filein = open(file_name, "rb")
        
    #将html转化为txt,用变量bb来暂时保存转化后的txt文本
    bb = BeautifulSoup(filein).get_text()
    
    
    with open("C:\\Users\\hp\\Desktop\\novels2\\{0}.txt".format(file),"a",encoding="gb18030") as file_handle:   # .txt可以不自己新建,代码会自动新建
        file_handle.write(bb)     #将txt文本依次写入文件夹中
        file_handle.write('\n')    






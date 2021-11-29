import sys
import os

# root_dir为要读取文件的根目录
root_dir = r"C:\\Users\\hp\\Desktop\\1"

# 依次读取根目录下的每一个文件
for file in os.listdir(root_dir):
    file_name = root_dir + "\\" + file
    filein = open(file_name, "r",encoding="utf-8")

    # txt可以不自己新建,代码会自动新建
    with open("C:\\Users\\hp\\Desktop\\txt\\{0}".format(file),"a",encoding="utf-8") as fnew: 
        #对每一行先删除空格，\n等无用的字符，再检查此行是否长度为0
        for line in filein.readlines():                                  
            data=line.strip()
            if len(data)!=0:
                fnew.write(data)






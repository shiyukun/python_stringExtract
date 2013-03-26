'''
Created on Mar 26, 2013

@author: shiyukun
'''
import os
import re
path = "D:\work\mozat-j2me\src"
out_path = "D:\text"
pattern = 'StringResources.get\("(.+?)"\)'
all_text = set([])

def processFile(file_path):
    f = open(file_path)
    line = f.readline()
    while line:
        line = f.readline()
        mm = re.findall(pattern, line)
        if mm:
            for m in mm:
                print line
                print m
                all_text.add(m)
            
    f.close()
def processFolder(folder_path):
    list_file = os.listdir(folder_path)
    for file_name in list_file:
        sub_path = folder_path + "\\" + file_name
        isFolder = os.path.isdir(sub_path)
        if(isFolder == True):
            processFolder(sub_path)
        else:
            print sub_path
            processFile(sub_path)
            
            
processFolder(path)
# processFile("D:\work\mozat-j2me\src\chat\Chat.java")
print all_text
out_file = open("D:\\text", 'w+')
for text in all_text:
    out_file.write(text)
    out_file.write("=\r\n")
out_file.close()
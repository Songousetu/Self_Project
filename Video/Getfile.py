import os, sys
def genDir():
    base = "C:\Sunaoxue\IT_Project/NSM/tuzhuang/Ver/"
    # base = ""
    # i = 1
    for i in range(1,10):
        file_name = base + str(i)
        print (file_name)
        os.mkdir(file_name)
        i=i+1

if __name__ == '__main__':
    genDir()
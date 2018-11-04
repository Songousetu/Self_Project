
# -*- encoding: utf-8 -*-
import os





def renameImage(pathFile, label):
    startNum = 0
    for files in os.listdir(pathFile):
        oldDir = os.path.join(pathFile, files)
        if os.path.isdir(oldDir):
            continue
        filename = os.path.splitext(files)[0]
        filetype = os.path.splitext(files)[1]
        # newDir = os.path.join(pathFile, str(label) + '_' + str(startNum) + filetype)
        newDir = os.path.join(pathFile,  str(startNum) + filetype)
        os.rename(oldDir, newDir)
        startNum += 1
        print(oldDir + ' 重命名为： ' + newDir)


renameImage('C:\\Sunaoxue\\IT_Project\\Pictrure_Big data_V1\\Test\\D4', 4)
'''

def maketxtList(imageFile,pathFile,label):
    fobj=open(pathFile,'a')
    for files in os.listdir(imageFile):
        fobj.write('\n'+'/root/Shirley/Parts/Test/D3/'+files+' '+str(label))
        print(files+' '+str(label)+' 写入成功！')
    fobj.close()
maketxtList('C:\\Sunaoxue\\IT_Project\\Pictrure_Big data_V1\\Test\\D3','C:\\Sunaoxue\\IT_Project\\Pictrure_Big data_V1\\Test\\Train.txt',3)
'''
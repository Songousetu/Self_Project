import os
import os.path
rootdir = "C:/Sunaoxue/IT_Project/warrantysmart/Data/Normal"

file_object = open('train_list_N.txt','w')

for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        print  filename
        file_object.write(rootdir + '/' + filename+ '\n')
file_object.close()



# file_name("C:\Sunaoxue\IT_Project\warrantysmart\Data\Data_Test\train\train_AB")
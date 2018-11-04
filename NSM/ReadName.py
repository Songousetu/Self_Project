# -*- coding:utf-8 -*-

import os

class ImageRename():
    def __init__(self):
        self.path = 'C:\Sunaoxue\IT_Project\NSM\Data/20180717'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)

        i = 0

        for item in filelist:
            # print (item)
            if item.endswith('.JPG') or item.endswith('.jpg') or item.endswith('.PNG') or item.endswith('.png'):
                src = os.path.join(os.path.abspath(self.path), item)
                print (src)
                # dst = os.path.join(os.path.abspath(self.path), item.split('.')[0] +'_V1' + '.JPG')
                dst = os.path.join(os.path.abspath(self.path), item.split('_')[0]  + '.JPG')
                try:
                    os.rename(src, dst)
                except WindowsError:
                    ReName = 'C:\Sunaoxue\IT_Project\NSM\Data/20180717_D/'+ str(i) + '.JPG'
                    os.rename(src, ReName)
                else:
                    print ('Done')


                #print ('converting %s to %s ...' % (src, dst))
                i = i + 1
        #print ('total %d to rename & converted %d jpgs' % (total_num, i))

if __name__ == '__main__':
    newname = ImageRename()
    newname.rename()
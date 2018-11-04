# -*- encoding: utf-8 -*-

from PIL import Image
import os.path
import glob


def convertjpg(jpgfile, outdir, width=360, height=360):# 想要更改的尺寸
    img = Image.open(jpgfile)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    except Exception as e:
        print(e)


for jpgfile in glob.glob("C:\Sunaoxue\IT_Project/NSM\Data/Upload Test/*.JPG"): #待处理图片的文件
    convertjpg(jpgfile, "C:\Sunaoxue\IT_Project/NSM\Data/Upload Test\Small")#处理后图片放入的文件夹

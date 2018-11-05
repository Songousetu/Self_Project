# -*- encoding: utf-8 -*-

from PIL import Image
import os.path
import glob


def convertjpg(jpgfile, outdir, width=640, height=480):# 想要更改的尺寸
    img = Image.open(jpgfile)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    except Exception as e:
        print(e)


for jpgfile in glob.glob("/root/DD/NSM/changesize/Readname/test/*.JPG"): #待处理图片的文件
    convertjpg(jpgfile, "/root/DD/NSM/changesize/Readname/draft")#处理后图片放入的文件夹

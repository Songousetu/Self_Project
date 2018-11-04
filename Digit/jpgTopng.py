# -*- coding:utf-8 -*-
from os.path import splitext
import glob
from PIL import Image


def get_all_file(filename):
    files = glob.glob(filename)
    return files


def to_ather_file(files, type):
    for jpg in files:
        im = Image.open(jpg)
        png = splitext(jpg)[0] + "." + type
        im.save(png)
        print png


if __name__ == "__main__":
    filename = "C:/Sunaoxue/IT_Project/warrantysmart/Data/Train/AB/*.[Jj][Pp][Gg]"
    files = get_all_file(filename)
    to_ather_file(files, "png")
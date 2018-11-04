# coding:utf-8

import inspect

import win32api

import os

from PIL import ImageGrab, Image

import pyHook  # 钩子~

import pythoncom

import pytesseract  # 图像识别文字包

import pyperclip

# 创建一个坐标列表

coordinate = [1, 1, 1, 1]


# 监听键盘事件

def on_mouse_event(event):
    # 获取当前文件路径

    file_ = inspect.getfile(inspect.currentframe())

    dir_path = os.path.abspath(os.path.dirname(file_))

    file_path = dir_path + '\\read.jpg'

    # 监听鼠标事件

    if event.MessageName == 'mouse left down':

        coordinate[0:2] = event.Position

    elif event.MessageName == 'mouse left up':

        coordinate[2:4] = event.Position

        win32api.PostQuitMessage()  # 退出监听循环

        # 截取坐标图片

        pic = ImageGrab.grab(coordinate)

        pic.save(file_path)

        text = pytesseract.image_to_string(Image.open(file_path), lang='chi_sim')  # 识别并返回

        pyperclip.copy(text.replace(' ', ''))  # 将识别内容导入系统剪切板


    return True

    if __name__ == '__main__':

    hm = pyHook.HookManager()  # 创建一个钩子管理对象

    hm.MouseAll = on_mouse_event  # 监听所有鼠标事件

    hm.HookMouse()  # 设定鼠标钩子

    pythoncom.PumpMessages()  # 进入循环，程序一直监听

import cv2
import numpy as np


def erjitidu(bh):#二级梯度评价函数
    qq=0.0
    m,n=bh.shape
    for i in range (2,m-1):
        for j in range (2,n-1):
            gx=(bh[i+1,j-1]+2*bh[i+1,j]+bh[i+1,j+1])-(bh[i-1,j-1]+2*bh[i-1,j]+bh[i-1,j+1])
            gy=(bh[i-1,j+1]+2*bh[i,j+1]+bh[i+1,j+1])-(bh[i-1,j-1]+2*bh[i,j-1]+bh[i+1,j-1])
            qq=qq+gx*gx+gy*gy
    return qq

def laplas(x):#拉普拉斯评价函数
    qq=0.0
    m,n=x.shape
    for i in range (2,m-1):
        for j in range (2,n-1):
            qq=qq+(20*x[i,j]-4*x[i,j-1]-4*x[i,j+1]-4*x[i-1,j]-4*x[i+1,j]-x[i+1,j+1]-x[i+1,j-1]-x[i-1,j-1]-x[i-1,j+1]);
    return qq


def mean(img):
    qq=0.0
    m,n=img.shape
    for i in range (0,m):
        for j in range (0,m):
            qq=qq+img[i,j]
    return qq


def haxisuanfa(img1,img2): #哈希算法比较两幅图像的相似性
    tmp=cv2.resize(img1,(8,8),interpolation=cv2.INTER_CUBIC)
    tmp2=cv2.resize(img2,(8,8),interpolation=cv2.INTER_CUBIC)
    tmp=np.float32(tmp/4.0)
    tmp2=np.float32(tmp2/4.0)
    a,b=tmp.shape
    re=np.zeros((a,b))
    m=mean(tmp)
    n=mean(tmp2)
    me=m/64
    me2=n/64
    #print m,n,me,me2
    #print tmp
    for i in range (0,8):
        for j in range (0,8):
            if tmp[i,j]>me:tmp[i,j]=1
            else:tmp[i,j]=0

        if tmp2[i,j]>me2:tmp2[i,j]=1
        else:tmp2[i,j]=0


        re[i,j]=tmp[i,j]-tmp2[i,j]

    num=0
    #print re
    for i in range (0,8):
        for j in range (0,8):
            if re[i,j]!=0:
                num=num+1
    #print num
    return num






lx=9.0
ly=9.0
pic=cv2.imread('test_09201.jpg')
pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
m,n=pic.shape
m=int(m)
n=int(n)
depth=np.ones((m,n))


pinhole=cv2.imread('pinhole.tif')
pinhole = cv2.cvtColor(pinhole, cv2.COLOR_BGR2GRAY)
allfocus=pic


for num in range (2,32):
    print (num)
    name='img_'+str(num)+'.jpg'
    img=cv2.imread(name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for i in range (int(lx/2)+1,m-int(lx/2)-1,2):
        for j in range (int(ly/2)+1,n-int(ly/2)-1,2):
            aa=allfocus[i-int(lx/2):i+int(lx/2),j-int(ly/2):j+int(ly/2)]
            bb=img[i-int(lx/2):i+int(lx/2),j-int(ly/2):j+int(ly/2)]
            pin=pinhole[i-int(lx/2):i+int(lx/2),j-int(ly/2):j+int(ly/2)]
            pd_forward=erjitidu(aa)
            pd_next=erjitidu(bb)
            pd_f=laplas(aa)
            pd_n=laplas(bb)
            #pd_fh=haxisuanfa(aa,pin)
            #pd_nh=haxisuanfa(bb,pin)
            if pd_forward>pd_next or pd_f>pd_n:
                depth[i-int(lx/2):i+int(lx/2),j-int(ly/2):j+int(ly/2)]=depth[i-int(lx/2):i+int(lx/2),j-int(ly/2):j+int(ly/2)]
                allfocus[i-int(lx/2):i+int(lx/2),j-int(ly/2):j+int(ly/2)]=allfocus[i-int(lx/2):i+int(lx/2),j-int(ly/2):j+int(ly/2)]
            else:
                depth[i-int(lx/2):i+int(lx/2),j-int(ly/2):j+int(ly/2)]=num
                allfocus[i-int(lx/2):i+int(lx/2),j-int(ly/2):j+int(ly/2)]=img[i-int(lx/2):i+int(lx/2),j-int(ly/2):j+int(ly/2)]


cv2.imshow('allfocus',allfocus)
cv2.imshow('depth',depth)
cv2.waitKey(0)



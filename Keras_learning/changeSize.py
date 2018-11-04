from PIL import Image
import os


ImageNames=os.listdir('C:\Sunaoxue\IT_Project\Pictrure_Big data_V1\Test\D4')


for i in range(len(ImageNames)):
    infile = 'C:\Sunaoxue\IT_Project\Pictrure_Big data_V1\Test\D4\\'+str(i)+'.jpg'  #输入图片所在路径
    outfile ='C:\Sunaoxue\IT_Project\Pictrure_Big data_V1\Test\D5\\'+str(i)+'.jpg' #输出图片所在路径
    Image.open(infile).convert('RGB').save(outfile) # convert the image to RGB mode  very important 将图片转化为RGB模式，虽然我不知道为什么，但是没有这一步会报错
    im = Image.open(infile)
    (x, y) = im.size  # read image size
    x_s = 2448  # define standard width
    y_s = 2448  # calc height based on standard width
    out = im.resize((x_s, y_s), Image.ANTIALIAS)  # resize image with high-quality
    out.save(outfile)
    print(str(i+1)+'original size: ', x, y)
    print(str(i+1)+'adjust size: ', x_s, y_s)
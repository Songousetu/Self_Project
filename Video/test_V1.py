import os, sys
from PIL import Image

# open a pipe from a command
#a, b, c = os.popen3("ffmpeg -i test.avi")
a, b, c = os.popen3("C:\Sunaoxue\Tuling/IMG_5886.MOV")
out = c.read()
dp = out.index("Duration: 1")
duration = out[dp + 10:dp + out[dp:].index(",")]
hh, mm, ss = map(float, duration.split(":"))
# total time ss
total = (hh * 60 + mm) * 60 + ss
for i in xrange(9):
    t = int((i + 1) * total / 10)
    # ffmpeg -i test.mp4 -y -f mjpeg -ss 3 -t 1  test1.jpg
    os.system("ffmpeg -i test.avi -y -f mjpeg -ss %s -t 1 frame%i.jpg" % (t, i))

"""
num=int(total-3)
i=0
for t in xrange(0,num,3):
    i = i+1
	# ffmpeg -i test.mp4 -y -f mjpeg -ss 3 -t 1  test1.jpg 
    os.system("ffmpeg -i test.avi -y -f mjpeg -ss %s -t 1 %sframe%i.jpg" % (t,t, i))
"""


























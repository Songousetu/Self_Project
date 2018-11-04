import imutils

import cv2

image_path = "test_09201.jpg"
image = cv2.imread(image_path)
translated = imutils.translate(image,25,-75)


gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

skeleton = imutils.skeletonize(gray,size=(3,3))

cv2.imshow("Skeleton",skeleton)

cv2.waitKey(2000)

#cv2.imshow("image", translated)
# cv2.waitKey(2000)
# -*- coding:utf-8 -*-
# python 2.7

import cv2
import numpy as np
import glob
import math

################################################################################

print 'criteria and object points set'

# termination criteria
criteria = (3L, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(8,5,0)
objpoint = np.zeros((9 * 9, 3), np.float32)
objpoint[:, :2] = np.mgrid[0:9, 0:9].T.reshape(-1, 2)

# arrays to store object points and image points from all the images

# 3d point in real world space
objpoints = []
# 2d points in image plane
imgpoints = []
################################################################################

print
'Load Images'

# images = glob.glob('images/Phone Camera/*.bmp')
images = glob.glob('C:\Sunaoxue\IT_Project\ADD/test/test/*.jpg')

for frame in images:

    img = cv2.imread(frame)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # find chess board corners
    ret, corners = cv2.findChessboardCorners(imgGray, (9, 9), None)

    # print ret to check if pattern size is set correctly
    print
    ret

    # if found, add object points, image points (after refining them)
    if ret == True:
        # add object points
        objpoints.append(objpoint)
        cv2.cornerSubPix(imgGray, corners, (11, 11), (-1, -1), criteria)
        # add corners as image points
        imgpoints.append(corners)

        # draw corners
        cv2.drawChessboardCorners(img, (9, 9), corners, ret)
        print (img)

        cv2.imshow('Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

################################################################################

print
'camera matrix'

ret, camMat, distortCoffs, rotVects, transVects = cv2.calibrateCamera(objpoints, imgpoints, imgGray.shape[::-1], None,None)

################################################################################

print
're-projection error'

meanError = 0
for i in xrange(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rotVects[i], transVects[i], camMat, distortCoffs)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
    meanError += error

print
"total error: ", meanError / len(objpoints)


################################################################################

def drawAxis(img, corners, imgpoints):
    corner = tuple(corners[0].ravel())
    cv2.line(img, corner, tuple(imgpoints[0].ravel()), (255, 0, 0), 5)
    cv2.line(img, corner, tuple(imgpoints[1].ravel()), (0, 255, 0), 5)
    cv2.line(img, corner, tuple(imgpoints[2].ravel()), (0, 0, 255), 5)

    return img


################################################################################

def drawCube(img, corners, imgpoints):
    imgpoints = np.int32(imgpoints).reshape(-1, 2)

    # draw ground floor in green color
    cv2.drawContours(img, [imgpoints[:4]], -1, (0, 255, 0), -3)

    # draw pillars in blue color
    for i, j in zip(range(4), range(4, 8)):
        cv2.line(img, tuple(imgpoints[i]), tuple(imgpoints[j]), (255, 0, 0), 3)

    # draw top layer in red color
    cv2.drawContours(img, [imgpoints[4:]], -1, (0, 0, 255), 3)

    return img


################################################################################

print
'pose calculation'

axis = np.float32([[3, 0, 0], [0, 3, 0], [0, 0, -3]]).reshape(-1, 3)
axisCube = np.float32([[0, 0, 0], [0, 3, 0], [3, 3, 0], [3, 0, 0], [0, 0, -3], [0, 3, -3], [3, 3, -3], [3, 0, -3]])

for frame in glob.glob('C:\Sunaoxue\IT_Project\ADD/test/test/*.jpg'):

    img = cv2.imread(frame)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (9, 9), None)

    if ret == True:
        # find the rotation and translation vectors.
        rotVects, transVects, inliers = cv2.solvePnPRansac(objpoint, corners, camMat, distortCoffs)

        # project 3D points to image plane
        '''
        imgpoints, jac = cv2.projectPoints(axis, rotVecs, transVecs, camMat, distortCoffs)
        img = drawAxis(img, corners, imgpoints)
        '''

        imgpoints, jac = cv2.projectPoints(axisCube, rotVects, transVects, camMat, distortCoffs)
        img = drawCube(img, corners, imgpoints)

        cv2.imshow('Image with Pose', img)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

# < pre name = "code" class ="python" >  ################################################################################
img1 = cv2.imread('C:\Sunaoxue\IT_Project\ADD/test/1.jpg')  # query image
img2 = cv2.imread('C:\Sunaoxue\IT_Project\ADD/test/2.jpg')  # train image


print 'SIFT Keypoints and Descriptors'
sift = cv2.SIFT()
keypoint1, descriptor1 = sift.detectAndCompute(img1, None)
keypoint2, descriptor2 = sift.detectAndCompute(img2, None)
################################################################################
print 'SIFT Points Match'
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
# flann = cv2.FlannBasedMatcher(index_params, search_params)
bf = cv2.BFMatcher()
matches = bf.knnMatch(descriptor1, descriptor2, k=2)
################################################################################
good = []
points1 = []
points2 = []
################################################################################
for i, (m, n) in enumerate(matches):

    if m.distance < 0.7 * n.distance:
        good.append(m)
        points1.append(keypoint1[m.queryIdx].pt)
        points2.append(keypoint2[m.trainIdx].pt)

points1 = np.float32(points1)
points2 = np.float32(points2)

F, mask = cv2.findFundamentalMat(points1, points2, cv2.RANSAC)

# We select only inlier points
points1 = points1[mask.ravel() == 1]
points2 = points2[mask.ravel() == 1]

################################################################################

# camera matrix from calibration
K = np.array([[517.67386649, 0.0, 268.65952163], [0.0, 519.75461699, 215.58959128], [0.0, 0.0, 1.0]])

# essential matrix
E = K.T * F * K

W = np.array([[0., -1., 0.], [1., 0., 0.], [0., 0., 1.]])
U, S, V = np.linalg.svd(E)

# rotation matrix
R = U * W * V
# translation vector
t = [U[0][2], U[1][2], U[2][2]]

# cv2.checkValidRot(R)

P1 = [[R[0][0], R[0][1], R[0][2], t[0]], [R[1][0], R[1][1], R[1][2], t[1]], [R[2][0], R[2][1], R[2][2], t[2]]]
P = [[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.]]

################################################################################

print 'points triangulation'

u = []
u1 = []
Kinv = np.linalg.inv(K)

# convert points in gray image plane to homogeneous coordinates
for idx in range(len(points1)):
    t = np.dot(Kinv, np.array([points1[idx][0], points1[idx][1], 1.]))
    t1 = np.dot(Kinv, np.array([points2[idx][0], points2[idx][1], 1.]))

    u.append(t)
    u1.append(t1)
################################################################################

# re-projection error
reprojError = 0

# point cloud (X,Y,Z)
pointCloudX = []
pointCloudY = []
pointCloudZ = []

for idx in range(len(points1)):
    X = cv2.triangulatePoints(u[idx], P, u1[idx], P1)

    pointCloudX.append(X[0])
    pointCloudY.append(X[1])
    pointCloudZ.append(X[2])

    temp = np.zeros(4, np.float32)
    temp[0] = X[0]
    temp[1] = X[1]
    temp[2] = X[2]
    temp[3] = 1.0
    print temp

    # calculate re-projection error
    reprojPoint = np.dot(np.dot(K, P1), temp)
    imgPoint = np.array([points1[idx][0], points1[idx][1], 1.])

    reprojError += math.sqrt(
        (reprojPoint[0] / reprojPoint[2] - imgPoint[0]) * (reprojPoint[0] / reprojPoint[2] - imgPoint[0]) + (
        reprojPoint[1] / reprojPoint[2] - imgPoint[1]) * (reprojPoint[1] / reprojPoint[2] - imgPoint[1]))

print 'Re-project Error:', reprojError / len(points1)

import numpy as np
import cv2 as cv
import glob

chessboardSize = (8, 5)	# Pass the checkboar dimensions to the function
frameSize = (1280, 720) 

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((chessboardSize[0]*chessboardSize[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboardSize[0],
                       0:chessboardSize[1]].T.reshape(-1, 2)

imgp = []
images = glob.glob('*.jpg') #Edit based on if it is jpg or png


def swap(nums):
    for i in range(0, len(nums), 2):
        try:
            nums[i], nums[i+1] = nums[i+1], nums[i]
        except:
            pass
    return nums


for image in images:
    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    ret, corners = cv.findChessboardCorners(gray, chessboardSize, None)

    if ret == True:
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

        for i in range(len(corners2)):
            imgp.append(corners2[i][0][0])
            imgp.append(corners2[i][0][1])

        img = cv.drawChessboardCorners(img, chessboardSize, corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(1000)

#-----------------------------------------------------EDIT BELOW BASED ON YOUR CAMERA CALIBRATION-----------------------------------------------------

dist = np.array([4.55996076e+01,  4.16042567e+04, 7.41964622e+00, -1.57784586e+00,
                 7.50716231e+04], np.double)

mtx = np.array([1.44206747e+04, 0.00000000e+00, 4.16624177e+02,
                0.00000000e+00, 1.43001522e+03, 1.99904270e+02,
                0.00000000e+00, 0.00000000e+00, 1.00000000e+00], np.double).reshape(3, 3)

objp = [1.62, 1.80, 0, 1.56, 1.80, 0, 1.50, 1.80, 0, 1.44, 1.80, 0, 1.38, 1.80, 0, 1.32, 1.80, 0, 1.26, 1.80, 0, 1.20, 1.80, 0, 1.62, 1.86, 0, 1.56, 1.86, 0, 1.50, 1.86, 0, 1.44, 1.86, 0, 1.38, 1.86, 0, 1.32, 1.86, 0, 1.26, 1.86, 0, 1.20, 1.86, 0, 1.62, 1.92, 0, 1.56, 1.92, 0, 1.50, 1.92, 0, 1.44, 1.92,
        0, 1.38, 1.92, 0, 1.32, 1.92, 0, 1.26, 1.92, 0, 1.20, 1.92, 0, 1.62, 1.98, 0, 1.56, 1.98, 0, 1.50, 1.98, 0, 1.44, 1.98, 0, 1.38, 1.98, 0, 1.32, 1.98, 0, 1.26, 1.98, 0, 1.20, 1.98, 0, 1.62, 2.04, 0, 1.56, 2.04, 0, 1.50, 2.04, 0, 1.44, 2.04, 0, 1.38, 2.04, 0, 1.32, 2.04, 0, 1.26, 2.04, 0, 1.20, 2.04, 0]

#--------------------------------------------------------------------STOP HERE--------------------------------------------------------------------

objp.reverse()
objp = np.array(objp, np.float32).reshape(-1, 3)

# imgp = swap(imgp) # swap the x and y coordinates. Uncomment if you want to swap the x and y coordinates
imgp = np.array(imgp, np.float32).reshape(-1, 2)

success, rotation_vector, translation_vector = cv.solvePnP(
    objectPoints=objp, imagePoints=imgp, cameraMatrix=mtx, distCoeffs=dist)

rotM = cv.Rodrigues(rotation_vector)[0]
cameraPosition = -np.matrix(rotM) * np.matrix(translation_vector)

print("Rotation Vector: \n", rotation_vector)
print("Rotation Degrees: \n", np.degrees(rotation_vector))
print("Translation Vector: \n", cameraPosition)

cv.destroyAllWindows()

import numpy as np
import cv2 as cv
import math

objp = [1.62, 1.80, 0, 1.56, 1.80, 0, 1.50, 1.80, 0, 1.44, 1.80, 0, 1.38, 1.80, 0, 1.32, 1.80, 0, 1.26, 1.80, 0, 1.20, 1.80, 0, 1.62, 1.86, 0, 1.56, 1.86, 0, 1.50, 1.86, 0, 1.44, 1.86, 0, 1.38, 1.86, 0, 1.32, 1.86, 0, 1.26, 1.86, 0, 1.20, 1.86, 0, 1.62, 1.92, 0, 1.56, 1.92, 0, 1.50, 1.92, 0, 1.44, 1.92,
        0, 1.38, 1.92, 0, 1.32, 1.92, 0, 1.26, 1.92, 0, 1.20, 1.92, 0, 1.62, 1.98, 0, 1.56, 1.98, 0, 1.50, 1.98, 0, 1.44, 1.98, 0, 1.38, 1.98, 0, 1.32, 1.98, 0, 1.26, 1.98, 0, 1.20, 1.98, 0, 1.62, 2.04, 0, 1.56, 2.04, 0, 1.50, 2.04, 0, 1.44, 2.04, 0, 1.38, 2.04, 0, 1.32, 2.04, 0, 1.26, 2.04, 0, 1.20, 2.04, 0]
objp.reverse()
objp = np.array(objp, np.float32).reshape(-1, 3)
objpoints = [objp]

imgp = [419.13412, 1068.8829, 424.81805, 937.82086, 431.1312, 809.5475, 436.9917, 684.95966, 437.4158, 561.8475, 441.2975, 439.72064, 445.4747, 317.3859, 444.4246, 195.41719, 344.8355, 1029.2823, 351.3001, 911.15125, 356.72003, 796.01794, 361.1652, 683.6569, 362.86572, 572.49835, 366.62662, 462.38846, 370.3426, 351.8674, 369.4506, 240.57732, 282.44662, 997.1663, 289.2739, 889.64514, 293.29214, 785.21533, 299.0162, 682.63403,
        300.59793, 581.216, 304.56366, 480.5872, 307.35815, 379.76273, 306.99243, 278.0688, 229.21298, 970.3423, 235.98654, 871.87683, 240.77638, 775.87494, 246.36096, 681.60956, 248.68774, 588.44354, 252.52582, 495.8467, 254.68811, 403.11197, 254.80092, 309.61746, 184.50703, 947.6974, 190.27696, 857.1328, 195.74687, 768.121, 200.5076, 680.88574, 203.2755, 594.4035, 207.66791, 508.72375, 208.53635, 422.54614, 210.72336, 336.5901]

imgp = np.array(imgp, np.float32).reshape(-1, 2)
imgpoints = [imgp]

dist = np.array([0.0, 0.0, 0.0, 0.0, 0.0], np.double)
mtx = np.array([919.033203125, 0.0, 651.2035522460938, 0.0,
               919.698486328125, 357.77734375, 0.0, 0.0, 1.0], np.double).reshape(3, 3)

success, rotation_vector, translation_vector = cv.solvePnP(
    objectPoints=objp, imagePoints=imgp, cameraMatrix=mtx, distCoeffs=dist)

rotM = cv.Rodrigues(rotation_vector)[0]
cameraPosition = -np.matrix(rotM) * np.matrix(translation_vector)

def rotationMatrixToEulerAngles(R) :

    assert(isRotationMatrix(R))

    sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])

    singular = sy < 1e-6

    if  not singular :
        x = math.atan2(R[2,1] , R[2,2])
        y = math.atan2(-R[2,0], sy)
        z = math.atan2(R[1,0], R[0,0])
    else :
        x = math.atan2(-R[1,2], R[1,1])
        y = math.atan2(-R[2,0], sy)
        z = 0

    return np.array([x, y, z])

def isRotationMatrix(R) :
    Rt = np.transpose(R)
    shouldBeIdentity = np.dot(Rt, R)
    I = np.identity(3, dtype = R.dtype)
    n = np.linalg.norm(I - shouldBeIdentity)
    return n < 1e-6

euler = rotationMatrixToEulerAngles(rotM)

print("Rotation Vector: \n", rotM)
print("Euler Angles: \n", euler)
print("Translation Vector: \n", cameraPosition)
print("Original Translation Vector: \n", translation_vector)

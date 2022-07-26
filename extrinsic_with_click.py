import cv2
import numpy as np

x_list = []
y_list = []
matrix = []

#------------------------------------------------------------------------------EDIT PARAMETERS HERE------------------------------------------------------------------------------

objp = [0.60, 0, 0, 0.60, 0.60, 0, 0.60, 1.20, 0, 0.60, 1.80, 0, 0.60, 2.40, 0, 1.20, 0,
        0, 1.20, 0.60, 0, 1.20, 1.20, 0, 1.20, 1.80, 0, 1.20, 2.40, 0, 1.80, 0, 0, 1.80, 0.60, 0, 1.80, 1.20, 0, 1.80, 1.80, 0, 1.80, 2.40, 0, 2.40, 0, 0, 2.40, 0.60, 0, 2.40, 1.20, 0, 2.40, 1.80, 0, 2.40, 2.40, 0, 3.0, 0, 0, 3.0, 0.60, 0, 3.0, 1.20, 0, 3.0, 1.80, 0, 3.0, 2.40, 0]

dist_list = [0.0, 0.0, 0.0, 0.0, 0.0]
mtx_list = [919.033203125, 0.0, 651.2035522460938,
            0.0, 919.698486328125, 357.77734375, 0.0, 0.0, 1.0]

#-----------------------------------------------------------------------------------STOP HERE-----------------------------------------------------------------------------------

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        cv2.imshow('image', img)
        x_list.append(y)    # it is swapped here. Change maybe needed
        y_list.append(x)    # it is swapped here. Change maybe needed

    if event == cv2.EVENT_RBUTTONDOWN or len(x_list) == 25:
        matrix = points_to_matrix(x_list, y_list)
        calibration(matrix, objp=objp,
                    dist_list=dist_list, mtx_list=mtx_list)


def points_to_matrix(x_list, y_list):
    matrix = []
    for i in range(len(x_list)):
        matrix.append(x_list[i])
        matrix.append(y_list[i])
    return matrix


def calibration(imgp, objp, dist_list, mtx_list):
    objp = np.array(objp, np.float32).reshape(-1, 3)
    imgp = np.array(imgp, np.float32).reshape(-1, 2)

    dist = np.array(dist_list, np.double)
    mtx = np.array(mtx_list, np.double).reshape(3, 3)

    success, rotation_vector, translation_vector = cv2.solvePnP(
        objectPoints=objp, imagePoints=imgp, cameraMatrix=mtx, distCoeffs=dist)

    rotM = cv2.Rodrigues(rotation_vector)[0]
    cameraPosition = -np.matrix(rotM) * np.matrix(translation_vector)

    print("Rotation Vector: \n", np.degrees(rotation_vector[0][0]))
    print("Translation Vector: \n", cameraPosition)
    exit()


if __name__ == "__main__":

    img = cv2.imread(
        '/home/jacob/Documents/Accio/GlobalTruth/frame0000.jpg', 1) # change this to the path of the image
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
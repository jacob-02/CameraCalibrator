
# Camera Calibrator

It helps in finding the extrinsic parameters of the camera which in turn
helps in finding the position of the camera in a 3D pose with respect to the
user defined world coordinates. Helps in setting up a global truth for robotic
systems.




## Installation

Installing CameraCalibrator

```bash
  git clone https://github.com/jacob-02/CameraCalibrator
  pip install -r requirements.txt
```
    
## Deployment

To deploy this project run

```bash
  cd CameraCalibrator
  python3 extrinsic_with_checkboard.py
  python3 extrinsic_with_click.py
```
The second command calibrates the camera position with respect to image points
detected by checkboard corner detector function in opencv. The *checkboard size, 
object points with respect to a world frame and if the image which we are using to calibrate is a .jpg or .png* must be edited.

The third command calibrates the camera position with respect to image points 
selected in an image that is fed and the points are chosen by selecting on the
image with a mouse pointer.

Common things to be edited in both the files are:
 - Object Points with respect to a Global Origin
 - Distortion Coefficient of the Camera
 - Camera Matrix of the Camera

The Object Points must be measured by the user and input into the code.
Distortion coeffs and Camera matrix can be found my running the following 2 codes:

```bash
cd images
python3 calibrator.py
python3 image_save.py
```
The third command helps in saving multiple images of a checkboard whose size must be
defined by the user correctly. 

After clicking a suitable number of images, *minimum 10*, 
the user can run the second command that will help in giving the camera matrix and the 
distortion coefficients. This can then be inputted into the main files and give the
user the translation and rotational vectors (radians and degrees).


## Acknowledgements

 - [Camera Calibration](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)
 - [Camera Calibration in Python with OpenCV - Python Script with Images](https://www.youtube.com/watch?v=3h7wgR5fYik)
 - [image_pipeline](https://github.com/ros-perception/image_pipeline)


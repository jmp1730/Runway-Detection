# Runway Detection and Localization in Aerial Images Using Deep Learning
### Developed by Joshua Mathew Philip from Cochin University of Science and Technology.
### Made for UG Major Project.

In this project, our objective was to build a vision based system using deep learning and image processing techniques to detect runway and localize the runway. Vision based systems provide low cost solution to detect landing sites by providing rich textual information. So we are trying implement a low cost runway localization system which use only use camera as extra hardware to detect runway.

## Features
- Runway Detection and Localization:
Purpose: The program will detect if there is a runway in an image and localize it.
Input: Image imported from system to be tested.
Output: If runway detected:
			The same image with a blue shade highlighting the runway is displayed.
	    If runway not detected:
			A message showing ”runway not detected” is displayed.<br>

## How this works?
The Runway detection and Localization System works in two modules:
1. Runway Detection
which includes:
--Data Preprocessing
--Feature Extraction
--Classification and Training
--Fine Tuning

2. Runway Localization
which includes:
--Line Detection Techniques
--CNN

### Steps workflow:
- Setting up 
- Download/Update latest data.
- Activate Virtual Environment.
- Start the program. 

### Hardware and Software Requirements
## Hardware:
- Processor: i3 or i5 (i5 is better) 
- RAM: 8GB (Minimum)  
- Hard Disk: 500GB or above<br>
## Software:
- Tkinter :The frontend development is entirely done with Tkinter. Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python’s de facto standard GUI.<br>
- Python 3.7 : The entire application is written in the python program- ming language, the deep learning modules used are also based on python.<br>
- Tensorflow v2.1 : It’s the backbone of the back-end part of the system. Focused on training and inference of the neural networks.<br>
- OpenCV : It’s also a part of backend part, mainly aimed at real-time computer vision.<br>
- Keras: It provides a Python interface for artificial neural networks and acts as an interface for the TensorFlow library.<br>

## STEPS

### Installing Prerequisites
- 1.1 - Download and Install Python IDLE.<br>
- 1.2 - Download and install anaconda3 from given link : 
https://www.filehorse.com/download-anaconda-64/download/ <br>
- 1.3 - Setting Virtual Environment 
https://drive.google.com/file/d/11DD9TefmGKzvc6_jADen38FgYlbfu9Bi/view?usp=sharing
Extract mrcnn1.zip file in the `c/users/user/anaconda3/envs folder`.<br>
- 1.4 - Open anaconda prompt in the `Runway_detection` folder<br>
- 1.5 - Adding data set
https://1drv.ms/u/s!AmgKYzARBl5ca3HNaHIlzp_IXjs
Extract NWPU-RESISC45.rar file to the `Runway_detection` folder.<br>

### Running the Program
- 2.1 - Open anaconda prompt.<br>
- 2.2 - Run command : `activate mrcnn1` .<br>
- 2.3 - Change directory to `Runway_detection` folder.<br>
- 2.4 - Run command : `python gui.py`.<br>
- 2.5 - Upload an image.
- 2.6 - Click the button on the pop up window to start detection.<br>


### Brief of given files
1. `pre.py` - for preprocessing.<br>
2. `resnet50.py` - resnet50 model.<br>
3. `detect.py` - for recognition of runway.<br>
4. `gui.py` - for creation of user interface and to run the program.<br>
5. `ht.py` - hough transform for localization.<br>
6. `mrcnn1.zip` - to set up the virtual environment.<br>
7. `mask_rcnn.py` - to segment image.<br>


### Screenshots
# Dataset Creation-
![Dataset Creation](/images/dr.png) <br>
![Dataset Creation](/images/dn.png) <br>
# Runway Recognition-
![Runway Recognition](/images/guid.png) <br>
![Runway Recognition](/images/guin.png) <br>


Any improvement to this Documentation or any new contributions are always welcome! 

Thanks,
Joshua Mathew Philip
# Fender
The fender is a robot used in a delivery service provided within the Engineering Research Building (ERB) at The University of Texas at Alrington (UTA). It is accessible for usage using this website(repo)](https://github.com/Jonahbui/fender-web-app)



# Hardware Specifications
- Raspberry Pi 4
- [Sabertooth2x32](https://www.dimensionengineering.com/products/sabertooth2x32)
- [KangarooX2](https://www.dimensionengineering.com/products/kangaroo)
- TFMini Plus
- Intel RealSense T265
- Intel RealSense D435
- A 24V to 5V USB-C Converter



# Notes
In this section is relevant information that may aid in the development of the fender.
## Login Information
```
user: ubuntu
pass: ERBPS&FENDER
```


## Sabertooth2x32 Configuration
The sabertooth is running in USB mode and normal mode.

To find the port the sabertooth is connected to in the Pi, go here:
```
cd /dev/serial/by-id/...
```

The DIP switches should be setup as such (1-ON, 2-OFF, 3-ON, 4-ON, 5-ON, 6-OFF)


## KangarooX2 Configuration
The DIP switches should be setup as such (1-ON, 2-ON, 3-ON, 4-ON)


## Source Code
The source code should be in the directory ```/Fender ```.


## Packages
### librealsense & pyrealsense2
The package pyrealsense2 is part of the librealsense library. After building and installing librealsense, you can find the pyrealsense2 library in ```/librealsense/wrappers/python```. 

Currently, on the pi you can find it in ```Fender/librealsense/wrappers/python```. However, we were not able to successfully install pyrealsense2 such that it can be imported. For installation instructions on pyrealsense2 that we used, follow this [link](https://github.com/IntelRealSense/librealsense/tree/master/wrappers/python).

### opencv
This package should be built locally and installed already. However, we were not able to test functionality with it. Also, librealsense has a wrapper for opencv that might be useful.

# Packages
- [pysabertooth](https://github.com/MomsFriendlyRobotCompany/pysabertooth)
- [opencv](https://docs.opencv.org/4.x/d9/df8/tutorial_root.html)
- [librealsense](https://github.com/IntelRealSense/librealsense)
- [pyrealsense2](https://pypi.org/project/pyrealsense2/)



# Contributors
- Jonah Bui
- Connor Dominguez
- Anh Tran
- Burhanuddin Chinwala
- Ian Klobe

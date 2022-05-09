# Fender
The fender is a robot used in a delivery service provided within the Engineering Research Building (ERB) at The University of Texas at Alrington (UTA). It is accessible for usage using this [repository](https://github.com/Jonahbui/fender-web-a). A hardware schematics can be found in this repository as well, if necessary.


### Table of Contents
1. [Hardware Specifications](#hardware-specifications)
2. [Hardware Configurations](#hardware-configurations)
    - [Sabertooth2x32 Configuration](#sabertooth2x32-configuration)
    - [KangarooX2 Configuration](#kangaroox2-configuration)
3. [Software & Pi Configurations](#software-and-pi-configurations)
    - [Login](#login-information)
    - [Source Code](#source-code)
    - [State of Packages](#state-of-packages)
5. [Packages](#packages)
6. [Contributors](#contributors)

# Hardware Specifications
- Raspberry Pi 4
- [Sabertooth2x32](https://www.dimensionengineering.com/products/sabertooth2x32)
- [KangarooX2](https://www.dimensionengineering.com/products/kangaroo)
- TFMini Plus
- Intel RealSense T265
- Intel RealSense D435
- A 24V to 5V USB-C Converter




# Hardware Configurations
## Sabertooth2x32 Configuration
The sabertooth is running in USB mode and normal mode.

To find the port the sabertooth is connected to in the Pi, go here:
```
cd /dev/serial/by-id/...
```

The DIP switches should be setup as such (1-ON, 2-OFF, 3-ON, 4-ON, 5-ON, 6-OFF)


## KangarooX2 Configuration
The DIP switches should be setup as such (1-ON, 2-ON, 3-ON, 4-ON)




# Software and Pi Configurations
In this section is relevant information that may aid in the development of the fender.
## Login Information
```
user: ubuntu
pass: ERBPS&FENDER
```

## Source Code
The source code should be in the directory ```/Fender ```.


## State of Packages
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

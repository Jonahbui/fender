# Fender
The fender is a robot used in a delivery service provided within the Engineering Research Building (ERB) at The University of Texas at Alrington (UTA). It is accessible for usage using this website WEBSITE_HERE [(repo)](https://github.com/Jonahbui/fender-web-app)

# Hardware Specifications
- Raspberry Pi 4
- [Sabertooth2x32](https://www.dimensionengineering.com/products/sabertooth2x32)
- [KangarooX2](https://www.dimensionengineering.com/products/kangaroo)
- TFMini Plus
- Lidar
- Intel Realsense

# Notes
In this section is relevant information that may aid in the development of the fender.
## Sabertooth2x32 Configuration
The sabertooth is running in USB mode and normal mode.

To find the port the sabertooth is connected to in the Pi, go here:
```
cd /dev/serial/by-id/...
```

The DIP switches should be setup as such (1-ON, 2-OFF, 3-ON, 4-ON, 5-ON, 6-OFF)

## KangarooX2 Configuration
The DIP switches should be setup as such (1-ON, 2-ON, 3-ON, 4-ON)


# Packages
- [pysabertooth](https://github.com/MomsFriendlyRobotCompany/pysabertooth)
- [opencv](https://docs.opencv.org/4.x/d9/df8/tutorial_root.html)

# Contributors
- Jonah Bui
- Connor Dominguez
- Anh Tran
- Burhanuddin Chinwala
- Ian Klobe

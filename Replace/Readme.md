## Replacement arduino library file
1. Download the esp32-eyes library from: https://github.com/playfultechnology/esp32-eyes.
2.	Place the downloaded library folder in your Arduino libraries directory. The typical location is one of:
C:\Users\YourUserName\Documents\Arduino\libraries\
C:\Users\YourUserName\AppData\Local\Arduino15\
3.	Inside the installed library folder, locate:
...\Arduino\libraries\esp32-eyes\Common.h
...\Arduino\libraries\esp32-eyes\Face.cpp
4.	If library installed, look for a folder like: ...\Arduino\libraries\esp32-eyes\.
5.	Replace both Common.h and Face.cpp with the custom versions provided by your hardware supplier. These modified files adjust the library to match the specific OLED wiring and display configuration of your ESP32-C3 board.

### *Using the unmodified library files from GitHub will cause incorrect display behaviour or compilation errors on your specific hardware.

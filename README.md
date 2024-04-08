# UART-Data-Transmission-Firmware
This repository hosts firmware code designed for bidirectional data transmission between a PC and a microcontroller unit (Arduino UNO) using UART communication. The firmware enables the transmission of a specified text from the PC to the MCU, storing it in EEPROM memory, and subsequently transmitting it back to the PC. Additionally, it incorporates real-time measurement of data transmission speed in bits per second.
# Overview:
**1.Python Script (FinalPC.py):** Sends text data to the Arduino Uno character by character. It also calculates and prints the real-time transmission and receiving speed in bits/second.

**2.Arduino Sketch (FinalMCU.ino):** Receives data from the PC via the serial port, stores it in EEPROM, and sends back the stored data upon request. 
# Contents:
**FinalPC**:Contains the PC-side code (FinalPC.py) responsible for initiating data transmission and displaying received data on the console.

**FinalMCU:** Houses the MCU firmware code (FinalMCU.ino) written in Embedded C/C++, managing data reception, storage, and transmission.
# Requirements:
1.Python 3.x

2.Arduino Uno or compatible board

3.USB cable for connection to PC

4.USB to UART converter

# Usage:
1.Connect the Arduino Uno to the PC via USB.

2.Upload the FinalMCU.ino sketch to the Arduino Uno.

3.Run the FinalPC.py script on the PC.

4.Ensure that the correct COM port for the Arduino Uno is specified in the script.

# Note:
The provided Arduino code does not include any built-in functions or headers such as EEPROM.h. All functionalities related to EEPROM read and write operations are implemented without relying on external libraries.

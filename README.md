# WhatsPyApp

An automated script to send human-like messages on your WhatsApp Web Client.

## How to use?

### Dependencies
1. Platform: **Windows x64**
2. Packages: **Selenium**, **time**, **random**

### Changes to make
In the ``sendMessage.py`` script, make the following changes:
1. Line Number **16**:
	```python
	target = 'Contact Name' #Replace with your target's name.
	```
2. Line Number **37**:
	```python
	# Enter your long message here.
	multiline_msg = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
	Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
	Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''
	```
	
### How to run?
Note: This program was made in [PyCharm](https://www.jetbrains.com/pycharm/download/).

1. Click on run program. (green play button)
2. Wait for the Chromium instance to open.
3. Scan the QR code with WhatsApp.
	a. Open WhatsApp > Click on Three Dots.
	b. Select WhatsApp Web.
	c. Scan QR Code or click on + sign on top right.
4. Watch the script do its magic!

### Problems
You can download the latest [Chromimum Webdriver  here](http://chromedriver.chromium.org/downloads).
Replace this file with the ```chromedriver.exe``` to update your web driver.

## This script is for educational purposes only. Please use it at your own risk. Whatsapp or I am not responsible for any problems caused by the user (You) of this script.
# QR Code VLC Player

This goal of this project is to create a program that can generate QR codes based on the videos in the videos directory and play them when the corresponding code is scanned.

## Requirements
This python program can be ran on any device with a camera that can run python files.

### Python Dependencies (requirements.txt)
- Python 3.11.5+ *(This is the one I was using)*
- opencv-python
- qrcode
- python-vlc

## Getting started
1. Place all your videos in the "videos" folder
2. Attach a camera (webcam)
3. Run main.py
4. QR Codes will automatically be generated under codes directory
5. With your camera, point towards the QR Code
6. Corresponding video will play in full screen

## Configuration
The following are what can be configured for better performance

| File | Variable | Description | Default Value |
| ------ | ---------- | ------------- | --------------- |
| main.py | sleepTime | The time between frames. | 0.5s |
| main.py | showOutput | Shows the camera's output (frame) | True |
| QRCode.py | videos_directory | The videos folder path | "./videos" |

### Other Configurations
#### To change the color of the QR Code
The only colors currently considered are black and white colors.
If you need to invert the colors, please refer to the following.

In QRCode.py, you have the following line 37:

    img = qr.make_image(fill_color="white", back_color="black")

You can change "fill_color" and "back_color" to black or white.
When changing these colors, you also need to change "inverted" to True or False:

| *fill_color* | *back_color* | inverted |
| ---------- | ---------- | -------- |
| white | black | True |
| black | white | False |

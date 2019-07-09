# GUI for VSN lab
### made by Michal Gilski for VSN Lab in 2019

This the a simple GUI to display the camera feed from multiple cameras using ZeroMQ. 
## Installation
To use this program on Linux based systems follow the install guide.
## Usage
To run the program execute "python main.py". The GUI receives and displays camera feeds, bounding box coordinates (that is displayed as a box) and text information from up to 5 cameras. The data format is specified in Message.proto.

To use Gui on a local computer with the webcam use "python main.py -l" or "python main.py --local" 

The Gui accepts input from both port 9000 and 8000

## Supported topics:
- Image - Frame to be displayed - type: ImageInfo
- Command - Text to be displayed below a stream - type: AdditionalControl
- Prediction - Text that can be displayed on top of the interface (only one place, so it should be used only by one camera, preferably the leader) 
- 



 


import picamera
import io
import os

from time import sleep

# Import to send data from raspberry pi to arduino
from serial import Serial

# Import the API's to perform the object detection on images

# Will be used for ser.write() to send data to arduino via usb
ser = Serial('/dev/ttyACM0', 9600)

# Will be used to check if description of an image classifies as "trash"
TRASH_ITEMS = set(['paper', 'product', 'aluminum', 'cardboard', 'plastic',
'bottle', 'can', 'plate', 'glass', 'metal', 'trash', 'wrapper', 'cup',
'drink', 'drinkware', 'waste', 'litter', 'pollution'])

def describe_img(image_url):

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        image_url)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    # Perform label detection on the image file

    # Check if trash was detected
    """
    EXAMPLE:
    for label in labels:
        if label.description in TRASH_ITEMS:
            print "TRASH DETECTED"
            # ser.write(1)
            return"""

camera = picamera.PiCamera()
counter = 0
while True:
    print 'Capturing image:', counter
    camera.capture('image1.jpg')
    describe_img('image1.jpg')
    counter += 1

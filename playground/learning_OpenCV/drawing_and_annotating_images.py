import cv2
import numpy as np

image = np.zeros((500, 500, 3), dtype=np.uint8)
# creates an array using numpy with only zeros (for a blank image)
# remember, images are 3d in opencv, 2 dimensions for width and height, 1 for RGB
# the width and height are defined to be 500
# the RGB dimension is simply defined as 3 bc there are three layers (red,blue,green)


'The below code covers how to draw various shapes'

cv2.rectangle(image, (50,50), (400,400), (0,255,0), 3)
# the first parameter after image defines the starting point
# in this case, the rectangle starts x1 = 50 and y1 = 50
# the parameter after defines the rectangle endpoints (x2=400, y2=400)
# the rectangle should have a height and width of 350
# (0,255,0) defines the color, this is RGB for Green
# 3 defines the rectangle thickness

cv2.circle(image, (250,250), 100, (255,0,0), 10)
# for a circle, the first parameter after image defines the starting point
# the starting point is the center of our image (which was l=500 and w=500)
# 100 defines circle radius
# (255,0,0) gives the circle a blue color
# 10 is the thickness of the circle

cv2.line(image, (0,0), (500,500), (0,0,255), 2)
# (0,0) is the line starting point
# the line goes till (500,500)
# the line will have a red color and a thickness of 2

cv2.imshow("Image with Shapes", image)

# with OpenCV, the coordinate system works in a downward manner
# the origin begins at the top left


'The below code shows how to add text to an image'

text_img = np.zeros((500, 500, 3), dtype=np.uint8)

cv2.putText(text_img, "Fun shapes!", (50,250), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
# the first parameter after image is the text you'd like to put
# afterwards, the font is defined
# 1 represents the scale of the text
# (0,255,0) is the color for the text that you'd like
# 2 represents text width

cv2.imshow("Image with Text!", text_img)




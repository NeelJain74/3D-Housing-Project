import os
# allows you to interact with the OS
import cv2
# openCV library

print(os.getcwd())
# view the current working directory

charizard_img = cv2.imread("charizard_sprite.png")
# reads the image into an array

cv2.imshow("Original Img", charizard_img)
# imshow opens a new windows containing the image
# this new window requires a title, which goes as the 1st parameter
cv2.waitKey(5)
# waitKey defines how long the window will stay open
# a value of 0 means that you must close it
# # value defines how many milliseconds it will stay open (e.g. 5 = 5 ms)






import os
# allows you to interact with the OS
import cv2
# openCV library

print(os.getcwd())
# view the current working directory

charizard_img = cv2.imread("images/charizard_sprite.png")
# reads the image into an array

cv2.imshow("Original Img", charizard_img)
# imshow opens a new windows containing the image
# this new window requires a title, which goes as the 1st parameter
cv2.waitKey(0)
# waitKey defines how long the window will stay open
# a value of 0 means that you must close it
# # value defines how many milliseconds it will stay open (e.g. 5 = 5 ms)

gray_charizard_img = cv2.cvtColor(charizard_img, cv2.COLOR_BGR2GRAY)
# converts the img to grayscale
cv2.imshow("Grayscale Img", gray_charizard_img)

cv2.imwrite("images/grayscale_charizard.jpg", gray_charizard_img)
# saves the image in your current wd as a file

cv2.destroyAllWindows()
# destroys all open windows
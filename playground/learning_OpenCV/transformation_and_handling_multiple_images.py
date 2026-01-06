import cv2

charizard_img = cv2.imread("images/charizard_sprite.png")
# reads the image

resized_charizard = cv2.resize(charizard_img, (800, 800))
# resizes the image to 800x800

cv2.imshow("Resized Image", resized_charizard)
# displays the image (in this case, the resized one)

cropped_charizard = charizard_img[100:250, 100:300]
# "crops" the image by including specified pixels only
# the format is (x1, y1) to (x2, y2)
# cv2.imshow("Cropped Image", cropped_charizard)

cv2.imwrite("images/resized_charizard.jpg", resized_charizard)
# saves the image in images folder


'The below code focuses on rotating an image'

(h, w) = charizard_img.shape[:2]
# a typical image contains 3 dimensions (width, height, RGB color)
# height and width are extracted by using [:2], and set to h and w, respectively

center = (w//2, h//2)
# to rotate the image, we must store its center
# note: w is mapped first bc OpenCV reads width first
# numpy reads height first, which is what we used for initial map

rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1)
# creates a new matrix with the rotated #'s stored
# the matrix rotates the 2D image by 45 degrees
# it does this by multipling the existing matrix by a # for rotation
# the image scale is kept at 1

rotated_charizard = cv2.warpAffine(charizard_img, rotation_matrix, (w,h))
# affine tranformations preserve lines and parallels but not necessarily distances/angles
# rotation is considered an affine tranformation, along with translation, etc.
# this function applies the rotated matrix onto the image
# the (w,h) parameter at the end ensures the same img size as OG img






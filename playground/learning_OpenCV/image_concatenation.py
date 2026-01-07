import cv2
import numpy as np

charizard_img = cv2.imread("images/charizard_sprite.png")
blastoise_img = cv2.imread("images/blastoise_sprite.png")
# reading charizard and blastoise sprite images

cv2.imshow("Charizard Sprite", charizard_img)
cv2.imshow("Blastoise Sprite", blastoise_img)
# both images have different sizes
# to display both images in one window, they should both be same size

'The below code shows how to ensure both images are the same size'

height = min(charizard_img.shape[0], blastoise_img.shape[0])
width = min(charizard_img.shape[1], blastoise_img.shape[1])
# .shape[0] displays the height of each img in pixels, min function takes the lower height between both imgs
# likewise with .shape[1], which displays width and takes min

charizard_resized = cv2.resize(charizard_img, (width, height))
blastoise_resized = cv2.resize(blastoise_img, (width, height))
# ensures that both images are now the same width and height
# resize takes width first, then height

'The below code shows how to display both images side-by-side in one window'

side_by_side = cv2.hconcat([charizard_resized, blastoise_resized])
# hconcat puts the images side-by-side (horizontal concatenation)
cv2.imshow("Side by Side Images", side_by_side)
# displays the hconcat matrix
cv2.imwrite("images/hconcat_charizard_and_blastoise.png", side_by_side)
# saves the image on machine

'The below code shows how to display both images top-to-down in one window'

top_down = cv2.vconcat([charizard_resized ,blastoise_resized])
# vconcat puts images in vertical order (one on top of another)
# the charizard sprite will be at the top
cv2.imshow("Top Down Images", top_down)
#displays the vertically concatenated images
cv2.imwrite("images/vconcat_charizard_and_blastoise.png", top_down)

cv2.destroyAllWindows()











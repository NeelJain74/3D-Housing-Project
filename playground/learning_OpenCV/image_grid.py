import cv2
import numpy as np

charizard_img = cv2.imread("images/charizard_sprite.png")
blastoise_img = cv2.imread("images/blastoise_sprite.png")
mew_img = cv2.imread("images/mew_sprite.png")
mewtwo_img = cv2.imread("images/mewtwo_sprite.jpg")

#cv2.imshow("Mew Sprite", mew_img)
#cv2.imshow("Mewtwo Sprite", mewtwo_img)
# displays the mew and mewtwo images

'The below code shows how to make a 2x2 grid of images'

charizard_resized = cv2.resize(charizard_img, (300,300))
blastoise_resized = cv2.resize(blastoise_img, (300,300))
mew_resized = cv2.resize(mew_img, (300,300))
mewtwo_resized = cv2.resize(mewtwo_img, (300,300))
# resizing all images to 300x300 pixels
# for a grid, all images should be the same size and relatively small

cv2.imshow("Charizard Resized", charizard_resized)
cv2.imshow("Blastoise Resized", blastoise_resized)
cv2.imshow("Mew Resized", mew_resized)
cv2.imshow("Mewtwo Resized", mewtwo_resized)
# displaying all resized imgs
cv2.destroyAllWindows()


row_one = cv2.hconcat([charizard_resized, blastoise_resized])
row_two = cv2.hconcat([mewtwo_resized, mew_resized])
# creates a horizontal concatenation twice, each representing a row

final_grid = cv2.vconcat([row_one, row_two])
# vertically concats rows defined earlier to make a complete grid

cv2.imshow("Grid", final_grid)
# displaying the grid

cv2.imwrite("images/image_grid.png", final_grid)

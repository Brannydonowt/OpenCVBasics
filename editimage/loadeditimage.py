import cv2

# imread reads an image
# -1 = unchanged
# 0 = grayscale
# 1 = coloured
img_grayscale = cv2.imread('editimage/flowerimg.jpg', 0)
# Show an image in window : window name, image file
cv2.imshow('grayscale img', img_grayscale)
# wait until input 0 = indefinitely
cv2.waitKey(0)
# destroy all windows
cv2.destroyAllWindows()
# write to a new file based on x 
cv2.imwrite('greyscale.jpg', img_grayscale)


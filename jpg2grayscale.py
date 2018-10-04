from PIL import Image
import numpy as np

def grayscale(rgb):
	print("Starting gray scale conversion...")
	width, height = rgb.shape[0], rgb.shape[1]
	rgb2 = np.zeros((width, height, 3), dtype='uint8')
	for i in range(0, width):
		for j in range(0, height):
			rgb2[i][j][:3] = [int(np.sum(rgb[i][j])/3)]*3
	print("Done!")
	return rgb2

img = Image.open("smalldog.jpg")
arr = np.array(img)
# print(arr.shape)
arrgray = grayscale(arr)

img2 = Image.fromarray(arrgray)
img2.save("smallgraydog.jpg") # also can save as png (pillow automatically converts)
img.show()
img2.show()

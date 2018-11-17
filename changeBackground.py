from PIL import Image
import numpy as np

def targets(x,y):
	yield (x,y) # Center
	yield (x+1,y) # Left
	yield (x-1,y) # Right
	yield (x,y+1) # Above
	yield (x,y-1) # Below
	yield (x+1,y+1) # Above and to the right
	yield (x+1,y-1) # Below and to the right
	yield (x-1,y+1) # Above and to the left
	yield (x-1,y-1) # Below and to the left

def changeBackground(array, color='white'):
	white = [255, 255, 255]
	black = [0, 0, 0]
	if(color=='white'): color_code = white
	elif(color=='black'): color_code = black
	height = array.shape[0]
	width = array.shape[1]
	for x in range(width):
		for y in range(height):
			px = array[x][y]
			if(px[0] == 255 and px[1] == 255 and px[2] == 255):
				for i,j in targets(x,y):
					array[i][j] = color_code			


img = Image.open("smalldog.jpg")
arr = np.array(img)
changeBackground(arr, 'black')
img2 = Image.fromarray(arr)
img2.save("Modified/smalldog_background.jpg")

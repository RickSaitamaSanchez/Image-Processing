from PIL import Image
import numpy as np

def make_image_thumbnail(jpg):
	copy = jpg.copy()
	copy.thumbnail((128,128), Image.ANTIALIAS)
	return copy
	
img = Image.open("smalldog.jpg")
thumb = make_image_thumbnail(img)
# img.show()
thumb.show()
thumb.save("thumb.jpg")
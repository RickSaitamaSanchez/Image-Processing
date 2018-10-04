from PIL import Image
import numpy as np

def max_pooling(x, pooling_kernel_size=2):
	pks = pooling_kernel_size
	height, width = x.shape[0], x.shape[1]
	subx = np.zeros((height//pks,width//pks, 3), dtype='uint8')
	i, k = 0, 0
	while(i <= height-pks):
		j, l = 0, 0
		while(j <= width-pks):
			tmp = x[i:pks+i, j:pks+j] # submatrix (max pooling kernel)
			subx[k][l] = (tmp.max(1)).max(0) # biggest 3-dim array of values (RGB) into image kernel 
			l += 1 # submatrix position (step one by one)
			j += pks # pooling kernel position (step pks by pks)
		k += 1
		i += pks
	return subx

img = Image.open("smalldog.jpg")
arr = np.array(img)
pool_arr = max_pooling(arr)
pool_img = Image.fromarray(pool_arr)
pool_img.save("max_pooling_dog.jpg")
img.show()
pool_img.show()

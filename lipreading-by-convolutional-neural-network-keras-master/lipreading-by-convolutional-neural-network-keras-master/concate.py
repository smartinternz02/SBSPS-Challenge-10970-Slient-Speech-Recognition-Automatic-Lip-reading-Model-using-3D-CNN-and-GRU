import numpy as np
import cv

#read from folder result_lip and write to same folder with name concate-output.jpg
def concate_images(): 
	concate_seq= np.array([0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,10,11,12,13,14,14])
	#read image
	path="result_lip/"
	im_1 = cv.imread(path+"0.jpg", cv.IMREAD_COLOR)
	im_2 = cv.imread(path+"0.jpg", cv.IMREAD_COLOR)
	im_3 = cv.imread(path+"1.jpg", cv.IMREAD_COLOR)
	im_4 = cv.imread(path+"1.jpg", cv.IMREAD_COLOR)
	im_5 = cv.imread(path+"2.jpg", cv.IMREAD_COLOR)
	layer1 = np.concatenate((im_1, im_2, im_3, im_4, im_5), axis=1)

	im_6 = cv.imread(path+"2.jpg", cv.IMREAD_COLOR)
	im_7 = cv.imread(path+"3.jpg", cv.IMREAD_COLOR)
	im_8 = cv.imread(path+"3.jpg", cv.IMREAD_COLOR)
	im_9 = cv.imread(path+"4.jpg", cv.IMREAD_COLOR)
	im_10 = cv.imread(path+"4.jpg", cv.IMREAD_COLOR)
	layer2 = np.concatenate((im_6, im_7, im_8, im_9, im_10), axis=1)

	im_11 = cv.imread(path+"5.jpg", cv.IMREAD_COLOR)
	im_12 = cv.imread(path+"5.jpg", cv.IMREAD_COLOR)
	im_13 = cv.imread(path+"6.jpg", cv.IMREAD_COLOR)
	im_14 = cv.imread(path+"6.jpg", cv.IMREAD_COLOR)
	im_15 = cv.imread(path+"7.jpg", cv.IMREAD_COLOR)
	layer3 = np.concatenate((im_11, im_12, im_13, im_14, im_15), axis=1)

	im_16 = cv.imread(path+"7.jpg", cv.IMREAD_COLOR)
	im_17 = cv.imread(path+"8.jpg", cv.IMREAD_COLOR)
	im_18 = cv.imread(path+"8.jpg", cv.IMREAD_COLOR)
	im_19 = cv.imread(path+"9.jpg", cv.IMREAD_COLOR)
	im_20 = cv.imread(path+"10.jpg", cv.IMREAD_COLOR)
	layer4 = np.concatenate((im_16, im_17, im_18, im_19, im_20), axis=1)

	im_21 = cv.imread(path+"11.jpg", cv.IMREAD_COLOR)
	im_22 = cv.imread(path+"12.jpg", cv.IMREAD_COLOR)
	im_23 = cv.imread(path+"13.jpg", cv.IMREAD_COLOR)
	im_24 = cv.imread(path+"14.jpg", cv.IMREAD_COLOR)
	im_25 = cv.imread(path+"14.jpg", cv.IMREAD_COLOR)
	layer5 = np.concatenate((im_21, im_22, im_23, im_24, im_25), axis=1)

	output = np.concatenate((layer1, layer2, layer3, layer4, layer5), axis=0)
	cv.imwrite(path+"concate-output.jpg", output)
	print("[INFO] concate done")



#concate_images()
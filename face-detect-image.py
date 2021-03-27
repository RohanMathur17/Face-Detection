import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-i" , "--image", required = True , help = "Input Image")
ap.add_argument("-p" , "--prototxt", required = True , help = "Input for prototxt file")
ap.add_argument("-m" , "--model", required = True , help = "Input for caffe trained model")

ap.add_argument("-c" , "--confidence", type = float , default = 0.5, help = "Min Threshold to detect")


args = vars(ap.parse_args())

print("Now Loading Model...")

net = cv2.dnn.readNetFromCaffe(args["prototxt"],args["model"])

image = cv2.imread(args["image"])

(h, w) = image.shape[:2]

blob = cv2.dnn.blobFromImage(cv2.resize(image , (300,300)) , 1.0 ,
	    					 (300,300) , (104.0 , 177.0 , 123.0))


print("Computing Object Detections")
net.setInput(blob)                           # Passing the blob
detections = net.forward()					 # 

# loop over the detections
for i in range(0, detections.shape[2]):
	# extract the confidence (i.e., probability) associated with the
	# prediction
	confidence = detections[0, 0, i, 2]
	# filter out weak detections by ensuring the `confidence` is
	# greater than the minimum confidence
	if confidence > args["confidence"]:
		# compute the (x, y)-coordinates of the bounding box for the
		# object
		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")
 
		# draw the bounding box of the face along with the associated
		# probability
		text = "{:.2f}%".format(confidence * 100)
		y = startY - 10 if startY - 10 > 10 else startY + 10
		cv2.rectangle(image, (startX, startY), (endX, endY),
			(0, 0, 255), 2)
		cv2.putText(image, text, (startX, y),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)


#python face-detect-image.py --image deep-learning-face-detection\rooster.jpg --prototxt cv-models\deploy.prototxt.txt \
#	--model cv-models\res10_300x300_ssd_iter_140000.caffemodel
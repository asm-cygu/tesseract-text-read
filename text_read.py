import cv2
import pytesseract
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", type=str,
	help="path to input image")
args = vars(ap.parse_args())

#pytesseract.pytesseract.tesseract_cmd = args["path"]

img = cv2.imread(args["path"])
text = pytesseract.image_to_string(img)
print("Result: " + text)
f = open(args["path"] + ".txt", "w")
f.write(text.encode("utf-8"))
f.close()

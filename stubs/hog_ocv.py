import cv2
import os
hog = cv2.HOGDescriptor()

LOCAL_PATH = os.path.dirname(os.path.realpath(__file__))
im = cv2.imread(LOCAL_PATH + '/robot.jpg')
h = hog.compute(im)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

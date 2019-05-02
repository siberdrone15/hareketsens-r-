import cv2

def diffres(t0, t1, t2):

  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)

  return cv2.bitwise_and(d1, d2)

cam = cv2.VideoCapture(0)
winName = "Sensor:)"

cv2.namedWindow(winName)

a = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

b = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

c = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

while True:

  cv2.imshow( winName, diffres(a,b,c) )

  a = b

  b = c

  c = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

  key = cv2.waitKey(10)

  if key == 27:

    cv2.destroyWindow(winName)

    break

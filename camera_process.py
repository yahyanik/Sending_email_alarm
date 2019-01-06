import cv2
import imutils


fgbg = cv2.createBackgroundSubtractorMOG2()

video_source = 0

def center(self, box):

    p1 = int(box[0]) + int(box[2]) / 2
    p2 = int(box[1]) + int(box[3]) / 2

    return [p1, p2]

def AllCenter(self, cent):

    if len(cent[0]) != 0:
        p1 = sum(cent[0]) / len(cent[0])
        p2 = sum(cent[1]) / len(cent[1])
    else:
        p1 = None
        p2 = None

    return (p1, p2)



camera = cv2.VideoCapture(video_source)
if not camera.isOpened():
    raise RuntimeError('Could not start camera.')
while True:
            # read current frame
    _, img = camera.read()
    frame1 = imutils.resize(img, width=min((600, img.shape[1])))
    blur = cv2.GaussianBlur(frame1, (21, 21), 0)
    fgmask = fgbg.apply(blur)
    _, thresh = cv2.threshold(fgmask, 100, 255, 50)
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        k1 = Camera.center((x, y, w, h))[0]
        k2 = Camera.center((x, y, w, h))[1]
        if box[0] <= k1 < box[1] and box[2] <= k2 < box[3]:
            cent[0].append(k1)
            cent[1].append(k2)
    get = self.AllCenter(cent)
#######################################################################################################################################






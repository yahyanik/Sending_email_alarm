import cv2
import imutils
import email_send_request
import time


fgbg = cv2.createBackgroundSubtractorMOG2()

video_source = 0
tersh = 300



camera = cv2.VideoCapture(video_source)
if not camera.isOpened():
    raise RuntimeError('Could not start camera.')
while True:
    flag_to_send_email = False
            # read current frame
    _, img = camera.read()
    frame1 = imutils.resize(img, width=min((600, img.shape[1])))
    blur = cv2.GaussianBlur(frame1, (21, 21), 0)
    fgmask = fgbg.apply(blur)
    _, thresh = cv2.threshold(fgmask, 100, 255, 50)
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        if (w*h) >= tersh:
            flag_to_send_email = True


    if flag_to_send_email:
        print 'emil sent!'
        email_send_request.RequestEmail.request()
        time.sleep(60*30)



#######################################################################################################################################






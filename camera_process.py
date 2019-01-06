import cv2
import imutils
import email_send_request
import time


fgbg = cv2.createBackgroundSubtractorMOG2()

video_source = "./WIN_20181102_16_16_56_Pro.mp4"
tersh = 1000



camera = cv2.VideoCapture(video_source)
if not camera.isOpened():
    raise RuntimeError('Could not start camera.')
_, img = camera.read()
while True:
    flag_to_send_email = False
    _, img = camera.read()
    frame1 = imutils.resize(img, width=min((600, img.shape[1])))
    blur = cv2.GaussianBlur(frame1, (21, 21), 0)
    fgmask = fgbg.apply(blur)
    _, thresh = cv2.threshold(fgmask, 100, 255, 50)
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        if (w*h) >= tersh and (w*h)< (frame1.shape[1]*frame1.shape[0]):
            flag_to_send_email = True
            cv2.rectangle(frame1, (x, y), (w, h), (200, 0, 0), 3)

    cv2.imshow('tracking', frame1)

    if flag_to_send_email:
        print 'email sent!'
        email_send_request.request()
        time.sleep(60*10)
    k = cv2.waitKey(200)
    if k == 7: break



#######################################################################################################################################






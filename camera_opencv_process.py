import cv2
import imutils
from base_camera import BaseCamera


class Camera(BaseCamera):
    video_source = "./WIN_20181102_16_16_56_Pro.mp4"

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()
            frame1 = imutils.resize(img, width=min((600, img.shape[1])))
            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', frame1)[1].tobytes()
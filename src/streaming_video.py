import cv2

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .functions.hand_keypoint import detect_hand_keypoints
from .functions.card_hand import circulate


class VideoStreamThread(QThread): 
    change_pixmap = Signal(QPixmap)

    def run(self):
        cap = cv2.VideoCapture(0)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        while True:
            ret, frame = cap.read()
            if ret:
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                finger, img = detect_hand_keypoints(width, height, rgb_image)
                if finger is not None:
                    print(finger)
                    ans = circulate(self, self.card, finger)
                    if ans is not None:
                        cv2.putText(
                            img, text='match=%s ' % (ans), org=(10, 30),
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=3,
                            color=255, thickness=3
                        )
                h, w, ch = img.shape
                bytes_per_line = ch * w
                convert_to_qt_format = QImage(img.data, w, h, bytes_per_line, QImage.Format_RGB888)
                p = convert_to_qt_format.scaled(640, 480, Qt.KeepAspectRatio)
                self.change_pixmap.emit(QPixmap.fromImage(p))
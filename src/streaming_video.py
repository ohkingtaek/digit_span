import cv2
import pyrealsense2 as rs
import numpy as np

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .functions.hand_keypoint import detect_hand_keypoints
from .functions.card_hand import circulate


class VideoStreamThread(QThread): 
    change_pixmap = Signal(QPixmap)

    def run(self):
        pipeline = rs.pipeline()
        config = rs.config()

        pipeline_wrapper = rs.pipeline_wrapper(pipeline)
        pipeline_profile = config.resolve(pipeline_wrapper)
        device = pipeline_profile.get_device()
        device_product_line = str(device.get_info(rs.camera_info.product_line))

        found_rgb = False
        for s in device.sensors:
            if s.get_info(rs.camera_info.name) == 'RGB Camera':
                found_rgb = True
                break
        if not found_rgb:
            print("The demo requires Depth camera with Color sensor")
            exit(0)

        config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

        if device_product_line == 'L500':
            config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
        else:
            config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

        # Start streaming
        pipeline.start(config)
        # width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        # height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        while True:
            frames = pipeline.wait_for_frames()
            depth_frame = frames.get_depth_frame()
            color_frame = frames.get_color_frame()

            # Convert images to numpy arrays
            depth_image = np.asanyarray(depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())

            depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

            depth_colormap_dim = depth_colormap.shape

            resized_color_image = cv2.resize(color_image, dsize=(depth_colormap_dim[1], depth_colormap_dim[0]), interpolation=cv2.INTER_AREA)
            rgb_image = resized_color_image
            # rgb_image = cv2.cvtColor(images, cv2.COLOR_BGR2RGB)
            finger, img = detect_hand_keypoints(640, 480, rgb_image)
            if finger is not None:
                print(finger)
                ans = circulate(self, self.card, finger)
                if ans is not None:
                    cv2.putText(
                        img, text='match=%s ' % (ans), org=(50, 30),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=255, thickness=3
                    )
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # img = cv2.rectangle(img, 
            #     (int(self.card.loc[0]['xmin']), 
            #     int(self.card.loc[0]['ymin']), 
            #     int(self.card.loc[0]['xmax']),
            #     int(self.card.loc[0]['ymax'])
            #     ))
            h, w, ch = img.shape
            bytes_per_line = ch * w
            convert_to_qt_format = QImage(img.data, w, h, bytes_per_line, QImage.Format_RGB888)
            p = convert_to_qt_format.scaled(640, 480, Qt.KeepAspectRatio)
            self.change_pixmap.emit(QPixmap.fromImage(p))
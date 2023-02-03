import sys
import shutil
import schedule
import collections

import pandas as pd
import cv2
from PIL import Image

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from src.gui.ui_window import UI_MainWindow
from src.functions.card_detection import card_detect
from src.functions.image_process import image_save_yolo
from src.streaming_video import VideoStreamThread


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.temp = None
        self.setWindowTitle("Game")
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        self.ui.ui_pages.btn_1.clicked.connect(self.show_page_1)
        self.ui.ui_pages.btn_2.clicked.connect(self.load_image)
        self.ui.ui_pages.btn_3.clicked.connect(self.show_page_2)
        self.ui.ui_pages.btn_4.clicked.connect(self.streaming_video)

        self.show()

    def show_page_1(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
    
    def show_page_2(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)

    def load_image(self):
        frames = self.image_save()
        self.card_detection(frames)

        img_path = 'runs/detect/exp/img1.jpg'
        img = cv2.imread(img_path)
        img = cv2.resize(img, (640, 480))
        self.temp = img
        h, w, _ = img.shape
        bytes_per_line = 3 * w

        qimg = QImage(
            img, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()

        pixmap = QPixmap(qimg)
        self.ui.ui_pages.label_1.setPixmap(pixmap)
        # schedule.every(4).seconds.do(self.card_detection)
        
    def image_save(self):
        captured_num = image_save_yolo()
        return captured_num

    def card_detection(self, frames): 
        image = './assets/img/img'+str(frames)+'.jpg'
        image = Image.open(image)
        card = card_detect(image)
        if card is None:
            print('Card None')#break
        print(card)

        #card data preprocess
        card = card.astype({'xmin': 'float', 'ymin': 'float', 'xmax': 'float', 
        'ymax': 'float', 'confidence': 'float', 'class': 'int', 'name': 'string'})
        card.sort_values(['class'], axis=0, ascending=True, inplace=True)
        cls = card['class'].values
        counts = collections.Counter(cls)
        for i, d in counts.items():
            if d % 2 != 0:
                print(i, d)
                card.drop(card[card['class'] == i].index, axis=0, inplace=True)
                #break
        card.reset_index(drop=True, inplace=True)

        lis = list()
        if card.iloc[0]['xmin'] < card.iloc[1]['xmin']:
            lis.append([card.iloc[0]['xmin'], card.iloc[0]['ymin'], card.iloc[1]['xmax'], card.iloc[1]['ymax'], card.iloc[0]['name']])
        else:
            lis.append([card.iloc[1]['xmin'], card.iloc[1]['ymin'], card.iloc[0]['xmax'], card.iloc[0]['ymax'], card.iloc[0]['name']])
        #break + only one

        card.drop(card.index[0:], inplace=True)
        card.drop(['confidence', 'class'], axis=1, inplace=True)
        card.loc[0] = lis[0] #only one
        self.df = card.copy()

    def streaming_video(self):
        self.thread = VideoStreamThread(self)
        self.thread.change_pixmap.connect(self.set_image)
        self.thread.start()

    def set_image(self, image):
        self.ui.ui_pages.label_2.setPixmap(image)

if __name__ == "__main__":
    dir = 'runs/detect'
    try:
        shutil.rmtree(dir)
    except FileNotFoundError:
        pass
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("assets/icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())

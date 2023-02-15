from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(1400, 960)
        
        #Page 1
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        
        self.main_layout_1 = QVBoxLayout(self.page_1)
        self.main_layout_1.setObjectName(u"main_layout_1")
        
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1400, 960))
        self.frame.setMaximumSize(QSize(1400, 960))

        self.sub_layout_1 = QHBoxLayout(self.frame)
        self.sub_layout_1.setAlignment(Qt.AlignCenter)

        self.btn_1 = QPushButton("Game start")
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setMinimumSize(QSize(200, 80))
        self.btn_1.setMaximumSize(QSize(200, 80))
        self.sub_layout_1.addWidget(self.btn_1)

        application_pages.addWidget(self.page_1)


        #Page 2
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")

        self.main_layout_2 = QVBoxLayout(self.page_2)
        self.main_layout_2.setObjectName(u"main_layout_2")
        
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(1400, 960))
        self.frame_2.setMaximumSize(QSize(1400, 960))

        self.sub_layout_2 = QVBoxLayout(self.frame_2)
        self.sub_layout_2.setAlignment(Qt.AlignCenter)

        self.label_1 = QLabel()
        self.label_1.setObjectName(u"label_1")
        self.label_1.setFixedSize(640, 480)
        self.sub_layout_2.addWidget(self.label_1)

        self.btn_2 = QPushButton("Card_Load")
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setFixedSize(200, 100)
        self.sub_layout_2.addWidget(self.btn_2)
        
        self.btn_3 = QPushButton("Next")
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setFixedSize(200, 100)
        self.sub_layout_2.addWidget(self.btn_3)

        application_pages.addWidget(self.page_2)

        
        #Page 3
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")

        self.main_layout_3 = QVBoxLayout(self.page_3)
        self.main_layout_3.setObjectName(u"main_layout_3")
        
        self.frame_3 = QFrame(self.page_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(1400, 960))
        self.frame_3.setMaximumSize(QSize(1400, 960))

        self.sub_layout_3 = QHBoxLayout(self.frame_3)
        self.sub_layout_3.setAlignment(Qt.AlignCenter)

        self.label_2 = QLabel()
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFixedSize(640, 480)
        self.sub_layout_3.addWidget(self.label_2)

        self.btn_4 = QPushButton("Start")
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setFixedSize(200, 100)
        self.sub_layout_3.addWidget(self.btn_4)

        application_pages.addWidget(self.page_3)

        self.retranslateUi(application_pages)

        QMetaObject.connectSlotsByName(application_pages)

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
from PyQt5.QtWidgets import QWidget,QPushButton,QHBoxLayout
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QObject


class MyButtonsWidget(QWidget,QObject):


    DEFAULT_WIDTH_DEL_BTN  = 100
    """This is custom class, which allow move buttons
    on widget in a necessary place   """

    def __init__(self):
        super(MyButtonsWidget, self).__init__()
        self.create_buttons()
        self.set_layout(self.create_layout())
        self.__painter = QPainter()

    @property
    def painter(self):
        return self.__painter

    def create_buttons(self):
        self.btn_back = QPushButton("Back", self)
        self.btn_back.setStyleSheet("background-color: rgb(255,167,167)")

        self.btn_del_photo = QPushButton("Delete photo",self)
        self.btn_delete_all_photos = QPushButton("Delete all photos", self)
        self.btn_add_new_photos = QPushButton("Add new photos", self)
        self.btn_save_post = QPushButton("SavePost", self)

    def create_layout(self):
        qhb = QHBoxLayout()
        qhb.addWidget(self.btn_del_photo)
        qhb.addWidget(self.btn_back)
        qhb.addWidget(self.btn_delete_all_photos)
        qhb.addWidget(self.btn_add_new_photos)
        qhb.addWidget(self.btn_save_post)
        qhb.setContentsMargins(0,0,0,0)
        return qhb

    def set_layout(self,layout):
        self.setLayout(layout)

    def set_width_for_del_btn(self,width):
        if width:
            self.btn_del_photo.setFixedWidth(width)
        else:
            self.btn_del_photo.setFixedWidth(MyButtonsWidget.DEFAULT_WIDTH_DEL_BTN)

    def toggle_show_edit_buttons(self, images_count):
        if images_count == 0 :
            self.btn_del_photo.hide()
            self.btn_delete_all_photos.hide()
        elif images_count == 1:
            self.btn_del_photo.show()
            self.btn_delete_all_photos.hide()
        else:
            self.btn_del_photo.show()
            self.btn_delete_all_photos.show()

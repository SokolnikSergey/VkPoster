from PyQt5.QtWidgets import QWidget,QTextEdit,QVBoxLayout
from PyQt5.QtCore import QObject,pyqtSignal
from PyQt5.QtGui import QFont
from view.EditPost.MyPicturesWidget import MyPicturesWidget
from view.EditPost.MyButtonsWidget import MyButtonsWidget


class EditPostWindow(QWidget,QObject):

    edit_post_closed = pyqtSignal()
    WIDTH_FOR_PHOTOS,HEIGHT_FOR_PHOTOS = 300,300

    def __init__(self):
        super(EditPostWindow, self).__init__()
        self.setting_window()
        self.create_and_setting_text_edit("")
        self.__widget_for_photos = MyPicturesWidget(EditPostWindow.WIDTH_FOR_PHOTOS,EditPostWindow.HEIGHT_FOR_PHOTOS,[],5)
        self.__widget_for_buttons = MyButtonsWidget()
        self.setLayout(self.create_layouts())


    @property
    def widget_for_photos(self):
        return self.__widget_for_photos
    @property
    def widget_for_buttons(self):
        return self.__widget_for_buttons

    @property
    def text_edit(self):
        return self.__text_edit

    def setting_window(self):
        self.setWindowTitle("Change Post")
        self.setGeometry(20,40,1000,600)


    def create_and_setting_text_edit(self,text):
        self.__text_edit = QTextEdit(self)
        self.__text_edit.setText(text)
        self.__text_edit.setFont(QFont("Times New Roman",15))



    def my_resize(self):
        self.widget_for_buttons.set_width_for_del_btn(self.widget_for_photos.get_first_picture_size().width())

    def resizeEvent(self, QResizeEvent):
        self.my_resize()

    def create_layouts(self):
        qv_box = QVBoxLayout()

        qv_box.addWidget(self.text_edit,2)
        qv_box.addSpacing(5)
        qv_box.addWidget(self.widget_for_photos,10)
        qv_box.addSpacing(20)
        qv_box.addWidget(self.widget_for_buttons,1)

        return qv_box


    def closeEvent(self, QCloseEvent):
        self.edit_post_closed.emit()
        QCloseEvent.accept()

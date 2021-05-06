from PyQt5.QtWidgets import QWidget,QPushButton,QListWidget,QHBoxLayout,QVBoxLayout
from PyQt5.QtCore import QObject,pyqtSignal
from PyQt5.QtGui import QIcon
from view.AuxiliaryElements.BlinkingText import BlinkingText

class ChosePostWindow(QWidget,QObject):

    choose_post_closed = pyqtSignal()


    def __init__(self):
        super(ChosePostWindow, self).__init__()
        self.setting_window()
        self.create_buttons()
        self.create_list_widget_and_setting()
        self.__blinking_label.start_blinking()
        self.set_layout()
        self.setWindowIcon(QIcon('../../model/AuxElements/icon.png'))


    def setting_window(self):
        self.setWindowTitle("Edit Post")
        self.setGeometry(100,100,500,500)

    def create_buttons(self):
        self.btn_delete_post = QPushButton("Delete Post")
        self.btn_delete_post.setMinimumHeight(30)

        self.btn_add_new_post = QPushButton("Add New Post")
        self.btn_add_new_post.setMinimumHeight(30)

        self.btn_backed = QPushButton("Back")
        self.btn_backed.setMinimumHeight(30)
        self.btn_backed.setStyleSheet("background-color: rgb(255,167,167)")

        self.__blinking_label = BlinkingText('Hint: Double click on post to start edit')

    def create_list_widget_and_setting(self):
        self.list_post_widget = QListWidget(self)
        self.list_post_widget.setSelectionMode(QListWidget.SingleSelection)

    def creating_layouts(self,obj_for_qv = None ,obj_for_qh = None):

        qv_b = QVBoxLayout()
        qh_b = QHBoxLayout()

        if None is not obj_for_qv:
            for obj in obj_for_qv:
                qv_b.addWidget(obj)

        if None is not obj_for_qh:
            for obj in obj_for_qh:
                qh_b.addWidget(obj)
        qv_b.addLayout(qh_b)

        return qv_b

    def set_layout(self):
        self.setLayout(self.creating_layouts([self.__blinking_label.info_label, self.list_post_widget],
                    [self.btn_backed,self.btn_add_new_post,self.btn_delete_post]))


    def closeEvent(self, QCloseEvent):
        self.choose_post_closed.emit()
        QCloseEvent.accept()


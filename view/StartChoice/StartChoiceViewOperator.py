from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QPainter,QColor,QPen,QLinearGradient
from PyQt5.Qt import Qt


class StartChoiceViewOperator(QObject):
    
    change_account = pyqtSignal()
    btn_post_to_group_pressed = pyqtSignal()
    btn_settings_pressed = pyqtSignal()

    def __init__(self, view):
        super(StartChoiceViewOperator, self).__init__()
        self.__view = view
        self.__painter = QPainter()
        self.snapping_signals()

    def snapping_signals(self):
        self.__view.btn_spammer_vk.clicked.connect(self.btn_post_to_group_pressed)
        self.__view.btn_change_account.clicked.connect(self.change_account)
        self.__view.settings_btn.clicked.connect(self.btn_settings_pressed)

    def show(self):
        self.__view.show()

    def hide(self):
        self.__view.hide()

    ################# The section of updating progress
    def update_posts_progress(self,done,remainded,fail):
        self.__view.btn_spammer_vk.amount_remainded = remainded
        self.__view.btn_spammer_vk.amount_done = done
        self.__view.btn_spammer_vk.amount_failed = fail

    ################# The section for updating and filling ProfileInfoWidget

    def update_account_data(self, first_name, last_name, ava):
        self.update_first_name(first_name)
        self.update_last_name(last_name)
        self.update_picture(ava)

    def update_picture(self,ava):
        if ava:
            self.__view.profile_info_widget.pict_lbl.setPixmap(ava)

    def update_first_name(self, new_first_name):
        self.__view.profile_info_widget.first_name_lbl.setText(new_first_name)

    def update_last_name(self, new_last_name):
        self.__view.profile_info_widget.last_name_lbl.setText(new_last_name)


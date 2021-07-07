from PyQt5.QtWidgets import QWidget,QSlider,QVBoxLayout,QHBoxLayout,QLCDNumber,\
    QCheckBox,QPushButton,QComboBox,QLabel
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSignal


class SettingsWindow(QWidget):

    window_closed = pyqtSignal()

    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.setup_window()
        self.create_scrolls()
        self.create_lcd_numbers()
        self.create_lables()
        self.create_check_boxes()
        self.create_comboboxes()
        self.create_buttons()
        self.setup_style()
        self.set_layouts()

    def setup_window(self):
        self.setWindowTitle("Settings")
        self.setGeometry(100,100,500,500)

    def setup_style(self):
        self.setStyleSheet("QPushButton {font: bold 14px; background-color: rgb(6, 50, 200)}"
                           "QLabel { font: bold 15px ; color: rgb(0,50,200) } "
                           "QLCDNumber {border : 0px;} "
                           "QCheckBox {font: bold 15px ; color: rgb(6, 50, 200)}")

    def create_lables(self):
        self.lbl_change_country = QLabel("Country to send -> ")
        self.lbl_amount_of_groups = QLabel("Max amount of groups to one search: ")
        self.lbl_amount_of_users = QLabel("Min amount of users in groups: ")
        self.lbl_timeout = QLabel("Timeout between operations(sec): ")

    def create_comboboxes(self):
        self.country_id_combobx = QComboBox(self)
        self.country_id_combobx.addItems(["Россия","Украина","Беларусь"])
        self.country_id_combobx.setCurrentIndex(2)
        self.country_id_combobx.update()


    def create_scrolls(self):
        self.timeout_scroll = QSlider(Qt.Horizontal,self)

        self.timeout_scroll.setPageStep(1)
        self.timeout_scroll.setTickPosition(2)
        self.timeout_scroll.setRange(5,30)

        self.max_amount_groups_scroll = QSlider(Qt.Horizontal,self)
        self.max_amount_groups_scroll.setPageStep(5)
        self.max_amount_groups_scroll.setTickPosition(2)
        self.max_amount_groups_scroll.setRange(5, 150)

        self.min_amount_users_scroll = QSlider(Qt.Horizontal, self)
        self.min_amount_users_scroll.setPageStep(500)
        self.min_amount_users_scroll.setTickPosition(2)
        self.min_amount_users_scroll.setMinimum(25)

        self.min_amount_users_scroll.setRange(25, 20000)

    def create_buttons(self):
        self.save_btn = QPushButton("Save Changes",self)

        self.btn_back = QPushButton("Back", self)
        self.btn_back.setStyleSheet("background-color: rgb(255,167,167)")

    def create_check_boxes(self):
        self.each_to_each_check_box = QCheckBox("Each Post to Each Group",self)
        self.just_once_limit_reached_check_box = QCheckBox("Show sendings limit reached just once", self)

    def create_lcd_numbers(self):
        self.lcd_timeout  = QLCDNumber(self)
        self.lcd_timeout.display(5)

        self.lcd_max_amount = QLCDNumber(self)
        self.lcd_max_amount.display(5)

        self.lcd_min_amount_users = QLCDNumber(self)
        self.lcd_min_amount_users.display(100)

    def set_layouts(self):

        self.qh_country_id = QHBoxLayout()
        self.qh_country_id.addWidget(self.lbl_change_country,1)
        self.qh_country_id.addWidget(self.country_id_combobx,3)

        self.qh_timeout = QHBoxLayout()
        self.qh_timeout.addWidget(self.timeout_scroll)
        self.qh_timeout.addWidget(self.lcd_timeout)

        self.qh_max_amount  = QHBoxLayout()
        self.qh_max_amount.addWidget(self.max_amount_groups_scroll)
        self.qh_max_amount.addWidget(self.lcd_max_amount)

        self.qh_min_amount_users = QHBoxLayout()
        self.qh_min_amount_users.addWidget(self.min_amount_users_scroll)
        self.qh_min_amount_users.addWidget(self.lcd_min_amount_users)

        self.qh_each = QHBoxLayout()
        self.qh_each.addWidget(self.each_to_each_check_box)

        self.qh_limit_reached = QHBoxLayout()
        self.qh_limit_reached.addWidget(self.just_once_limit_reached_check_box)

        self.qh_save_back = QHBoxLayout()
        self.qh_save_back.addWidget(self.btn_back)
        self.qh_save_back.addWidget(self.save_btn)


        self.qv_box1 = QVBoxLayout()

        self.qv_box1.addLayout(self.qh_country_id,1)
        self.qv_box1.addWidget(self.lbl_timeout,1)
        self.qv_box1.addLayout(self.qh_timeout,1)
        self.qv_box1.addWidget(self.lbl_amount_of_groups,1)
        self.qv_box1.addLayout(self.qh_max_amount,1)
        self.qv_box1.addWidget(self.lbl_amount_of_users,1)
        self.qv_box1.addLayout(self.qh_min_amount_users,1)
        self.qv_box1.addLayout(self.qh_each)
        self.qv_box1.addLayout(self.qh_limit_reached)
        self.qv_box1.addLayout(self.qh_save_back)

        self.setLayout(self.qv_box1)

    def closeEvent(self, close_event):
        close_event.ignore()
        self.window_closed.emit()

from PyQt5.QtWidgets import QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QCheckBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal


from view.AuxiliaryElements.ListWidgetCustomScroll import ListWidgetCustomScroll
from view.AuxiliaryElements.BlinkingText import BlinkingText


class PostToGroupWindow(QWidget):
    btn_make_resendings_clicked = pyqtSignal()

    def __init__(self):
        super(PostToGroupWindow, self).__init__()
        self.__resend_button_on_ui = False
        self.setting_group_post_window()
        self.create_buttons_and_labels()
        self.create_layouts()
        self.blinking_label.info_label.hide()
        self.setWindowIcon(QIcon('../../model/AuxElements/icon.png'))


    def setting_group_post_window(self):
        self.setGeometry(100, 100, 956, 700)
        self.setWindowTitle("Send Posts To Groups")

    def create_buttons_and_labels(self):
        self.lable_amount_actions = QLabel("Amount Actions to Execute = 0")
        self.check_box_all_ticks_groups = QCheckBox("Remove all ticks ",self)

        self.btn_help = QPushButton("Help",self)
        self.btn_help.setStyleSheet("color: rgb(0,0,255)")


        self.btn_recover_actions = QPushButton("Recover Delayed Actions",self)
       # self.btn_recover_actions.setStyleSheet("color: rgb(200,20,255)")

        self.list_post_widget = ListWidgetCustomScroll()

        self.list_group_widget = ListWidgetCustomScroll()
        self.list_group_widget.setMinimumHeight(150)

        self.btn_start_spam = QPushButton("Send Posts",self)
        self.btn_start_spam.setStyleSheet("background-color: rgb(123, 227, 150)")

        self.btn_start_spam.setFont(QFont("Arial",20))
        self.btn_start_spam.setMinimumHeight(50)

        self.btn_edit_post = QPushButton("Edit posts",self)
        self.line_post_name  = QLineEdit()
        self.btn_back = QPushButton("Back",self)
        self.btn_back.setStyleSheet("background-color: rgb(255,167,167)")
        self.btn_read_all_records = QPushButton("Recover saved posts", self)

        self.primary_group_key_label = QLabel("Input primary word of group")
        self.btn_search_groups = QPushButton("Search Groups")

        self.posts_label = QLabel("Posts to send:")
        self.groups_label = QLabel("Searched groups:")



        self.blinking_label = BlinkingText('Images for post are in progress of uploading...')

    def append_resending_button(self, button_text = 'resend posts'):
        if not self.__resend_button_on_ui:
            self.btn_make_resendings = QPushButton(button_text, self)
            self.btn_make_resendings.clicked.connect(self.btn_make_resendings_clicked)
            self.qh_box2.addWidget(self.btn_make_resendings)
            self.__resend_button_on_ui = True
        else:
            self.btn_make_resendings.setText(button_text)

    def remove_resending_button(self):
        if self.__resend_button_on_ui:
            self.btn_make_resendings.deleteLater()
            self.__resend_button_on_ui = False


    def create_layouts(self):
        #######creating layouts

        self.qh_box0 = QHBoxLayout()
        self.qh_box = QHBoxLayout()
        self.qh_box2 = QHBoxLayout()
        self.qh_box3 = QHBoxLayout()
        self.qh_box4 = QHBoxLayout()


        self.qh_box0.addWidget(self.lable_amount_actions)
        self.qh_box.addWidget(self.btn_back, 10)
        self.qh_box.addWidget(self.btn_edit_post,10)
        self.qh_box2.addWidget(self.primary_group_key_label)
        self.qh_box2.addWidget(self.line_post_name)
        self.qh_box2.addWidget(self.btn_search_groups)

        self.qh_box3.addWidget(self.btn_read_all_records)
        self.qh_box3.addWidget(self.btn_help)
        self.qh_box3.addWidget(self.btn_recover_actions)
        self.qh_box4.addWidget(self.check_box_all_ticks_groups)


        self.qv_box = QVBoxLayout()
        self.qv_box.addLayout(self.qh_box0)
        self.qv_box.addLayout(self.qh_box3)
        self.qv_box.addWidget(self.posts_label)
        self.qv_box.addWidget(self.list_post_widget)
        self.qv_box.addLayout(self.qh_box2)
        self.qv_box.addLayout(self.qh_box4)
        self.qv_box.addWidget(self.groups_label)
        self.qv_box.addWidget(self.list_group_widget)

        self.qv_box.addWidget(self.btn_start_spam)
        self.qv_box.addWidget(self.blinking_label.info_label)

        self.qv_box.addLayout(self.qh_box)

        self.setLayout(self.qv_box)
from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QSizePolicy
from view.MyProgressButton.MyProgressButton import MyProgressButton
from view.StartChoice.ProfileInfoWidget import ProfileInfoWidget
from PyQt5.QtGui import QIcon


class StartChoiceWindow(QWidget):
    def __init__(self):
        super(StartChoiceWindow, self).__init__()

        self.setting_beginner_window()
        self.create_profile_info_widget()
        self.create_buttons_and_labels()
        self.create_and_set_layout()


    def setting_beginner_window(self):
        self.setGeometry(100, 50, 500, 275)
        self.setWindowTitle("Choose Type")
        self.setWindowIcon(QIcon('../../model/AuxElements/icon.png'))

    def create_buttons_and_labels(self) :
        self.btn_spammer_vk = MyProgressButton("Posts To Group",self) #text,parent,done,remainded,failed
        self.btn_spammer_vk.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)

        self.settings_btn = QPushButton("Settings", self)
        self.settings_btn.setSizePolicy(QSizePolicy.MinimumExpanding,QSizePolicy.MinimumExpanding)

        self.btn_change_account = QPushButton("Change Account", self)
        self.btn_change_account.setSizePolicy(QSizePolicy.MinimumExpanding,QSizePolicy.MinimumExpanding)


    def create_and_set_layout(self):

        self.qh_settings_change_acc = QHBoxLayout()
        self.qh_settings_change_acc.addWidget(self.settings_btn)
        self.qh_settings_change_acc.addWidget(self.btn_change_account)

        self.qv_box = QVBoxLayout()

        self.qv_box.addWidget(self.profile_info_widget,0)
        self.qv_box.addWidget(self.btn_spammer_vk)

        self.qv_box.addLayout(self.qh_settings_change_acc)
        self.setLayout(self.qv_box)

    def create_profile_info_widget(self):
        self.profile_info_widget = ProfileInfoWidget(self)
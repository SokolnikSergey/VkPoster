from PyQt5.QtWidgets import QMessageBox
from PyQt5.Qt import Qt
from PyQt5.QtCore import QObject,pyqtSignal
from PyQt5.QtGui import QIcon

class ExceptionWarning(QMessageBox,QObject):

    accepted  = pyqtSignal()
    declined  = pyqtSignal()

    def __init__(self,message):
        super(ExceptionWarning, self).__init__()
        self.setText(message)
        self.setting_window()
        self.setWindowIcon(QIcon('../../model/AuxElements/icon.png'))
        self.buttonClicked.connect(self.btn_clicked)

    def setting_window(self):
        self.setModal(True)
        self.setWindowModality(Qt.ApplicationModal)
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    def btn_clicked(self,btn):
        role = self.buttonRole(btn)
        if role == 0 :
            self.accepted.emit()

        elif role == 1:
            self.declined.emit()

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon


class AcceptLeaveApp(QMessageBox):
    def __init__(self ):
        super(AcceptLeaveApp, self).__init__()
        self.setWindowIcon(QIcon('../../model/AuxElements/icon.png'))
        self.setWindowTitle('Need authorization')
        self.set_texts()
        self.set_buttons(QMessageBox.Ok,QMessageBox.Ok,QMessageBox.Cancel)

    def set_texts(self,main_text =  "Need authorization" ,auxiliary_info = "Application doesn't work without signed in account"):
        self.setText(main_text)
        self.setInformativeText(auxiliary_info)

    def set_buttons(self,default_button,*buttons):
        for button in buttons:
            self.addButton(button)
        self.setDefaultButton(default_button)


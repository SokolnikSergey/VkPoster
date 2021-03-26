from PyQt5.QtWidgets import QMessageBox


class AcceptLeaveApp(QMessageBox):
    def __init__(self):
        super(AcceptLeaveApp, self).__init__()
        self.setWindowTitle('Need authorization')
        self.set_texts("Application doesn't work without signed in account",
                       "Start authorization?")

        self.set_buttons(QMessageBox.Ok,QMessageBox.Ok,QMessageBox.Cancel)

    def set_texts(self,main_text,auxiliary_info):
        self.setText(main_text)
        self.setInformativeText(auxiliary_info)

    def set_buttons(self,default_button,*buttons):
        for button in buttons:
            self.addButton(button)
        self.setDefaultButton(default_button)


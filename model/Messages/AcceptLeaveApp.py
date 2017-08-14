from PyQt5.QtWidgets import QMessageBox


class AcceptLeaveApp(QMessageBox):
    def __init__(self):
        super(AcceptLeaveApp, self).__init__()
        self.set_texts("Do you want leave application?",
                       "Application doesn't work without authorization")

        self.set_buttons(QMessageBox.Cancel,QMessageBox.Ok,QMessageBox.Cancel)

    def set_texts(self,main_text,auxiliary_info):
        self.setText(main_text)
        self.setInformativeText(auxiliary_info)

    def set_buttons(self,default_button,*buttons):
        for button in buttons:
            self.addButton(button)
        self.setDefaultButton(default_button)


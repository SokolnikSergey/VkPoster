
from PyQt5.QtWidgets import QFileDialog


class MyFileDialog(QFileDialog):

    def __init__(self):
        super(MyFileDialog,self).__init__()
        self.setting_window()
        print(123)

    def setting_window(self):
        self.setGeometry(100,100,500,500)
        self.setViewMode(QFileDialog.Detail)
        self.setFileMode(QFileDialog.ExistingFiles)
        self.setOption(QFileDialog.ReadOnly,True)
        self.setNameFilters(["Images (*png *jpg *gif)","All (*.*)"])


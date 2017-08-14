from PyQt5.QtWidgets import QSplashScreen,QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import Qt

class SplashScreen(QSplashScreen):

    def __init__(self,path):
        super(SplashScreen, self).__init__()
        self.setPixmap(QPixmap(path))
        self.set_message("Loading comonents")

    def set_message(self,msg):
        self.showMessage(msg, Qt.AlignCenter | Qt.AlignBottom, Qt.red)

    def keyPressEvent(self, *args, **kwargs):
        pass







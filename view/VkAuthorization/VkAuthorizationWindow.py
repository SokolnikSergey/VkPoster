from PyQt5.QtCore import pyqtSignal,  QObject
from PyQt5.Qt import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView

class VkAuthWindow(QWebView,QObject):
    """This class for authorization and achieve token  """
    window_closed = pyqtSignal()

    def __init__(self):
        super(VkAuthWindow, self).__init__()
        self.window_setting()

    def window_setting(self):
        self.setFixedSize(800, 400)
        self.setWindowTitle("VkAuthorization")
        self.setWindowModality(Qt.ApplicationModal)

    def closeEvent(self,close_event):
        close_event.ignore()
        self.window_closed.emit()




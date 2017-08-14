from PyQt5.QtCore import QObject,pyqtSignal
from view.VkAuthorization.VkAuthorizationWindowOperator import VkAuthorizationWindowOperator
from view.VkAuthorization.VkAuthorizationWindow import VkAuthWindow
from model.VkAuthorizationModel.VkAuthorizationBinder import VkAuthorizationBinder


class VkAuthorizationModel(QObject):
    token_recieved_signal = pyqtSignal(str)
    auth_window_closed = pyqtSignal()

    PATH_TO_TOKEN_FILE = './AuxElements/token.bin'

    def __init__(self,application_id):
        super(VkAuthorizationModel, self).__init__()

        self.__view = None
        self.__application_id = application_id
        self.create_view()
        self.binder = VkAuthorizationBinder(self,self.__view)



    @property
    def application_id(self):
        return self.__application_id

    @application_id.setter
    def application_id(self, new_application_id):
        self.__application_id = new_application_id

    def start_authorization(self):
        self.__view.clear_page()
        self.__view.setStartUrl()

    def create_view(self):
        self.__view = VkAuthorizationWindowOperator(VkAuthWindow(),self.__application_id)

    def show(self):
        self.__view.show()

    def hide(self):
        self.__view.hide()

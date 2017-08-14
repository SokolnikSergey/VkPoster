from PyQt5.QtCore import pyqtSignal,QObject
from view.StartChoice.StartChoiceViewOperator import  StartChoiceViewOperator
from view.StartChoice.StartChoiceWindow import StartChoiceWindow
from model.StartChoiceModel.Binder import StartChoiceBinder

import os


class StartChoiceModel(QObject):
    change_account = pyqtSignal()
    post_to_group_pressed = pyqtSignal()
    setting_pressed  = pyqtSignal()

    progress_posts_changed = pyqtSignal(int,int,int) #done,remainded,failed


    def __init__(self,logger,publisher):
        super(StartChoiceModel, self).__init__()

        self.create_view()
        self.create_binder()
        self.__logger = logger

        self.publisher = publisher
        self.publisher.add_new_account_data_subscriber(self)

    def create_binder(self):
        self.binder = StartChoiceBinder(self.__start_choice_win_operator,self)

    def create_view(self):
        self.__start_choice_win_operator = StartChoiceViewOperator(StartChoiceWindow())


    def start_hepler(self):
        try :
            os.startfile("..\AuxElements\Helper.chm")

        except Exception as ex:
            self.__logger.change_name(self.__class__.__name__)
            self.__logger.exception(ex)

    def update_account_data(self,data):
        self.__start_choice_win_operator.update_account_data(*data)

    def show(self):
        self.__start_choice_win_operator.show()

    def hide(self):
        self.__start_choice_win_operator.hide()

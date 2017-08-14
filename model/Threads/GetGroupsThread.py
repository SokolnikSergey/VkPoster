from PyQt5.QtCore import QThread,pyqtSignal,QObject
from model.VkOperations.VkOperations import VkOperations

class GetGroupsThread(QThread,QObject):

    group_founded = pyqtSignal(list)

    def __init__(self,logger,vk_api,key_word = "",amount = 0,country_id = 3,min_amount_users = 20 ):
        self.__logger = logger
        self.__key_word = key_word
        self.__amount = amount
        self.__vk_api = vk_api
        self.__country_id = country_id
        self.__min_amount_users = min_amount_users

        super(GetGroupsThread, self).__init__()


    @property
    def key_word (self):
        return self.__key_word

    @key_word.setter
    def key_word(self,new_key_word):
        if(isinstance(new_key_word,str)):
            self.__key_word  = new_key_word

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self,new_amount):
        if (isinstance(new_amount,int)):
            self.__amount = new_amount

    @property
    def vk_api(self):
        return self.__vk_api

    @vk_api.setter
    def vk_api(self,new_vk_api):
        self.__vk_api = new_vk_api

    @property
    def country_id(self):
        return self.__country_id

    @country_id.setter
    def country_id(self,new_country_id):
        self.__country_id = new_country_id

    @property
    def min_amount_users(self):
        return self.__min_amount_users

    @min_amount_users.setter
    def min_amount_users(self, new_min_amount_users):
        self.__min_amount_users = new_min_amount_users

    def run(self):
        try:
            list_of_groups = VkOperations.search_groups_by_key_word(self.__vk_api,self.__key_word,
                                            self.__amount,self.__country_id,self.__min_amount_users)
            if list_of_groups is None:
                self.group_founded.emit([])
            else:
                self.group_founded.emit(list_of_groups)

            self.__logger.change_name(self.__class__.__name__)
            self.__logger.info("Groups have got")
        except Exception as ex:

            self.__logger.change_name(self.__class__.__name__)
            self.__logger.exception(ex)
from model.Interfaces.Publisher import Publisher
from PyQt5.QtGui import QPixmap
from model.DataUploadingVkOperations.DataUploadingVkOperations import DataUploadingVkOperations


class VkSessionData(Publisher):

    """Class-container . This is publisher class , that allow
    update account data if token changes."""
    def __init__(self,token = "",user_id = "",album_id = "",vk_api = None,
            avatar = None,first_name = "No First name" , last_name = "No Last Name"):

        self.__token = token
        self.__user_id = user_id
        self.__album_id = album_id
        self.__vk_api = vk_api
        self.__avatar = avatar
        self.__first_name = first_name
        self.__last_name = last_name

        self.__list_of_vk_api_subscribers = []
        self.__list_of_albim_id_subscribers = []
        self.__list_of_account_data_subscribers = []


    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self,new_token):
        self.__token = new_token

    @property
    def album_id(self):
        return self.__album_id

    @album_id.setter
    def album_id(self, new_album_id):
        self.__album_id = new_album_id
        self.album_id_changed(new_album_id)

    @property
    def vk_api(self):
        return self.__vk_api

    @vk_api.setter
    def vk_api(self, new_vk_api):
        self.__vk_api = new_vk_api
        self.vk_api_changed(self.__vk_api)

    @property
    def avatar(self):
        return self.__avatar

    @avatar.setter
    def avatar(self,ava):
        if(ava and isinstance(ava,QPixmap)):
            self.__avatar = ava

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self,new_first_name):
        if(new_first_name and isinstance(new_first_name,str)):
            self.__first_name = new_first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, new_last_name):
        if (new_last_name and isinstance(new_last_name, str)):
            self.__last_name = new_last_name


    def vk_api_changed(self,new_vk_api):
        for subscriber in self.__list_of_vk_api_subscribers:
            subscriber.vk_api_changed(new_vk_api)

    def album_id_changed(self,new_albim_id):
        for subscriber in self.__list_of_albim_id_subscribers:
            subscriber.album_id_changed(new_albim_id)

    def account_data_updated(self,data):
        for subdcriber in self.__list_of_account_data_subscribers:
            subdcriber.update_account_data(data)


    def add_new_subscriber(self, subscriber):
        self.__list_of_vk_api_subscribers.append(subscriber)
        subscriber.vk_api_changed(self.__vk_api)

    def remove_subscriber(self, subscriber):
        self.__list_of_vk_api_subscribers.remove(subscriber)

    def clear_all_subscribers(self):
        self.__list_of_vk_api_subscribers.clear()

    def add_new_aid_subscriber(self, subscriber):
        self.__list_of_albim_id_subscribers.append(subscriber)
        subscriber.album_id_changed(self.__album_id)

    def remove_aid_subscriber(self, subscriber):
        self.__list_of_albim_id_subscribers.remove(subscriber)

    def clear_all_aid_subscribers(self):
        self.__list_of_albim_id_subscribers.clear()

    def add_new_account_data_subscriber(self, subscriber):
        self.__list_of_account_data_subscribers.append(subscriber)
        subscriber.update_account_data((self.__first_name,self.__last_name,self.__avatar,))
                                                    # tuple(avatar_path,first_name,last_name)

    def remove_account_data_subscriber(self, subscriber):
        self.__list_of_account_data_subscribers.remove(subscriber)

    def clear_all_account_data_subscribers(self):
        self.__list_of_account_data_subscribers.clear()






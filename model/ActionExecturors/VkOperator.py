from PyQt5.QtCore import pyqtSignal,QObject

from model.ActionExecturors.ExecuteAble import ExecuteAble
from model.Enums.ActionsEnum import ActionsEnum
from model.Threads.GetGroupsThread import GetGroupsThread
from model.Threads.DataDownloadThread import DataDowndloadThread
from model.Threads.DataUploadThread import DataUploadThread
from model.VkOperations.VkOperations import VkOperations
from model.Converters.ConverterDataFromServerVk import ConverterDataFromServerVk
from model.Interfaces.Subscriber import Subscriber

class VkOperator(ExecuteAble,QObject,Subscriber):

    groups_without_post_received = pyqtSignal(list)
    action_has_done = pyqtSignal()
    action_has_failed = pyqtSignal()
    occured_warning = pyqtSignal(str,object,tuple)
    actions_delayed= pyqtSignal()

    def __init__(self,logger,session_data_publisher,group_container,vk_api,photo_manager, sending_container):
        super(VkOperator, self).__init__()

        self.__logger = logger
        VkOperations.logger = self.__logger
        self.__sending_container = sending_container
        self.__group_container = group_container
        self.__vk_api = vk_api
        self.__photo_manager = photo_manager

        self.create_threads()
        self.snapping_threads_signals()
        self.snapping_internal_signals()
        self.__session_data_publisher  = session_data_publisher
        self.subscribe(self.__session_data_publisher)

    @property
    def uploaded_thread(self):
        return self.__uploaded_thread

    def create_threads(self):
        self.__get_groups_thread = GetGroupsThread(self.__logger,self.__vk_api)
        self.__download_thread = DataDowndloadThread(self.__logger,[])
        self.__uploaded_thread = DataUploadThread(self.__logger,self.__vk_api,self.__photo_manager,[])

    def snapping_internal_signals(self):
        self.groups_without_post_received.connect(self.start_filling_groups_photos)
        self.__uploaded_thread.data_have_uploaded_to_vk.connect(self.send_post_to_group)

    def snapping_threads_signals(self):
        self.__get_groups_thread.group_founded.connect(self.receive_groups_without_photos)
        self.__download_thread.photos_downloaded.connect(self.receive_photos_for_groups)

    def update_group_container(self,groups):
        tmp_groups = groups.copy()
        self.__group_container.clear()
        self.__group_container.add_all(tmp_groups)

    def receive_groups_without_photos(self,groups):
        self.update_group_container(ConverterDataFromServerVk.convert_data_to_groups_without_photo(groups))

        self.groups_without_post_received.emit([path[2] for path in groups])

    def receive_photos_for_groups(self,photos):
        counter = 0
        for group in self.__group_container.list_of_groups:
            group.photo = photos[counter]
            counter += 1

        self.update_group_container(self.__group_container.list_of_groups)

    def start_filling_groups_photos(self,groups):

        self.__download_thread.list_of_photos = groups
        self.__download_thread.start()

    def start_get_groups(self,data):
        self.__get_groups_thread.amount = data[1]
        self.__get_groups_thread.key_word = data[0]
        self.__get_groups_thread.country_id = data[2]
        self.__get_groups_thread.min_amount_users = data[3]
        self.__get_groups_thread.vk_api = self.__vk_api
        self.__get_groups_thread.start()

    def start_preparing_to_send_post(self,data):
        self.__uploaded_thread.data = list(data)
        self.__uploaded_thread.vk_api = self.__vk_api
        self.__uploaded_thread.start()

    def send_post_to_group(self,data):
        try:
            VkOperations.send_post_to_group(self.__vk_api, data[1],data[2],data[0]) # group_id,  text, list_of_vk_images
            self.action_has_done.emit()
        except Exception as ex:
            self.action_has_failed.emit()
            if str(ex).split(".")[0] == '220' :
                self.occured_warning.emit("Too many recipients.You have used all your resources(100 posts - max )\nfor the day. Please continue tomorrow!\n"
                                          "Press Ok to delay actions for next time", self.actions_delayed_accepted, ())
        self.__sending_container.append_sending_to_file(data[1], data[2], data[0])

    def actions_delayed_accepted(self):
        self.actions_delayed.emit()

    def execute(self, cmd, data):
        if cmd == ActionsEnum.SEARCH_GROUPS:
            self.start_get_groups(data)

        elif cmd == ActionsEnum.SEND_POSTS_TO_GROUPS:
            self.start_preparing_to_send_post(data)


    def vk_api_changed(self,new_vk_api):
        self.__vk_api = new_vk_api

    def subscribe(self,publisher):
        publisher.add_new_subscriber(self)

    def unsubscribe(self,publisher):
        publisher.remove_subscriber(self)





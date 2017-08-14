from PyQt5.QtCore import QObject,pyqtSignal,QThread
class DataUploadThread(QThread,QObject):

    data_have_uploaded_to_vk = pyqtSignal(list)

    def __init__(self,logger,vk_api = None , photo_manager = None,data = [].copy()):
        super(DataUploadThread, self).__init__()
        self.__vk_api = vk_api
        self.__photo_manager = photo_manager
        self.__data = data

        self.__logger = logger



    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,new_data):
        if(isinstance(new_data,list)):
            self.__data = new_data

    @property
    def vk_api(self):
        return self.__vk_api

    @vk_api.setter
    def vk_api(self, new_vk_api):
        if new_vk_api:
            self.__vk_api = new_vk_api

    def upload_photos(self,list_of_photos):
        try:
            self.data[2] = [self.__photo_manager.getPathOfPhoto(self.__vk_api, photo) for photo in list_of_photos]
            self.data_have_uploaded_to_vk.emit(self.data)
            self.__logger.change_name(self.__class__.__name__)
            self.__logger.info("Photo has uploaded")
        except Exception as ex :
            self.__logger.change_name(self.__class__.__name__)
            self.__logger.exception(ex)

    def run(self):
        try:
            self.data = list(self.data)
            self.upload_photos(self.data[2])
        except Exception as ex:
            self.__logger.change_name(self.__class__.__name__)
            self.__logger.exception(ex)


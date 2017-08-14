from PyQt5.QtCore import QThread,pyqtSignal,QObject
from model.Converters.ConverterDataFromServerVk import ConverterDataFromServerVk
class DataDowndloadThread(QThread,QObject):

    photos_downloaded = pyqtSignal(list)

    def __init__(self,logger,list_of_photos):
        super(DataDowndloadThread, self).__init__()
        self.__list_of_photos = list_of_photos
        self.__logger = logger

    @property
    def list_of_photos(self):
        return self.__list_of_photos

    @list_of_photos.setter
    def list_of_photos(self,new_list_of_photos):
        self.__list_of_photos =new_list_of_photos

    def run(self):
        try:
            list_of_photos = [ConverterDataFromServerVk.convert_remote_img_to_QImage(path)
                              for path in self.__list_of_photos]
            self.photos_downloaded.emit(list_of_photos)

            self.__logger.change_name(self.__class__.__name__)
            self.__logger.info("Data has downloaded")

        except Exception as ex:
            self.__logger.change_name(self.__class__.__name__)
            self.__logger.exception(ex)

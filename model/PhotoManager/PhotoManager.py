import copy
from PyQt5.QtCore import QBuffer,QIODevice
from model.Containers.PhotoCompliancesContainer import PhotoCompliancesContainer
from model.DataUploadingVkOperations.DataUploadingVkOperations import DataUploadingVkOperations
from model.PhotoDBOperations.PhotoDBOperations import PhotoDBOperations
from model.PhotoConvertionOperations.PhotoConvertionOperations import PhotoConvertionOperations
from model.Interfaces.Subscriber import Subscriber

class PhotoManager(Subscriber):

    def __init__(self,logger,db,session_data,compliances_container = None,album_id = 0):
        self.__logger = logger
        self.__compliances_container = compliances_container
        self.__compliances = None
        self.__db = db
        self.__album_id = album_id
        self.create_auxiliary_objects()
        self.subscribe(session_data)

    def create_auxiliary_objects(self):
        self.__temp_photo_buffer = QBuffer()
        self.__temp_photo_buffer.open(QIODevice.WriteOnly)

    def fill_compliance_container(self,aid):

        self.__compliances = PhotoDBOperations.read_compliences(self.__db)
        self.__compliances_container = self.__compliances.get(aid,None)

        if  self.__compliances_container:
            self.__compliances_container.images = [PhotoConvertionOperations.convert_byte_array_to_image
                            (bytes_of_photo) for bytes_of_photo in self.__compliances_container.images]
        else:
            container = PhotoCompliancesContainer([], [])
            self.__compliances[aid] = container
            self.__compliances_container = container


    def  getPathOfPhoto(self,vk_api,photo):
        self.__logger.change_name(self.__class__.__name__)
        try :
            path = self.__compliances_container.get_path(photo)
            if ( path is not None):
                self.__logger.info("The complience has found")
                return path


            path = DataUploadingVkOperations.upload_photo_to_vk(vk_api,
                   DataUploadingVkOperations.getUploadURL(vk_api),
                   PhotoConvertionOperations.convert_image_to_byte_array(photo,self.__temp_photo_buffer))

            if(path is not None):
                self.__compliances_container.add_compliance(photo,path)
                bytes_complience_container = copy.copy(self.__compliances_container)
                bytes_complience_container.images = [PhotoConvertionOperations.convert_image_to_byte_array
                        (image,self.__temp_photo_buffer)  for image in self.__compliances_container.images]
                self.__compliances[self.__album_id] = bytes_complience_container
                PhotoDBOperations.update_db(self.__db,self.__compliances)
                self.__logger.info("The complience has added")
                return path

        except Exception as ex:
            self.__logger.exception(ex)


    def album_id_changed(self,new_aid):
        self.__album_id = new_aid
        if self.__album_id:
            DataUploadingVkOperations.ALBUM_ID = new_aid
            self.fill_compliance_container(new_aid)

    def subscribe(self,publisher):
        publisher.add_new_aid_subscriber(self)

    def unsubscribe(self,publisher):
        publisher.remove_subscriber(self)

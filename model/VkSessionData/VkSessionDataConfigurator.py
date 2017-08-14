from model.VkAuthorizationModel.ReadWriteToken import ReadWriteToken
import requests,vk
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap,QRegion
from PyQt5.QtCore import QRect

class VkSessionDataConfigurator:
    def __init__(self,logger,session_data_container,path_to_token_file):

        self.__logger = logger

        self.__path_to_token_file = path_to_token_file
        self.__session_data_container = session_data_container
        self.create_aux_elements()
        self.beging_setting(self.__path_to_token_file)



    def  create_aux_elements(self):
        pict_mask = QPixmap(r"../auxElements/profile_mask.png")
        pict_mask = pict_mask.scaled(100, 100)
        self.__profile_mask = pict_mask.createMaskFromColor(Qt.white)


    def update_session_data_container_with_new_token(self,new_token):
        try:
            if(isinstance(new_token,str) and new_token):
                vk_api = self.create_vk_api(new_token)
                self.set_vk_api(vk_api)
                self.set_token(new_token)
                self.set_album_id(vk_api)
                self.set_user_id(new_token)
                self.update_account_data(vk_api)
                self.write_token_to_file(self.__path_to_token_file,new_token)
                self.__logger.change_name(self.__class__.__name__)
                self.__logger.info("Token changed " + new_token)
            else:
                self.__logger.error("Token DID NOT changed !!!" + new_token)

        except Exception as ex:
            self.__logger.change_name(self.__class__.__name__)
            self.__logger.exception(ex)

    def beging_setting(self,file):
        token = self.read_token_from_file(file)
        if token:
            self.update_session_data_container_with_new_token(token)

    def read_token_from_file(self,file):
        return ReadWriteToken.search_avaliable_token(file)

    def write_token_to_file(self,file,token):
        ReadWriteToken.write_token_to_file(file,token)

    def create_vk_api(self, token):
        session = vk.Session(token)
        vk_api = vk.API(session=session)
        return vk_api

    def update_account_data(self,new_vk_api):
        data = new_vk_api.users.get(user_ids=new_vk_api.account.getProfileInfo()["screen_name"], fields='photo_200')[0]
        ava = self.download_photo(data["photo_200"])
        first_name = data["first_name"]
        last_name = data["last_name"]
        self.__session_data_container.avatar = ava
        self.__session_data_container.first_name = first_name
        self.__session_data_container.last_name = last_name
        self.__session_data_container.account_data_updated((first_name,last_name,ava,))



    def download_photo(self,path_image):
        image = QPixmap()
        image.loadFromData(requests.get(path_image).content)
        image = image.scaled(100,100)
        image.setMask(self.__profile_mask)

        return image



    def set_vk_api(self,vk_api):
        self.__session_data_container.vk_api = vk_api

    def set_token(self,token):
        self.__session_data_container.token = token

    def set_user_id(self,token):
        req = self.__session_data_container.vk_api.users.get(access_token=token)
        uid  = req[0]["uid"]
        self.__session_data_container.user_id = uid

    def search_album_of_user_by_title(self,title,vk_api):
        req = vk_api.photos.getAlbums()
        for group in req:
            if group["title"] == title:
                return group["aid"]


    def set_album_id(self,vk_api):
        try:
            album_aid = self.search_album_of_user_by_title("uploadsPhotos",vk_api)
            if album_aid:
                self.__session_data_container.album_id = album_aid
            else :
                vk_api.photos.createAlbum(title = "uploadsPhotos",type = 'nobody')
                album_aid = self.search_album_of_user_by_title("uploadsPhotos",vk_api)
                if album_aid :
                    self.__session_data_container.album_id = album_aid
            self.__logger.change_name(self.__class__.__name__)
            self.__logger.info("uploads Photo Album changed " + str(album_aid))
        except Exception as ex:
            self.__logger.change_name(self.__class__.__name__)
            self.__logger.exception(ex)

    def token_changed(self,new_token):
        self.set_token(new_token)
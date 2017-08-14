class ConfigContainerPostToGroup:

    def __init__(self,app_id = 0,post_container_path = '',photo_complience_path = ''):
        self.__application_id = app_id
        self.__post_container_path = post_container_path
        self.__photo_complience_path = photo_complience_path

    @property
    def application_id(self):
        return self.__application_id

    @property
    def photo_complience_path(self):
        return self.__photo_complience_path

    @property
    def post_container_path(self):
        return self.__post_container_path

    @application_id.setter
    def application_id(self,new_app_id):
        if(isinstance(new_app_id,(str,int))):
            self.__application_id = new_app_id

    @photo_complience_path.setter
    def photo_complience_path(self,new_photo_comp_path):
        if(isinstance(new_photo_comp_path,str)):
            self.__photo_complience_path = new_photo_comp_path

    @post_container_path.setter
    def post_container_path(self,new_post_container_path):
        if(isinstance(new_post_container_path,str)):
            self.__post_container_path = new_post_container_path



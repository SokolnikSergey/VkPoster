

class Group:
    def __init__(self,title="",gid = 0,description ="",photo = "",is_allow_post= 0 ):
        self.__title = title
        self.__gid  = gid
        self.__description = description
        self.__photo = photo
        self.__is_allow_post = is_allow_post

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self,new_title):
        if(isinstance(new_title,str)):
            self.__title = new_title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        if (isinstance(new_description, str)):
            self.__description = new_description

    @property
    def photo(self):
        return self.__photo

    @photo.setter
    def photo(self, new_photo):
        self.__photo = new_photo

    @property
    def is_allow_post(self):
        return self.__is_allow_post

    @is_allow_post.setter
    def is_allow_post(self, new_is_allow_post):
        if (isinstance(new_is_allow_post, int)):
            self.__is_allow_post = new_is_allow_post

    @property
    def gid(self):
        return self.__gid


    @gid.setter
    def gid(self, new_gid):
        if (isinstance(new_gid, int)):
            self.__gid = new_gid




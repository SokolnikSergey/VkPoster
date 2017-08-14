class Post:
    def __init__(self,list_of_photos,text = ""):
        self.__text = text
        self.__list_of_photos  = list_of_photos

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self,new_text):
        if (isinstance(new_text,str)):
            self.__text = new_text

    @property
    def list_of_photos(self):
        return self.__list_of_photos

    @list_of_photos.setter

    def list_of_photos(self,new_list_of_photos):
        if(isinstance(new_list_of_photos,list)):
            self.__list_of_photos = new_list_of_photos

    def clear_list_of_photos(self):
        self.__list_of_photos.clear()

    def add_photo(self,new_photo):
        if isinstance(new_photo,str):
            self.__list_of_photos.append(new_photo)

    def size(self):
        return len(self.__list_of_photos)

    def remove_photo(self,photo_for_remove):
        for photo in self.__list_of_photos:
            if photo is photo_for_remove:
                self.__list_of_photos.remove(photo_for_remove)


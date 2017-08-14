class PhotoCompliancesContainer:
    def __init__(self,images,paths_on_server):
        self.__images = images
        self.__paths_on_server = paths_on_server

    @property
    def images(self):
        return self.__images

    @images.setter
    def images(self,new_images):
        if(isinstance(new_images,list)):
            self.__images = new_images

    @property
    def paths_on_server(self):
        return self.__paths_on_server

    @paths_on_server.setter
    def paths_on_server(self,new_paths_on_server):
        if(isinstance(new_paths_on_server,list)):
            self.__paths_on_server = new_paths_on_server

    def add_compliance(self,image,path_on_server):
        self.__images.append(image)
        self.__paths_on_server.append(path_on_server)

    def remove_compliance(self,image):
        position = self.__images.index(image)
        self.__images.pop(position)
        self.__paths_on_server.pop(position)

    def clear(self):
        self.__images.clear()
        self.__paths_on_server.clear()

    def get_path(self,image):
        if image in self.__images:
            postition = self.__images.index(image)
            return self.__paths_on_server[postition]
        return None
import configparser,os
from model.ConfigParser.ConfigContainerPostToGroup.ConfigContainerPostToGroup import ConfigContainerPostToGroup
class ConfigParser:
    def __init__(self,path_to_ini = "",config_container = None):
        self.__config_parser = None
        self.__config_container = config_container
        self.__path_to_ini = path_to_ini

        self.create_parser()
        self.read_from_config_file()
        self.fill_container_with_options()

    def create_parser(self):
        self.__config_parser  = configparser.ConfigParser()

    def fill_container_with_options(self):
        if isinstance(self.__config_container,ConfigContainerPostToGroup) :
            self.read_app_id_from_ini()
            self.read_path_post_container_from_ini()
            self.read_path_photo_compliences()

    def write_to_config_file(self):
        if self.__config_parser is not  None:
            with open(self.__path_to_ini,"w") as config_file:
                self.__config_parser.write(config_file)

    def read_from_config_file(self):
        if self.__config_parser is not  None :
            if  (os.path.exists(self.__path_to_ini)):
                self.__config_parser.read(self.__path_to_ini)
            else:
                self.set_default_values()
                self.__config_parser.read(self.__path_to_ini)

    def set_default_values(self):
        self.__config_parser.add_section("Settings")
        self.__config_parser.add_section("Paths")

        self.__config_parser.set("Settings","AppID","5842253")
        self.__config_parser.set("Paths", "PathToPostDB", "../DB/Posts")
        self.__config_parser.set("Paths","PathCompliencesPhoto",'../DB/photoCompliances')

        self.write_to_config_file()

    def read_app_id_from_ini(self):
        app_id = None
        if self.__config_parser is not None:
            if "Settings" in self.__config_parser:
                app_id = self.__config_parser["Settings"]["AppID"]
                if(id is not None) and self.__config_container:
                    self.__config_container.application_id = app_id
        return app_id

    def read_path_post_container_from_ini(self):
        posts_path = None
        if self.__config_parser is not None:
            if "Paths" in self.__config_parser:
                posts_path = self.__config_parser["Paths"]["PathToPostDB"]
                if (id is not None) and self.__config_container:
                    self.__config_container.post_container_path = posts_path
        return posts_path

    def read_path_photo_compliences(self):
        compliences_path = None
        if self.__config_parser is not None:
            if "Paths" in self.__config_parser:
                compliences_path = self.__config_parser["Paths"]["PathCompliencesPhoto"]
                if (id is not None) and self.__config_container:
                    self.__config_container.photo_complience_path = compliences_path
        return compliences_path

    def write_app_id_to_ini(self,app_id):
        app_id = str(app_id)
        if(self.__config_parser) and "Settings" in self.__config_parser:
            if(isinstance(app_id,str)):
                self.__config_parser["Settings"]["AppID"] = app_id
                self.write_to_config_file()

    def write_posts_path_to_ini(self, posts_path):
        if (self.__config_parser) and "Paths" in self.__config_parser:
            if (isinstance(posts_path,str)):
                self.__config_parser["Paths"]["PathToPostDB"] = posts_path
                self.write_to_config_file()

    def write_photo_compliences_path_to_ini(self, photo_comp_path):
        if (self.__config_parser) and "Paths" in self.__config_parser:
            if (isinstance(photo_comp_path,str)):
                self.__config_parser["Paths"]["PathCompliencesPhoto"] = photo_comp_path
                self.write_to_config_file()

    def write_element(self,section,element,value):
        self.__config_parser[section][element] = value

    def read_element(self,section,element):
        return self.__config_parser[section][element]

from model.Containers.GroupContainer.Group import Group
from PyQt5.QtGui import QImage
import requests

class ConverterDataFromServerVk:

    @staticmethod
    def convert_data_to_groups_without_photo(list_of_groups):
        return [ConverterDataFromServerVk.create_group(title=group[1],gid= group[0]) for group in list_of_groups ]

    @staticmethod
    def convert_data_to_groups_with_photo(list_of_groups):
        list_of_groups = [ConverterDataFromServerVk.create_group(title=group[1],
            photo=ConverterDataFromServerVk.convert_remote_img_to_QImage(group[2]),
                                        gid=group[0]) for group in list_of_groups]

        return  list_of_groups

    @staticmethod
    def create_group(title="",gid = 0,description ="",photo = "",is_allow_post= 0):
        return Group(title,gid,description,photo,is_allow_post)

    @staticmethod
    def convert_remote_img_to_QImage(path):
        data = requests.get(path)
        image = QImage()
        image.loadFromData(data.content)

        return image
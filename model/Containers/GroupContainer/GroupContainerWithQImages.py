from model.Containers.GroupContainer.Group import Group
from model.Containers.Interfaces.AbstractContainer import AbstractContainer
from PyQt5.QtGui import QImage


class GroupContainerWithQImages(AbstractContainer):
    def __init__(self, list_of_groups):
        self.__list_of_groups = list_of_groups

    @property
    def list_of_groups(self):
        return self.__list_of_groups

    @list_of_groups.setter
    def list_of_groups(self, new_list_of_groups):
        if (isinstance(new_list_of_groups, list) and all(isinstance(group, group)
                                                         for group in self.__list_of_groups)):
            self.__list_of_groups = new_list_of_groups

    def size(self):
        return len(self.__list_of_groups)

    def add(self, group):
        if(isinstance(group,Group)):
            if(isinstance(group.photo,QImage)):
                self.list_of_groups.append(group)
            else:
                self.list_of_groups.append(self.convert_groups(group))

    def add_all(self,list_of_groups):
        if(isinstance(list_of_groups,list)):
            for group in list_of_groups:
                self.add(group)



    def clear(self):
        self.__list_of_groups.clear()

    def remove_all(self,list_to_remove):
        for group in list_to_remove:
            self.remove(group)

    def remove(self, group):
        if (group in self.__list_of_groups):
            self.__list_of_groups.remove(group)

    def remove_group_by_id(self, id_for_remove):
        for group in self.list_of_groups:
            if (group.gid == id_for_remove):
                self.list_of_groups.remove(group)

    def remove_group_by_title(self, title_to_remove):
        for group in self.list_of_groups:
            if (group.title == title_to_remove):
                self.list_of_groups.remove(group)

    def remove_groups_by_is_allow(self, is_allowed_to_remove):
        for group in self.list_of_groups:
            if (group.is_allow_post == is_allowed_to_remove):
                self.list_of_groups.remove(group)


    ###################################################################

    def update_container(self,list_of_groups):
        self.clear()
        if(len(list_of_groups)):
            for group in self.__list_of_groups:
                self.add(group)
    #############################################################

    def convert_groups(self,groups):
        if(isinstance(groups,list) and all(isinstance(group,Group) for group in groups)):

            if all(isinstance(group.photo,QImage) for group in groups):
                return groups

            return [Group(group.title,group.gid,group.description,QImage(group.photo))
                        for group in groups]

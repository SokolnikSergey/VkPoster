from model.Containers.GroupContainer.Group import Group
from model.Containers.Interfaces.ContainerPublisher import ContainerPublisher
from model.Containers.Interfaces.AbstractContainer import AbstractContainer

class GroupContainer(ContainerPublisher,AbstractContainer,):

    def __init__(self,list_of_groups):
        self.__list_of_groups = list_of_groups
        self.__subscribers = []

    @property
    def list_of_groups(self):
        return self.__list_of_groups

    @list_of_groups.setter
    def list_of_groups(self,new_list_of_groups):
        if(isinstance(new_list_of_groups,list) and all(isinstance(group,Group) for group in self.list_of_groups)):
            self.__list_of_groups = new_list_of_groups

    def size(self):
        return len(self.__list_of_groups)

    def clear(self):
        self.list_of_groups.clear()
        self.cleared()

    def add(self,group):
        if (isinstance(group,Group)):
            self.__list_of_groups.append(group)
            self.added([group])

    def add_all(self,groups):
        if isinstance(groups,list):
            if all(isinstance(group,Group) for group in groups):
                self.__list_of_groups.extend(groups)
                self.added(groups)

            else:
                for group in groups :
                    self.add(group)

    def remove(self,group):
        if (isinstance(group,Group)):
            if group in self.__list_of_groups:
                self.__list_of_groups.remove(group)
                self.removed([group])

    def remove_group_by_id(self,id_for_remove):
        removed_group = []
        for group in self.list_of_groups:
            if(group.gid == id_for_remove):
                self.list_of_groups.remove(group)
                removed_group.append(group)
        if len(removed_group):
            self.removed(removed_group)

    def remove_group_by_title(self,title_to_remove):
        removed_group = []
        for group in self.list_of_groups:
            if ( group.title == title_to_remove ) :
                self.list_of_groups.remove(group)
                removed_group.append(group)

        if len(removed_group):
            self.removed(removed_group)

    def remove_groups_by_is_allow(self,is_allowed_to_remove):

        removed_group = []
        for group in self.list_of_groups:
            if (group.is_allow_post == is_allowed_to_remove):
                self.list_of_groups.remove(group)
                removed_group.append(group)
        if len(removed_group):
            self.removed(removed_group)
###################################################################

    def added(self,groups):

        for subscriber in self.__subscribers:
            subscriber.publisher_added(groups)

    def removed(self, groups):
        for subscriber in self.__subscribers:
            subscriber.publisher_removed(groups)

    def cleared(self):
        for subscriber in self.__subscribers:
            subscriber.publisher_cleared()

    def remove_subscriber(self, object_to_unsubscribe):
        self.__subscribers.remove(object_to_unsubscribe)

    def add_subscriber(self, object_to_subscribe):

        self.__subscribers.append(object_to_subscribe)

        object_to_subscribe.update(self.__list_of_groups)
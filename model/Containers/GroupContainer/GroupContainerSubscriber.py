from model.Containers.Interfaces.ContainerSubscriber import ContainerSubscriber

from PyQt5.QtCore import pyqtSignal,QObject

class GroupContainerSubscriber(QObject,ContainerSubscriber):

    groups_added = pyqtSignal(list)
    groups_removed = pyqtSignal(list)
    container_cleared = pyqtSignal()
    group_container_updated = pyqtSignal(list)

    def __init__(self,group_container):
        super(GroupContainerSubscriber, self).__init__()
        self.__group_container  = group_container
        self.__publisher = None


    def publisher_added(self, groups):
        groups = self.__group_container.convert_groups(groups)
        self.__group_container.add_all(groups)
        self.groups_added.emit(groups)

    def publisher_removed(self, groups):
        groups = self.__group_container.convert_groups(groups)
        self.__group_container.remove_all(groups)
        self.groups_removed.emit(groups)

    def publisher_cleared(self):
        self.__group_container.clear()
        self.container_cleared.emit()

    def update(self, groups):
        groups = self.__group_container.convert_groups(groups)
        self.__group_container.clear()
        self.__group_container.add_all(groups)
        self.group_container_updated.emit(groups)

    def subscribe(self,publisher):
        publisher.add_subscriber(self)
        self.__publisher = publisher

    def unsubscribe(self,publisher):
        publisher.remove_subscriber(self)
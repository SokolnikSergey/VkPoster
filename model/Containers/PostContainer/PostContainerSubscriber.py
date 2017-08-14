from model.Containers.Interfaces.ContainerSubscriber import ContainerSubscriber

from PyQt5.QtCore import pyqtSignal,QObject

class PostContainerSubscriber(QObject,ContainerSubscriber):

    posts_added = pyqtSignal(list)
    posts_removed = pyqtSignal(list)
    container_cleared = pyqtSignal()
    post_container_updated = pyqtSignal(list)

    def __init__(self,post_container):
        super(PostContainerSubscriber, self).__init__()
        self.__post_container  = post_container
        self.__publisher = None


    def publisher_added(self, posts):
        posts = self.__post_container.convert_posts(posts)
        self.__post_container.add_all(posts)
        self.posts_added.emit(posts)

    def publisher_removed(self, posts):
        posts = self.__post_container.convert_posts(posts)
        self.__post_container.remove(posts)
        self.posts_removed.emit(posts)

    def publisher_cleared(self):
        self.__post_container.clear()
        self.container_cleared.emit()

    def update(self, posts):
        posts = self.__post_container.convert_posts(posts)
        self.__post_container.clear()
        self.__post_container.add_all(posts)
        self.post_container_updated.emit(self.__post_container.list_of_posts)


    def subscribe(self,publisher):
        publisher.add_subscriber(self)
        self.__publisher = publisher

    def unsubscribe(self,publisher):
        publisher.remove_subscriber(self)
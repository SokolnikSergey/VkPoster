from model.Containers.PostContainer.Post import Post
from model.Containers.Interfaces.AbstractContainer import AbstractContainer
from model.Containers.Interfaces.ContainerPublisher import ContainerPublisher

class PostContainer(AbstractContainer,ContainerPublisher):
    def __init__(self,list_of_posts):
        self.__list_of_posts = list_of_posts
        self.__subscribers = []

    @property
    def list_of_posts(self):
        return self.__list_of_posts

    @list_of_posts.setter
    def list_of_posts(self,new_list_of_posts):
        if(isinstance(new_list_of_posts,list) and all(isinstance(post,Post) for post in self.list_of_posts)):
            self.__list_of_posts = new_list_of_posts

    def size(self):
        return len(self.__list_of_posts)

    def add(self,post):
        if(isinstance(post,Post)):
            self.__list_of_posts.append(post)
        self.added([post])

    def add_all(self,posts):
        if isinstance(posts, list):
            if all(isinstance(group, Post) for group in posts):
                self.__list_of_posts.extend(posts)
                self.added(posts)
            else:
                for group in posts:
                    self.add(group)

    def remove(self,post):
        if(post in self.__list_of_posts):
            self.__list_of_posts.remove(post)
        self.removed(post)

    def remove_post_by_text(self,text_for_delete):
        post_to_remove = []
        for post in self.list_of_posts:
            if(post.text == text_for_delete):
                self.list_of_posts.remove(post)
                post_to_remove.append(post)
        if(len(post_to_remove)):
            self.removed(post_to_remove)

    def clear(self):
        self.list_of_posts.clear()
        self.cleared()
#############################################################3

    def added(self,post):
        for subscriber in self.__subscribers:
            subscriber.publisher_added(post)

    def removed(self, post):
        for subscriber in self.__subscribers:
            subscriber.publisher_removed(post)

    def cleared(self):
        for subscriber in self.__subscribers:
            subscriber.publisher_cleared()

    def remove_subscriber(self, object_to_unsubscribe):
        self.__subscribers.remove(object_to_unsubscribe)

    def add_subscriber(self, object_to_subscribe):
        self.__subscribers.append(object_to_subscribe)
        object_to_subscribe.update(self.__list_of_posts)

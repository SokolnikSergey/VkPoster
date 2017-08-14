from model.Containers.PostContainer.PostContainer import Post
from model.Containers.Interfaces.AbstractContainer import AbstractContainer
from PyQt5.QtGui import QImage


class PostContainerWithQImages(AbstractContainer):
    def __init__(self, list_of_posts):
        self.__list_of_posts = list_of_posts

    @property
    def list_of_posts(self):
        return self.__list_of_posts

    @list_of_posts.setter
    def list_of_posts(self, new_list_of_posts):
        if (isinstance(new_list_of_posts, list) and all(isinstance(post, Post) for post in self.list_of_posts)):
            self.__list_of_posts = new_list_of_posts

    def size(self):
        return len(self.__list_of_posts)

    def add(self, post):
        if (isinstance(post, Post)):
            if not len(post.list_of_photos) or \
                    all(isinstance(image,QImage) for image in post.list_of_photos ):
                self.__list_of_posts.append(post)
            else:
                self.__list_of_posts.append(self.convert_posts(post))

    def add_all(self,list_of_posts):
        if (isinstance(list_of_posts, list)):
            for post in list_of_posts:
                self.add(post)

    def remove(self, posts):
        for post_to_delete in posts:
            for post in self.__list_of_posts:
                if post.text == post_to_delete.text :
                    self.__list_of_posts.remove(post)

    def update_container(self,list_of_posts):
        self.clear()
        if(len(list_of_posts)):
            for post in self.__list_of_posts:
                self.add(post)

    def clear(self):
        self.__list_of_posts.clear()

    #############################################################

    def convert_posts(self,posts):

        if (isinstance(posts, list) and all(isinstance(post, Post) for post in posts)):
            if all(isinstance(post.list_of_photos, QImage) for post in posts):
                return posts
            temp_posts = []
            for post in posts:
                list_of_images = []
                for path in post.list_of_photos:
                    image = QImage(path)
                    image.setText(path,"")
                    list_of_images.append(image)
                temp_posts.append(Post(list_of_images,post.text))
            return temp_posts


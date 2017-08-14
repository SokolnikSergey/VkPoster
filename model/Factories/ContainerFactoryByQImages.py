from model.Factories.AbstractContainerFactory import AbstractContainerFactory
from model.Containers.PostContainer.PostContainerWithQImages import PostContainerWithQImages
from model.Containers.GroupContainer.GroupContainerWithQImages import GroupContainerWithQImages


class ContainerFactoryByQImages(AbstractContainerFactory):
    def create_group_container(self):
        return PostContainerWithQImages([])
    
    def create_post_container(self):
        return GroupContainerWithQImages([])


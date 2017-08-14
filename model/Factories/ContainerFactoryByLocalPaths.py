from model.Factories.AbstractContainerFactory import AbstractContainerFactory
from model.Containers.PostContainer.PostContainer import PostContainer
from model.Containers.GroupContainer.GroupContainer import GroupContainer

class ContainerFactoryByLocalPaths(AbstractContainerFactory):
    def create_group_container(self):
        return GroupContainer([])

    def create_post_container(self):
        return PostContainer([])


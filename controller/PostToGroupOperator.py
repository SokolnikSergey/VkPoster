import sys

from PyQt5.QtWidgets import QApplication
from model.Containers.PostContainer.Post import Post
from model.Containers.PostContainer.PostContainer import PostContainer
from model.PostToGroup.PostToGroupModel import PostToGroupModel
from model.Containers.GroupContainer.Group import Group
from model.Containers.GroupContainer.GroupContainer import GroupContainer
from model.Containers.GroupContainer.GroupContainerWithQImages import GroupContainerWithQImages
from model.Containers.PostContainer.PostContainerWithQImages import PostContainerWithQImages

x = QApplication([])

container = PostContainer([Post(["D:\PythonVK\cabeza4.png","D:\PythonVK\PenPicture.png"],"Some text for post"),Post(["D:\PythonVK\cabeza4.png","D:\PythonVK\PenPicture.png"],"Some text for pos2t")])

group_container = GroupContainer([Group("энотхер тай",1,"","D:\PythonVK\PenPicture.png"),Group("фывфывфы",2,"","D:\PythonVK\PenPicture.png")])
myApp = PostToGroupModel(PostContainerWithQImages([]),GroupContainerWithQImages([]),container,group_container)

group_container.add(Group("энотхер тайтл",3,"","D:\PythonVK\PenPicture.png"))
group_container.add_all([Group("энотхер тайтdddл",5,"","D:\PythonVK\PenPicture.png"),Group("+1 ",32222333333,"","D:\PythonVK\PenPicture.png")])

container.add(Post(["D:\PythonVK\cabeza4.png","D:\PythonVK\PenPicture.png"],"Another text for post"))
container.add_all([Post(["D:\PythonVK\cabeza4.png","D:\PythonVK\PenPicture.png"],"Another text for post3"),Post(["D:\PythonVK\cabeza4.png","D:\PythonVK\PenPicture.png"],"Another text for post4")])

group_container.remove_group_by_id(5)
container.remove_post_by_text("Another text for post3")

myApp.show()





sys.exit(x.exec_())
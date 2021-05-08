from view.ChoosePost.ChosePostViewOperator import ChosePostViewOperator
from view.ChoosePost.ChosePostWindow import ChosePostWindow
from PyQt5.QtCore import pyqtSignal, QObject
from model.ChosePostForEdit.BinderChosePostForEdit import BinderChosePostForEdit
from model.Containers.PostContainer.PostContainerSubscriber import PostContainerSubscriber

class ChosePostForEditModel(QObject):

    update_post_container = pyqtSignal(list)
    add_posts_to_post_container = pyqtSignal(list)
    remove_post_from_container = pyqtSignal(list)
    clear_post_container = pyqtSignal()

    chose_post_to_edit = pyqtSignal(str,list)

    choose_post_closed = pyqtSignal()
    delete_post = pyqtSignal(str)
    add_new_post = pyqtSignal(str,list)

    btn_back_pressed = pyqtSignal()

    occured_warning = pyqtSignal(str, object, tuple)  ##signal to fill warning pop-up message
                                                    # (str = text,object = fix method
                                                    # tuple = params for fix method)

    def __init__(self, post_container, post_container_publisher=None):
        super(ChosePostForEditModel, self).__init__()
        self.__choose_post_for_edit_win_operator = None
        self.create_view()

        self.__post_container = post_container

        self.__post_container_subscriber = PostContainerSubscriber \
            (self.__post_container)

        self.__binder = BinderChosePostForEdit(self, self.__choose_post_for_edit_win_operator)

        self.snapping_signals()

        self.__post_container_subscriber.subscribe(post_container_publisher)

    @property
    def post_container(self):
        return self.__post_container

    def create_view(self):
        self.__choose_post_for_edit_win_operator = ChosePostViewOperator(ChosePostWindow())

    def add_new_post_prefered(self):
        self.add_new_post.emit("",[])

    def detect_post_to_edit(self,text):
        for post in self.__post_container.list_of_posts :
            if(post.text == text):
                self.chose_post_to_edit.emit(post.text,post.list_of_photos)


    def show(self):
        self.__choose_post_for_edit_win_operator.show()

    def hide(self):
        self.__choose_post_for_edit_win_operator.hide()

    def snapping_signals(self):
        self.__choose_post_for_edit_win_operator.occured_warning_view.connect(self.occured_warning)

        self.__post_container_subscriber.posts_added.connect(self.add_posts_to_post_container)
        self.__post_container_subscriber.posts_removed.connect(self.remove_post_from_container)
        self.__post_container_subscriber.container_cleared.connect(self.clear_post_container)
        self.__post_container_subscriber.post_container_updated.connect(self.update_post_container)
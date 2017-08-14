from view.PostToGroup.PostToGroupWindow import PostToGroupWindow
from PyQt5.QtCore import pyqtSignal, QObject
from model.PostToGroup.Binder import Binder
from controller.PostToGroupController.PostToGroupController import PostToGroupController
from model.Containers.PostContainer.PostContainerSubscriber import PostContainerSubscriber
from model.Containers.GroupContainer.GroupContainerSubscriber import GroupContainerSubscriber
from view.PostToGroup.PostToGroupWindowOperator import PostToGroupWindowOperator


class PostToGroupModel(QObject):
    update_post_container = pyqtSignal(list)
    add_posts_to_post_container = pyqtSignal(list)
    remove_post_from_container = pyqtSignal(list)
    clear_post_container = pyqtSignal()

    update_group_container = pyqtSignal(list)
    add_groups_to_group_container = pyqtSignal(list)
    remove_groups_from_container = pyqtSignal(list)
    clear_group_container = pyqtSignal()

    read_all_record_from_db = pyqtSignal()
    edit_posts_signal_clicked = pyqtSignal()
    send_posts_to_groups_signal = pyqtSignal(list, list)  # (posts,groups)
    search_groups_by_key_word_signal = pyqtSignal(str)  # (key_word)

    amout_of_actions_changed = pyqtSignal(int,int,int) # actions_has_done, actions_remainded,actions_failed

    btn_change_account = pyqtSignal()
    btn_back_clicked = pyqtSignal()
    btn_helper_clecked = pyqtSignal()

    recover_actions_clicked = pyqtSignal()

    occured_warning = pyqtSignal(str, object, tuple)  ##signal to fill warning pop-up message
                                                    # (str = text,object = fix method
                                                    # tuple = params for fix method)

    def __init__(self, post_container, group_container, post_container_publisher=None,
                 group_container_publisher=None):
        super(PostToGroupModel, self).__init__()
        self.__post_to_group_win_operator = None
        self.create_view()
        self.__post_container = post_container
        self.__group_container = group_container

        self.__group_container_subscriber = GroupContainerSubscriber \
            (self.__group_container)

        self.__post_container_subscriber = PostContainerSubscriber \
            (self.__post_container)

        self.__binder = Binder(self, self.__post_to_group_win_operator)

        self.snapping_signals()

        self.__group_container_subscriber.subscribe(group_container_publisher)
        self.__post_container_subscriber.subscribe(post_container_publisher)

    @property
    def post_container(self):
        return self.__post_container

    @property
    def group_container(self):
        return self.__group_container

    def search_groups_by_key_word(self, key_word):
        if (PostToGroupController.is_allowed_search_post(key_word)):
            self.search_groups_by_key_word_signal.emit(key_word)
        else:
            self.occured_warning.emit("There is no keyword for searching groups,Please"
                                      "Enter KeyWord",None,())


    def recover_groups_by_ids(self, ids):
        return [group for group in self.__group_container.list_of_groups if str(group.gid) in ids]

    def recover_posts_by_texts(self, texts):
        return [post for post in self.__post_container.list_of_posts if post.text in texts]

    def send_posts_to_groups(self, posts_texts_for_send, groups_ids_for_send):
        groups = self.recover_groups_by_ids(groups_ids_for_send)
        posts =  self.recover_posts_by_texts(posts_texts_for_send)
        if PostToGroupController.is_allowed_send_posts_to_group(posts,groups):
            self.send_posts_to_groups_signal.emit(groups,posts)
        else:
            self.occured_warning.emit("You should choose at least one group "
                                      "and one post for sending", None, ())

    def amount_actions_changed(self,amount_has_done,amount_remained,amount_failed):
        self.amout_of_actions_changed.emit(amount_has_done,amount_remained,amount_failed)

    def create_view(self):
        self.__post_to_group_win_operator = PostToGroupWindowOperator(PostToGroupWindow())

    def show(self):
        self.__post_to_group_win_operator.show()

    def hide(self):
        self.__post_to_group_win_operator.hide()

    def snapping_signals(self):
        self.__post_container_subscriber.posts_added.connect(self.add_posts_to_post_container)
        self.__post_container_subscriber.posts_removed.connect(self.remove_post_from_container)
        self.__post_container_subscriber.container_cleared.connect(self.clear_post_container)
        self.__post_container_subscriber.post_container_updated.connect(self.update_post_container)

        self.__group_container_subscriber.groups_added.connect(self.add_groups_to_group_container)
        self.__group_container_subscriber.groups_removed.connect(self.remove_groups_from_container)
        self.__group_container_subscriber.container_cleared.connect(self.clear_group_container)
        self.__group_container_subscriber.group_container_updated.connect(self.update_group_container)

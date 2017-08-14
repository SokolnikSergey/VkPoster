class BinderChosePostForEdit:
    def __init__(self,model,view_operator):

        self.__model = model
        self.__view_operator  = view_operator
        self.snapping_signals()

    def snapping_signals(self):
        self.__model.update_post_container.connect(self.__view_operator.fill_posts_list_widget)
        self.__model.add_posts_to_post_container.connect(self.__view_operator.add_items_to_post_list_widget)
        self.__model.remove_post_from_container.connect(self.__view_operator.remove_items_from_post_list_widget)
        self.__model.clear_post_container.connect(self.__view_operator.clear_posts_list_widget)

        self.__view_operator.chose_post_signal.connect(self.__model.detect_post_to_edit)
        self.__view_operator.choose_post_closed.connect(self.__model.choose_post_closed)
        self.__view_operator.delete_post_signal.connect(self.__model.delete_post)
        self.__view_operator.add_new_post_signal.connect(self.__model.add_new_post_prefered)

        self.__view_operator.btn_back_clicked.connect(self.__model.btn_back_pressed)

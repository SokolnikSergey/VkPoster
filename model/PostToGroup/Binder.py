class Binder:
    def __init__(self,model,view_operator):
        self.__model = model
        self.__view_operator  = view_operator
        self.snapping_signals()

    def snapping_signals(self):
        self.__model.update_post_container.connect(self.__view_operator.fill_posts_list_widget)
        self.__model.add_posts_to_post_container.connect(self.__view_operator.add_items_to_post_list_widget)
        self.__model.remove_post_from_container.connect(self.__view_operator.remove_items_from_post_list_widget)
        self.__model.clear_post_container.connect(self.__view_operator.clear_posts_list_widget)

        self.__model.add_groups_to_group_container.connect(self.__view_operator.add_items_to_group_list_widget)
        self.__model.remove_groups_from_container.connect(self.__view_operator.remove_items_from_group_list_widget)
        self.__model.clear_group_container.connect(self.__view_operator.clear_groups_list_widget)
        self.__model.update_group_container.connect(self.__view_operator. fill_groups_list_widget)
        self.__model.amout_of_actions_changed.connect(self.__view_operator.update_amount_of_actions)

        self.__view_operator.search_groups_signal.connect(self.__model.search_groups_by_key_word)
        self.__view_operator.send_posts_signal.connect(self.__model.send_posts_to_groups)
        self.__view_operator.btn_edit_post_clicked.connect(self.__model.edit_posts_signal_clicked)
        self.__view_operator.btn_read_all_records_clicked.connect(self.__model.read_all_record_from_db)
        self.__view_operator.btn_change_account_pressed.connect(self.__model.btn_change_account)
        self.__view_operator.btn_back_clicked.connect(self.__model.btn_back_clicked)
        self.__view_operator.btn_helper_clicked.connect(self.__model.btn_helper_clecked)
        self.__view_operator.btn_recover_actions_clicked.connect(self.__model.recover_actions_clicked)
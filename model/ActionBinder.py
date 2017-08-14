class ActionBinder:
    def __init__(self,post_to_group,choose_post_for_edit,edit_post,action_maker):
        self.__post_to_group = post_to_group
        self.__choose_post_for_edit = choose_post_for_edit
        self.__edit_post = edit_post

        self.__action_maker  = action_maker

        self.snapping_post_to_group_signals()
        self.snapping_choose_post_for_edit()
        self.snapping_edit_post_signals()

    def snapping_post_to_group_signals(self):
        self.__post_to_group.send_posts_to_groups_signal.connect(self.__action_maker.create_send_posts_to_groups_actions)
        self.__post_to_group.search_groups_by_key_word_signal.connect(self.__action_maker.create_search_groups_action)
        self.__post_to_group.read_all_record_from_db.connect(self.__action_maker.create_read_all_records_from_db_action)


    def snapping_choose_post_for_edit(self):
        self.__choose_post_for_edit.chose_post_to_edit.connect(self.__edit_post.update_view)
        self.__choose_post_for_edit.delete_post.connect(self.__action_maker.create_delete_post_action)
        self.__choose_post_for_edit.add_new_post.connect(self.__edit_post.update_view)

    def snapping_edit_post_signals(self):
        self.__edit_post.post_changed.connect(self.__action_maker.create_edit_post_to_group_action)
        self.__edit_post.post_added.connect(self.__action_maker.create_add_post_action)
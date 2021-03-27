class ExceptionSignalsBinder:
    def __init__(self,exception_handler,choose_posts,post_to_group,edit_post,liable_about_view,warning_message,vk_operator):
        self.__warning_message = warning_message
        self.__exception_handler = exception_handler
        self.__liable_about_view = liable_about_view
        self.__post_to_group = post_to_group
        self.__edit_post = edit_post
        self.__choose_post = choose_posts
        self.__vk_operator = vk_operator

        self.snapping_signals()
        self.snapping_post_to_group_signals()
        self.snapping_choose_post_signals()
        self.snapping_edit_post_signals()
        self.snapping_vk_opearator_signals()


    def snapping_signals(self):
        self.__exception_handler.show_warning_dialog.connect(
            self.__liable_about_view.show_warning_message)

        self.__exception_handler.hide_warning_dialog.connect(
            self.__liable_about_view.hide_warning_message)

        self.__warning_message.accepted.connect(self.__exception_handler.fix)
        self.__warning_message.accepted.connect(self.__liable_about_view.hide_warning_message)



    def snapping_post_to_group_signals(self):
        self.__post_to_group.occured_warning.connect(self.__exception_handler.handle_warning)

    def snapping_choose_post_signals(self):
        self.__choose_post.occured_warning.connect(self.__exception_handler.handle_warning)

    def snapping_edit_post_signals(self):
        self.__edit_post.occured_warning.connect(self.__exception_handler.handle_warning)

    def snapping_vk_opearator_signals(self):
        self.__vk_operator.occured_warning.connect(self.__exception_handler.handle_warning)
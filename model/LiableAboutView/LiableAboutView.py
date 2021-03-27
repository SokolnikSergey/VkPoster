class LiableAboutView:

    def __init__(self,settings,main_starter,post_to_group,choose_post_for_edit,edit_post,warning_message):
        self.__settings = settings
        self.__main_starter = main_starter
        self.__post_to_group = post_to_group
        self.__choose_post_for_edit = choose_post_for_edit
        self.__edit_post = edit_post

        self.__warning_message = warning_message

        self.snapping_settings_signals()
        self.snapping_main_starter_signals()
        self.snapping_post_to_group_signals()
        self.snapping_choose_post_for_edit_signals()
        self.snapping_edit_post_signals()



    def show_settings(self):
        self.__settings.show()

    def hide_settings(self):
        self.__settings.hide()

    def show_main_starter(self):
        self.__main_starter.show()

    def hide_main_starter(self):
        self.__main_starter.hide()


    def show_post_to_group(self):
        self.__post_to_group.show()

    def hide_post_to_group(self):
        self.__post_to_group.hide()

    def show_choose_post_for_edit(self):
        self.__choose_post_for_edit.show()

    def hide_choose_post_for_edit(self):
        self.__choose_post_for_edit.hide()

    def show_edit_post(self):
        self.__edit_post.show()

    def hide_edit_post(self):
        self.__edit_post.hide()

    def show_warning_message(self,text):
        self.__warning_message.setWindowTitle('Error(TTH)')
        self.__warning_message.setText(text)
        self.__warning_message.show()

    def hide_warning_message(self):
        self.__warning_message.hide()


    def snapping_settings_signals(self):
        self.__settings.setting_window_closed.connect(self.hide_settings)
        self.__settings.setting_window_closed.connect(self.show_main_starter)

    def snapping_main_starter_signals(self):
        self.__main_starter.post_to_group_pressed.connect(self.show_post_to_group)
        self.__main_starter.post_to_group_pressed.connect(self.hide_main_starter)

        self.__main_starter.setting_pressed.connect(self.show_settings)
        self.__main_starter.setting_pressed.connect(self.hide_main_starter)

    def snapping_post_to_group_signals(self):
        self.__post_to_group.edit_posts_signal_clicked.connect(self.hide_post_to_group)
        self.__post_to_group.edit_posts_signal_clicked.connect(self.show_choose_post_for_edit)

        self.__post_to_group.btn_back_clicked.connect(self.show_main_starter)
        self.__post_to_group.btn_back_clicked.connect(self.hide_post_to_group)


    def snapping_choose_post_for_edit_signals(self):
        self.__choose_post_for_edit.chose_post_to_edit.connect(self.hide_choose_post_for_edit)
        self.__choose_post_for_edit.chose_post_to_edit.connect(self.show_edit_post)

        self.__choose_post_for_edit.add_new_post.connect(self.hide_choose_post_for_edit)
        self.__choose_post_for_edit.add_new_post.connect(self.show_edit_post)

        self.__choose_post_for_edit.choose_post_closed.connect(self.hide_choose_post_for_edit)
        self.__choose_post_for_edit.choose_post_closed.connect(self.show_post_to_group)

        self.__choose_post_for_edit.btn_back_pressed.connect(self.hide_choose_post_for_edit)
        self.__choose_post_for_edit.btn_back_pressed.connect(self.show_post_to_group)

    def snapping_edit_post_signals(self):
        self.__edit_post.post_changed.connect(self.hide_edit_post)
        self.__edit_post.post_changed.connect(self.show_choose_post_for_edit)

        self.__edit_post.post_added.connect(self.hide_edit_post)
        self.__edit_post.post_added.connect(self.show_choose_post_for_edit)

        self.__edit_post.edit_post_closed.connect(self.hide_edit_post)
        self.__edit_post.edit_post_closed.connect(self.show_choose_post_for_edit)



class StartChoiceBinder():
    def __init__(self,view,model):
        self.___view  = view
        self.__model = model
        self.snapping_signals()

    def snapping_signals(self):
        self.___view.change_account.connect(self.__model.change_account)
        self.___view.btn_post_to_group_pressed.connect(self.__model.post_to_group_pressed)
        self.___view.btn_settings_pressed.connect(self.__model.setting_pressed)

        self.__model.progress_posts_changed.connect(self.___view.update_posts_progress)
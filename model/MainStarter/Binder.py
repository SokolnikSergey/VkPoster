class StartChoiceBinder():
    def __init__(self,view,model):
        self.___view  = view
        self.__model = model
        self.snapping_signals()

    def snapping_signals(self):
        self.___view.change_account.connect(self.__model.get_token)
        self.___view.btn_post_to_group_pressed.connect(self.__model.post_to_group_pressed)
        self.___view.btn_settings_pressed.connect(self.__model.setting_pressed)
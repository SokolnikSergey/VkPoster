class Binder:
    def __init__(self,model,view):
        self.__model = model
        self.__view = view
        self.snapping_signals()


    def snapping_signals(self):
        self.__view.close_settings_window.connect(self.__model.setting_window_closed)
        self.__view.save_settings_signal.connect(self.__model.save_settings)
        self.__view.save_settings_signal.connect(self.__model.setting_window_closed)

        self.__view.country_id_changed.connect(self.__model.country_id_changed)
        self.__view.max_amount_groups_changed.connect(self.__model.max_amount_of_groups_changed)
        self.__view.min_amount_users_changed.connect(self.__model.min_amount_of_users_changed)
        self.__view.timeout_changed.connect(self.__model.timeout_changed)
        self.__view.each_to_each_changed.connect(self.__model.each_to_each_changed)
        self.__view.limit_reached_just_once_changed.connect(self.__model.limit_reached_just_once_changed)
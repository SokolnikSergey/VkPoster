class VkAuthorizationBinder:
    def __init__(self,model,view):
        self.__model = model
        self.__view  = view
        self.snapping_model_signals_with_view_signals()

    def snapping_model_signals_with_view_signals(self):
        self.__view.token_recieved.connect(self.__model.token_recieved_signal)
        self.__view.vk_auth_window_closed.connect(self.__model.auth_window_closed)

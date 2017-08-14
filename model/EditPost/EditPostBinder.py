class EditPostBinder:
    def __init__(self,model,view_operator):
        self.__model = model
        self.__view_operator = view_operator
        self.snapping_signals()

    def snapping_signals(self):
        self.__view_operator.save_changes_signal.connect(self.__model.save_changed_post)
        self.__view_operator.edit_post_closed.connect(self.__model.edit_post_closed)

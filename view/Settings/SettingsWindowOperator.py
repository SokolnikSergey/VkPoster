from PyQt5.QtCore import QObject,pyqtSignal

class SettingsWindowOperator(QObject):

    save_settings_signal = pyqtSignal()

    close_settings_window = pyqtSignal()

    country_id_changed = pyqtSignal(int)
    timeout_changed = pyqtSignal(int)
    max_amount_groups_changed = pyqtSignal(int)
    min_amount_users_changed= pyqtSignal(int)
    each_to_each_changed= pyqtSignal(int)

    def __init__(self,window):
        super(SettingsWindowOperator,self).__init__()
        self.__window = window
        self.snapping_internal_signals()


    def set_begins_values(self,values):

        self.__window.country_id_combobx.setCurrentIndex((values[0]))
        self.__window.max_amount_groups_scroll.setValue(values[1])
        self.__window.min_amount_users_scroll.setValue(values[2])
        self.__window.timeout_scroll.setValue(values[3])
        self.__window.each_to_each_check_box.setCheckState(values[4])

    def snapping_internal_signals(self):
        self.__window.timeout_scroll.valueChanged.connect(self.change_timeout_scroll_postition)
        self.__window.max_amount_groups_scroll.valueChanged.connect(self.change_max_amount_scroll_position)
        self.__window.min_amount_users_scroll.valueChanged.connect(self.change_min_amount_users_scroll_position)
        self.__window.each_to_each_check_box.stateChanged.connect(self.each_to_each_changed)
        self.__window.country_id_combobx.currentIndexChanged.connect(self.country_id_changed)

        self.__window.window_closed.connect(self.close_settings_window)

        self.__window.save_btn.clicked.connect(self.save_settings_signal)


    def change_max_amount_scroll_position(self,new_position):
        self.__window.lcd_max_amount.display(new_position)
        self.max_amount_groups_changed.emit(new_position)

    def change_timeout_scroll_postition(self,new_position):
        self.__window.lcd_timeout.display(new_position)
        self.timeout_changed.emit(new_position)

    def change_min_amount_users_scroll_position(self,new_postition):
        self.__window.lcd_min_amount_users.display(new_postition)
        self.min_amount_users_changed.emit(new_postition)

    def show(self):
        self.__window.show()

    def hide(self):
        self.__window.hide()
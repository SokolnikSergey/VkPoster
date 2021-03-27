from view.Settings.SettingsWindowOperator import SettingsWindowOperator
from view.Settings.SettingsWindow import SettingsWindow
from PyQt5.QtCore import QObject,pyqtSignal
from model.Settings.Binder import Binder

class SettingsModel(QObject):

    setting_window_closed = pyqtSignal()
    update_settings = pyqtSignal(list)


    def __init__(self,country_id = 3,max_amount_of_groups = 50,min_amount_of_users = 100, timeout_between_operations = 10,each_to_each = 0):
        super(SettingsModel, self).__init__()

        self.__country_id = country_id
        self.__max_amount_of_groups = max_amount_of_groups
        self.__min_amount_of_users = min_amount_of_users
        self.__timeout_between_operations = timeout_between_operations
        self.__each_to_each = each_to_each

        self.__on_start_settings_values = self.collect_values()
        self.create_view()

        self.set_begins_view_values()
        self.__binder = Binder(self,self.__view_operator)

    def create_view(self):
        self.__view_operator = SettingsWindowOperator(SettingsWindow())

    def set_begins_view_values(self, values = None):
        if values is None:
            self.__view_operator.set_begins_values(self.collect_values())
        else:
            self.__view_operator.set_begins_values(values)

    @property
    def country_id(self):
        return self.__country_id

    def country_id_changed(self,new_country_id):
        self.__country_id = new_country_id

    @property
    def timeout(self):
        return self.__timeout_between_operations


    def timeout_changed(self,new_timeout):
        self.__timeout_between_operations = new_timeout

    @property
    def max_amount_of_groups(self):
        return self.__max_amount_of_groups

    def max_amount_of_groups_changed(self,new_amount_groups):
        self.__max_amount_of_groups = new_amount_groups


    @property
    def min_amount_of_users(self):
        return self.__min_amount_of_users


    def min_amount_of_users_changed(self,new_amount_users):
        self.__min_amount_of_users = new_amount_users

    @property
    def each_to_each(self):
        return self.__each_to_each

    def each_to_each_changed(self,new_each_to_each):
        self.__each_to_each = new_each_to_each




    def collect_values(self):
        list_of_settings = []
        list_of_settings.append(self.__country_id)
        list_of_settings.append(self.__max_amount_of_groups)
        list_of_settings.append(self.__min_amount_of_users)
        list_of_settings.append(self.__timeout_between_operations)
        list_of_settings.append(self.__each_to_each)

        return list_of_settings

    def save_settings(self):
        list_of_settings = self.collect_values()
        self.__on_start_settings_values = self.collect_values()
        self.update_settings.emit(list_of_settings)


    def show(self):
        self.set_begins_view_values(self.__on_start_settings_values)
        self.__view_operator.show()

    def hide(self):
        self.__view_operator.hide()

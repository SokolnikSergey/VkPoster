from model.Interfaces.Publisher import Publisher

class ConfigContainerVkOperations(Publisher):

    def __init__(self, country_number = 3,max_amount_of_groups = 50 ,timeout = 5
                 ,min_amount_users_in_group = 100 ,e_to_e = False):
        self.__country_number = country_number
        self.__max_amount_of_groups = max_amount_of_groups
        self.__timeout = timeout
        self.__min_amount_users_in_group = min_amount_users_in_group
        self.__each_to_each = e_to_e

        self.__settings_subscriber = []


    @property
    def country_number(self):
        return self.__country_number


    @country_number.setter
    def country_number(self,new_country_id):
        if(isinstance(new_country_id,(str,int))):
            self.__country_number = new_country_id
            self.country_number_changed()

    @property
    def max_amount_of_groups(self):
        return self.__max_amount_of_groups

    @max_amount_of_groups.setter
    def max_amount_of_groups(self, new_max_amount_of_groups):
        if (isinstance(new_max_amount_of_groups, int)):
            self.__max_amount_of_groups = new_max_amount_of_groups
            self.max_amount_of_groups_changed()

    @property
    def timeout(self):
        return self.__timeout

    @timeout.setter
    def timeout(self, new_timeout):
        if (isinstance(new_timeout, int)):
            self.__timeout = new_timeout
            self.time_out_changed()

    @property
    def min_amount_users_in_group(self):
        return self.__min_amount_users_in_group

    @min_amount_users_in_group.setter
    def min_amount_users_in_group(self,new_min_amount):
        if(isinstance(new_min_amount,(int))):
            self.__min_amount_users_in_group = new_min_amount
            self.min_amount_users_in_group_changed()

    @property
    def each_to_each(self):
        return self.__each_to_each

    @each_to_each.setter
    def each_to_each(self, new_each_to_each):
        if (isinstance(new_each_to_each, (str,int))):
            self.__each_to_each = new_each_to_each
            self.each_to_each_changed()

    def country_number_changed(self):
        for subscriber in self.__settings_subscriber:
            subscriber.country_id_changed(self.__country_number)

    def max_amount_of_groups_changed(self):
        for subscriber in self.__settings_subscriber:
            subscriber.max_amount_of_group_changed(self.__max_amount_of_groups)

    def time_out_changed(self):
        for subscriber in self.__settings_subscriber:
            subscriber.timeout_changed(self.__timeout)

    def min_amount_users_in_group_changed(self):
        for subscriber in self.__settings_subscriber:
            subscriber.min_amount_users_in_group_changed(self.__min_amount_users_in_group)

    def each_to_each_changed(self):
        for subscriber in self.__settings_subscriber:
            subscriber.each_post_to_each_groups_changed(self.__each_to_each)

    def update_all_settings(self,subscriber):
        subscriber.country_id_changed(self.__country_number)
        subscriber.max_amount_of_group_changed(self.__max_amount_of_groups)
        subscriber.timeout_changed(self.__timeout)
        subscriber.each_post_to_each_groups_changed(self.each_to_each)

    def remove_subscriber(self, subscriber):
        if subscriber in self.__settings_subscriber :
            self.__settings_subscriber.remove(subscriber)


    def add_subscriber(self, subscriber):
        if not subscriber in self.__settings_subscriber:
            self.__settings_subscriber.append(subscriber)
            self.update_all_settings(subscriber)

    def clear_all_subscribers(self):
        self.__settings_subscriber.clear()

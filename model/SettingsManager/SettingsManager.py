from model.Interfaces.Subscriber import Subscriber
from model.ActionMaker.ActionMaker import ActionMaker

class SettingsManager(Subscriber):
    def __init__(self,settings_publisher):
        self.__setting_publisher = settings_publisher
        self.subscribe(settings_publisher)


    def country_id_changed(self,new_country_id):
        ActionMaker.COUNTRY_ID = new_country_id + 1

    def max_amount_of_group_changed(self,new_amount_of_group):
        ActionMaker.MAX_AMOUNT_OF_GROUPS = new_amount_of_group

    def timeout_changed(self,new_timeout):
        ActionMaker.TIME_OUT_SEND_POST = new_timeout

    def  min_amount_users_in_group_changed(self,new_min_amount):
        ActionMaker.MIN_AMOUNT_USERS_IN_GROUP = new_min_amount

    def each_post_to_each_groups_changed(self,new_e_to_e):
        ActionMaker.EACH_POST_TO_EACH_GROUP = new_e_to_e

    def limit_reached_just_once_changed(self,new_limit_reached_once):
        ActionMaker.SHOW_LIMIT_REACHED_JUST_ONCE = new_limit_reached_once

    def subscribe(self, publisher):
        publisher.add_subscriber(self)

    def unsubscribe(self, publisher):
        publisher.remove_subscriber(self)
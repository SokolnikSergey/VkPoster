import configparser,os
from model.ConfigParser.ConfigContainerPostToGroup.ConfigContainerVkOpererations import ConfigContainerVkOperations
class ConfigParserVkOperationGathering:
    def __init__(self,path_to_ini = "",config_container = None):
        self.__config_parser = None
        self.__config_container = config_container
        self.__path_to_ini = path_to_ini

        self.create_parser()
        self.read_from_config_file()
        self.fill_container_with_options()

    def create_parser(self):
        self.__config_parser  = configparser.ConfigParser()

    def fill_container_with_options(self):
        if isinstance(self.__config_container,ConfigContainerVkOperations) :
            self.read_country_number_from_ini()
            self.read_max_amount_of_groups_to_search()
            self.read_min_amount_of_users_in_group()
            self.read_each_post_to_each_groups()
            self.read_just_once_limit_reached()
            self.read_timeout_beetween_operations()

    def write_to_config_file(self):
        if self.__config_parser is not  None:
            with open(self.__path_to_ini,"w") as config_file:
                self.__config_parser.write(config_file)

    def read_from_config_file(self):
        if self.__config_parser is not  None :
            if  (os.path.exists(self.__path_to_ini)):
                self.__config_parser.read(self.__path_to_ini)
            else:
                self.set_default_values()
                self.__config_parser.read(self.__path_to_ini)

    def set_default_values(self):

        self.__config_parser.add_section("VkOperations")
        self.__config_parser.set("VkOperations","CountryToSearch",'2')
        self.__config_parser.set("VkOperations","MaxAmountOfGroupsToSearch",'50')
        self.__config_parser.set("VkOperations", "TimeOutBetweenOperations", '5')
        self.__config_parser.set("VkOperations", "MinAmountUsersInGroup", '200')
        self.__config_parser.set("VkOperations", "EachPostToEachGroups", '0')
        self.__config_parser.set("VkOperations", "JustOnceLimitReached", '0')


        self.write_to_config_file()

    def read_country_number_from_ini(self):
        if self.__config_parser is not None:
            if "VkOperations" in self.__config_parser:
                country_number = self.__config_parser["VkOperations"]["CountryToSearch"]
                if  country_number and self.__config_container:
                    self.__config_container.country_number = int(country_number)

    def read_max_amount_of_groups_to_search(self):
        if self.__config_parser is not None:
            if "VkOperations" in self.__config_parser:
                max_amount_of_groups = self.__config_parser["VkOperations"]["MaxAmountOfGroupsToSearch"]
                if(max_amount_of_groups is not None) and self.__config_container:
                    self.__config_container.max_amount_of_groups = int(max_amount_of_groups)

    def read_timeout_beetween_operations(self):
        if self.__config_parser is not None:
            if "VkOperations" in self.__config_parser:
                timeout = self.__config_parser["VkOperations"]["TimeOutBetweenOperations"]
                if (timeout is not None) and self.__config_container:
                    self.__config_container.timeout = int(timeout)

    def read_min_amount_of_users_in_group(self):
        if self.__config_parser is not None:
            if "VkOperations" in self.__config_parser:
                min_amount = self.__config_parser["VkOperations"]["MinAmountUsersInGroup"]
                if (min_amount is not None) and self.__config_container:
                    self.__config_container.min_amount_users_in_group = int(min_amount)


    def read_each_post_to_each_groups(self):
        if self.__config_parser is not None:
            if "VkOperations" in self.__config_parser:
                each_to_each = self.__config_parser["VkOperations"]["EachPostToEachGroups"]
                if (each_to_each is not None) and self.__config_container:
                    self.__config_container.each_to_each = int(each_to_each)

    def read_just_once_limit_reached(self):
        if self.__config_parser is not None:
            if "VkOperations" in self.__config_parser:
                just_once_limit = self.__config_parser["VkOperations"]["JustOnceLimitReached"]
                if (just_once_limit is not None) and self.__config_container:
                    self.__config_container.limit_reached_just_once = int(just_once_limit)


    def write_country_number_from_ini(self,country_number):

        self.__config_container.country_number = country_number
        country_number = str(country_number)
        if(self.__config_parser) and "VkOperations" in self.__config_parser:
            if(isinstance(country_number,str)):
                self.__config_parser["VkOperations"]["CountryToSearch"] = country_number
                self.write_to_config_file()

    def write_max_amount_of_groups_to_search(self, amount_groups):
        self.__config_container.max_amount_of_groups = amount_groups
        amount_groups = str(amount_groups)
        if (self.__config_parser) and "VkOperations" in self.__config_parser:
            if (isinstance(amount_groups,str)):
                self.__config_parser["VkOperations"]["MaxAmountOfGroupsToSearch"] = amount_groups
                self.write_to_config_file()

    def write_timeout_beetween_operations(self, timeout):
        self.__config_container.timeout = timeout
        timeout  = str(timeout)
        if (self.__config_parser) and "VkOperations" in self.__config_parser:
            if (isinstance(timeout,str)):
                self.__config_parser["VkOperations"]["TimeOutBetweenOperations"] = timeout
            self.write_to_config_file()

    def write_min_amount_users_in_group(self, min_amount_users):
        self.__config_container.min_amount_users_in_group = min_amount_users
        min_amount_users = str(min_amount_users)
        if (self.__config_parser) and "VkOperations" in self.__config_parser:
            if (isinstance(min_amount_users, str)):
                self.__config_parser["VkOperations"]["MinAmountUsersInGroup"] = min_amount_users
                self.write_to_config_file()

    def write_each_post_to_each_groups(self, e_to_e):
        self.__config_container.each_to_each = e_to_e
        e_to_e = str(e_to_e)
        if (self.__config_parser) and "VkOperations" in self.__config_parser:
            if (isinstance(e_to_e, str)):
                self.__config_parser["VkOperations"]["EachPostToEachGroups"] = e_to_e
                self.write_to_config_file()


    def write_show_limit_reached_just_once(self, limit_reached):
        self.__config_container.limit_reached_just_once = limit_reached
        limit_reached = str(limit_reached)
        if (self.__config_parser) and "VkOperations" in self.__config_parser:
            if (isinstance(limit_reached, str)):
                self.__config_parser["VkOperations"]["JustOnceLimitReached"] = limit_reached
                self.write_to_config_file()

    def update_values(self,values):
        self.write_country_number_from_ini(values[0])
        self.write_max_amount_of_groups_to_search(values[1])
        self.write_min_amount_users_in_group(values[2])
        self.write_timeout_beetween_operations(values[3])
        self.write_each_post_to_each_groups(values[4])
        self.write_show_limit_reached_just_once(values[5])

    def write_element(self,section,element,value):
        self.__config_parser[section][element] = value

    def read_element(self,section,element):
        return self.__config_parser[section][element]

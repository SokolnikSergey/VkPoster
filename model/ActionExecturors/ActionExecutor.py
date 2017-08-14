from model.Enums.ActionsEnum import ActionsEnum

class ActionExecutor:

    def __init__(self,vk_opeartor,container_operator):
        self.dict_compliance = {vk_opeartor : (ActionsEnum.SEND_POSTS_TO_GROUPS,ActionsEnum.SEARCH_GROUPS),
            container_operator : (ActionsEnum.ADD_POST,ActionsEnum.EDIT_POST,ActionsEnum.REMOVE_POST,
                                  ActionsEnum.READ_ALL_RECORDS_FROM_DB)}

    def decide_type_of_action(self,name_action):
        operation_compliance = self.dict_compliance.items()
        for operator,operations in list(operation_compliance):
            if(name_action in operations):
                return operator

    def execute_action(self,cmd,data):
        operator =  self.decide_type_of_action(cmd)
        if operator is not None :
            operator.execute(cmd,data)



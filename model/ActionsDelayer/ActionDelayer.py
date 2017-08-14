from PyQt5.QtCore import QObject
from model.ActionsDelayer.ActionReaderWriter import ActionReadWrite

class ActionDelayer(QObject):

    def __init__(self,action_holder,file_path = '../DB/DelayedActions'):
        super(ActionDelayer, self).__init__()
        self.__file_path = file_path
        self.__action_holder = action_holder


    def write_all_action_to_file(self):
        actions = self.__action_holder.leisurely_queue.copy()
        if actions:
            self.__action_holder.clear_leisurely_queue()
            ActionReadWrite.write_actions_to_file(self.__file_path,actions)

    def read_actions_from_file(self):
        actions = ActionReadWrite.read_actions_from_file(self.__file_path)
        if actions:
            self.__action_holder.add_action_to_leisurely_queue(actions)
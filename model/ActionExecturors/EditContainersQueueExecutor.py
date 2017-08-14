from  model.ActionExecturors.AbstractQueueExecutor import AbstractQueueExecutor
from PyQt5.QtCore import QTimer
class EditContainersQueueExecutor(AbstractQueueExecutor):

    def __init__(self,publisher_edit_containers_queue,edit_containers_queue,action_executor):
        self.__publisher_edit_containers_queue = publisher_edit_containers_queue
        self.__edit_containers_queue = edit_containers_queue
        self.__action_executor = action_executor
        self.create_timer()
        self.subscribe(self.__publisher_edit_containers_queue)

    def create_timer(self):
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.execute_action)

    def execute_action(self):
        action = self.__publisher_edit_containers_queue.take_action_from_edit_containers_queue()
        if (action is not None):
            self.__action_executor.execute_action(action.cmd, action.data)
            self.__timer.setInterval(int(action.time_out * 1000))
        else:
            self.__timer.stop()

    def start_executing(self):
        if not self.__timer.isActive():
            self.__timer.setInterval(1)
            self.__timer.start()

    def subscribe(self, publisher):
        self.__publisher_edit_containers_queue.add_subscriber_for_edit_container_queue(self)

    def unsubscribe(self, publisher):
        self.__publisher_edit_containers_queue.remove_subscriber_for_edit_container_queue(self)
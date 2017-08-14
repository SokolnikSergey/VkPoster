from model.ActionExecturors.AbstractQueueExecutor import AbstractQueueExecutor
from PyQt5.QtCore import QTimer,QObject,pyqtSignal

class LeisurelyQueueExecutor(AbstractQueueExecutor,QObject):
    progress_changed = pyqtSignal(int,int,int) ##done,remainded,failed

    def __init__(self,publisher_leisurely_queue,leisurely_queue,action_executor):
        super(LeisurelyQueueExecutor, self).__init__()

        self.__counter_of_action_has_done = 0
        self.__counter_of_actions_has_failed = 0
        self.__publisher_leisurely_queue = publisher_leisurely_queue
        self.__leisurely_queue = leisurely_queue
        self.__action_executor = action_executor
        self.create_timer()
        self.subscribe(self.__publisher_leisurely_queue)
        self.__list_of_action_amount_sibscribers = []
        self.create_auxiliary_attributes()

    def create_auxiliary_attributes(self):
        self.__available_to_execute_next = True

    def last_action_has_executed(self):
        self.__available_to_execute_next = True

    def increment_action_has_done(self):
        self.__counter_of_action_has_done += 1

    def increment_action_has_failed(self):
        self.__counter_of_actions_has_failed += 1

    def create_timer(self):
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.execute_action)

    def execute_action(self):
        if self.__available_to_execute_next:
            self.__available_to_execute_next = False ## TRANSFER TO STATE WAITING OF ECECUTE ACTION

            action = self.__publisher_leisurely_queue.take_action_from_leisurely_queue()

            if (action is not None):
                self.__action_executor.execute_action(action.cmd, action.data)
                self.__timer.setInterval(int(action.time_out * 1000))

            else:
                self.__available_to_execute_next = True
                self.__timer.stop()


    def notify_suscribers_about_changes_of_amount(self):
        self.progress_changed.emit(self.__counter_of_action_has_done,
        self.__publisher_leisurely_queue.size_of_leisurely_queue(),self.__counter_of_actions_has_failed)

    def start_executing(self):
        self.notify_suscribers_about_changes_of_amount()
        if not self.__timer.isActive():
            self.__timer.setInterval(1)
            self.__timer.start()

    def subscribe(self, publisher):
        self.__publisher_leisurely_queue.add_subscriber_for_leisure_queue(self)

    def unsubscribe(self, publisher):
        self.__publisher_leisurely_queue.remove_subscriber_for_leisure_queue(self)


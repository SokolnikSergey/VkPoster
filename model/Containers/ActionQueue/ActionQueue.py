from model.Containers.ActionQueue.Action import Action
class ActionQueue:

    def __init__(self,leisurely__actions,hurriedly_actions,edit_containers_actions):
        self.__leisurely_queue = leisurely__actions
        self.__hurriedly_queue = hurriedly_actions
        self.__edit_containers_queue = edit_containers_actions

        self.__leisurely_queue_subscribers = []
        self.__hurriedly_queue_subscribers = []
        self.__edit_containers_queue_subscribers = []


    @property
    def leisurely_queue(self):
        return self.__leisurely_queue

    @property
    def hurriedly_queue(self):
        return self.__hurriedly_queue

    @property
    def edit_containers_queue(self):
        return self.__edit_containers_queue

    def size_of_leisurely_queue(self):
        return len(self.__leisurely_queue)

    def size_of_hurriedly_queue(self):
        return len(self.__hurriedly_queue)

    def size_of_edit_container_queue(self):
        return len(self.__edit_containers_queue)

    def add_action_to_leisurely_queue(self,action, prepend = False):
        if(isinstance(action,Action)):
            if prepend:
                self.__leisurely_queue = [action] + self.__leisurely_queue
            else:
                self.__leisurely_queue.append(action)

        if(isinstance(action,list) and all(isinstance(act,Action) for act in  action)):
            self.__leisurely_queue.extend(action)

        for subscriber in self.__leisurely_queue_subscribers:
            subscriber.start_executing()

    def add_action_to_hurriedly_queue(self,action):
        if(isinstance(action,Action)):
            self.__hurriedly_queue.append(action)

        for subscriber in self.__hurriedly_queue_subscribers:
            subscriber.start_executing()

    def add_action_to_edit_containers_queue(self,action):
        if(isinstance(action,Action)):
            self.__edit_containers_queue.append(action)

        for subscriber in self.__edit_containers_queue_subscribers:
            subscriber.start_executing()

    def take_action_from_leisurely_queue(self):
        if len(self.__leisurely_queue):
           return  self.__leisurely_queue.pop(0)

    def take_action_from_hurriedly_queue(self):
        if len(self.__hurriedly_queue):
            return self.__hurriedly_queue.pop(0)

    def take_action_from_edit_containers_queue(self):
        if len(self.__edit_containers_queue):
            return self.__edit_containers_queue.pop(0)

    def clear_leisurely_queue(self):
        self.__leisurely_queue.clear()

    def clear_hurriedly_queue(self):
        self.__hurriedly_queue.clear()

    def clear_edit_containers_queue(self):
        self.__edit_containers_queue.clear()

    def add_subscriber_for_leisure_queue(self,subscriber):
        self.__leisurely_queue_subscribers.append(subscriber)

    def add_subscriber_for_hurriedly_queue(self,subscriber):
        self.__hurriedly_queue_subscribers.append(subscriber)

    def add_subscriber_for_edit_container_queue(self,subscriber):
        self.__edit_containers_queue_subscribers.append(subscriber)
        
    def remove_subscriber_for_leisure_queue(self,subscriber):
        if(subscriber in self.__leisurely_queue_subscribers):
            self.__leisurely_queue_subscribers.remove(subscriber)

    def remove_subscriber_for_hurriedly_queue(self,subscriber):
        if(subscriber in self.__hurriedly_queue_subscribers):
            self.__hurriedly_queue_subscribers.remove(subscriber)

    def remove_subscriber_for_edit_container_queue(self,subscriber):
        if(subscriber in self.__edit_containers_queue_subscribers):
            self.__edit_containers_queue_subscribers.remove(subscriber)

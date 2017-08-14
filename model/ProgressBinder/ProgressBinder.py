class ProgressBinder:
    def __init__(self,start_choice,post_to_group,p_to_g_notifier):
        self.__start_choice = start_choice
        self.__post_to_group  = post_to_group
        self.__post_to_group_notifier = p_to_g_notifier

        self.bind_start_choice_progress()

    def bind_start_choice_progress(self):
        self.__post_to_group_notifier.progress_changed.connect(self.__start_choice.progress_posts_changed)
        self.__post_to_group_notifier.progress_changed.connect(self.__post_to_group.amount_actions_changed)
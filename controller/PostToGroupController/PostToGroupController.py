class PostToGroupController:

    @staticmethod
    def is_allowed_send_posts_to_group(list_of_posts,list_of_groups):
        if (len(list_of_posts) and len(list_of_groups)):
            return True
        return False

    @staticmethod
    def is_allowed_search_post(field_of_search):
        if isinstance(field_of_search,str) and  field_of_search != '':
            return True
        return False

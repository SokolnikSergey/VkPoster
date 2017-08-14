from enum import Enum

class ActionsEnum(Enum):
    SEND_POSTS_TO_GROUPS = 1
    SEARCH_GROUPS = 2

    EDIT_POST = 3
    REMOVE_POST = 4
    ADD_POST = 5

    READ_ALL_RECORDS_FROM_DB = 6

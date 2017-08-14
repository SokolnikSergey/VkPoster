class VkAuthorizationController:

    @staticmethod
    def is_session_active(session):
        if session:
            return True
        return False
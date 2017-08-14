class CustomException(Exception):
    def __init__(self,message,type_of_ex,ptr_to_fix,ptr_to_execute,*args_to_execute):
        self.message = message
        self.type_of_ex = type_of_ex
        self.set_matches(ptr_to_fix,ptr_to_execute,args_to_execute)

    def set_matches(self,ptr_to_fix,ptr_to_execute,args_to_execute):
        self.fix = ptr_to_fix
        self.retry_execute = ptr_to_execute
        if len(args_to_execute) :
            self.args_to_execute = args_to_execute
        else:
            self.args_to_execute = None

    def fix(self):
        pass

    def retry_execute(self):
        pass

class Action:
    def __init__(self, cmd = None,data=None,time_out=0):
        self.__cmd = cmd
        self.__data = data
        self.__time_out = time_out

    @property
    def cmd(self):
        return self.__cmd

    @cmd.setter
    def cmd(self,new_cmd):
        self.__cmd = new_cmd

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        if(isinstance(new_data,list)):
            self.__data = new_data


    @property
    def time_out(self):
        return self.__time_out

    @time_out.setter
    def time_out(self,new_time_out):
        if (isinstance(new_time_out,int)):
            self.__time_out = new_time_out
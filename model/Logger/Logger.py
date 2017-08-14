import logging
import threading

class MyLogger():
    PATH_TO_FILE = "logger.log"
    _logger = None ###The single object
    _name = "root"
    lock = threading.Lock() ## Locker for logger ,
                            ## adjust permisions to logger

    def __init__(self):
        self.lock.acquire()
        if MyLogger._logger is None :
            MyLogger._logger =  self.create_logger()
        self.__dict__['_MyLogger__logger'] = MyLogger._logger
        self.lock.release()


    def __getattr__(self, attr):
        self.lock.acquire()
        ga = getattr(self._logger, attr)
        self.lock.release()

        return ga

    def __setattr__(self, attr, value):
        return setattr(self._logger, attr, value)

    def change_name(self,new_name):
        if(isinstance(new_name,str)):
            MyLogger._logger.name = new_name
            return True
        return False

    def change_level(self,new_level):
        if( new_level and
            new_level in (logging.DEBUG,logging.INFO,logging.WARNING,logging.ERROR,logging.FATAL) or
            new_level in ('CRITICAL','ERROR','WARN','WARNING','INFO','DEBUG') or
            new_level in (10,20,30,40,50)) :

            self._logger.setLevel(new_level)

    def create_logger(self):

        logging.basicConfig(level=logging.INFO)

        log = logging.getLogger()
        log.setLevel("DEBUG")
        formatter = self.get_formatter()

        handler = self.get_handler(formatter)

        log.addHandler(handler)

        return log

    def get_formatter(self):
         return logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_handler(self,formatter):

        handler = logging.FileHandler(filename = MyLogger.PATH_TO_FILE)
        handler.setFormatter(formatter)

        return handler

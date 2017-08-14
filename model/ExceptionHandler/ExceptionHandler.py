from PyQt5.QtCore import QObject, pyqtSignal


class ExceptionHandler(QObject):
    show_warning_dialog = pyqtSignal(str)
    show_accept_dialog = pyqtSignal(str)

    hide_warning_dialog = pyqtSignal()

    def __init__(self):
        super(ExceptionHandler, self).__init__()
        self.__exceptions_queue = None

    def handle_warning(self, text, fix_method, args):
        if self.__exceptions_queue is None:
            self.__exceptions_queue = []
            self.set_attributes(text, fix_method, args)
            self.show_warning_dialog.emit(self.__text)

        else:
            if not (text, fix_method, args) in self.__exceptions_queue:
                self.__exceptions_queue.append((text, fix_method, args))
            else:
                # replace actual exception at the end (the first of handling)

                if (self.__exceptions_queue.index((text, fix_method, args)) != len(self.__exceptions_queue) - 1):
                    self.__exceptions_queue.remove((text, fix_method, args))
                    self.__exceptions_queue.append((text, fix_method, args))

            self.update_actual_exception()

    def update_actual_exception(self):
        if len(self.__exceptions_queue):
            actual_ex = self.__exceptions_queue[len(self.__exceptions_queue) - 1]
            self.set_attributes(*actual_ex)
            self.show_warning_dialog.emit(self.__text)
            self.__exceptions_queue.pop()

    def set_attributes(self, text, fix_method, arguments):
        self.__text = text
        self.__fix_method = fix_method
        self.__args_to_fix_method = arguments

    def fix(self):
        if (self.__fix_method):
            self.__fix_method(*self.__args_to_fix_method)








from PyQt5.QtWidgets import QListWidget
from view.EditPost.MyWheelScroller import MyWheelScroller
class ListWidgetCustomScroll(QListWidget):

    def __init__(self):
        super(ListWidgetCustomScroll, self).__init__()
        self.__my_wheel_scroller = MyWheelScroller()
        self.bind_signals()

    def wheelEvent(self, eventWheel):
        if eventWheel.angleDelta().y() > 0:
            self.__my_wheel_scroller.prepend_new_scroll_action(MyWheelScroller.UP_WHEEL_ACTION)
        else:
            self.__my_wheel_scroller.prepend_new_scroll_action(MyWheelScroller.DOWN_WHEEN_ACTION)

    def scroll_up_list(self):
        self.verticalScrollBar().setValue(self.verticalScrollBar().value() - 1)

    def scroll_down_list(self):
        self.verticalScrollBar().setValue(self.verticalScrollBar().value() + 1)

    def bind_signals(self):
        self.__my_wheel_scroller.increment_offset.connect(self.scroll_up_list)
        self.__my_wheel_scroller.decrement_offset.connect(self.scroll_down_list)

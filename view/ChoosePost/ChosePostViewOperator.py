from model.MyListWidgetItem.MyListWidgetItem import MyListWidgetItem
from PyQt5.QtCore import QObject,QSize,pyqtSignal
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QMessageBox

class ChosePostViewOperator(QObject):

    chose_post_signal  = pyqtSignal(str)
    add_new_post_signal = pyqtSignal()
    delete_post_signal = pyqtSignal(str)
    choose_post_closed = pyqtSignal()

    btn_back_clicked = pyqtSignal()
    occured_warning_view = pyqtSignal(str, object, tuple)  ##signal to fill warning pop-up message

    def __init__(self,view):
        super(ChosePostViewOperator, self).__init__()
        self.__window  = view
        self.snapping_internal_signals()

    def remove_items_from_post_list_widget(self,posts):
        i = 0
        texts_to_delete = [post.text for post in posts]
        while(i < len(self.__window.list_post_widget)):
            if self.__window.list_post_widget.item(i).whatsThis() in texts_to_delete:
                self.__window.list_post_widget.takeItem(i)
            else:
                i+=1

        if len(self.__window.list_post_widget) == 0:
            self.__window.blinking_label.info_label.hide()

    def add_item_to_post_list_widget(self,text,list_of_photos):
        item = QListWidgetItem()
        item.setSizeHint(QSize(200, 100))
        l = MyListWidgetItem(text, list_of_photos, 5, 10)
        self.__window.list_post_widget.addItem(item)
        self.__window.list_post_widget.setItemWidget(item, l)
        item.setWhatsThis(text)

    def add_items_to_post_list_widget(self,posts):
        if len(posts) > 0:
            self.__window.blinking_label.info_label.show()

        for post in posts:
            self.add_item_to_post_list_widget(post.text,post.list_of_photos)

    def fill_posts_list_widget(self,list_of_posts):
        self.__window.list_post_widget.clear()
        self.add_items_to_post_list_widget(list_of_posts)

    def clear_posts_list_widget(self):
        self.__window.list_post_widget.clear()

    def double_clicked_under_item(self,item):
        self.chose_post_signal.emit(item.whatsThis())

    def show_confirmation_delete_post(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Do you really want to delete the post?")
        msgBox.setWindowTitle("Delete post?")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        return msgBox.exec()

    def delete_post_clicked(self):
        current_item = self.__window.list_post_widget.currentItem()
        if current_item:
            if self.show_confirmation_delete_post() == QMessageBox.Ok:
                self.delete_post_signal.emit(current_item.whatsThis())
        else:
            self.occured_warning_view.emit("Choose at least one post to delete it", None, ())

    def add_new_post_clicked(self):
        self.add_new_post_signal.emit()

    def snapping_internal_signals(self):
        self.__window.list_post_widget.itemDoubleClicked.connect(self.double_clicked_under_item)
        self.__window.choose_post_closed.connect(self.choose_post_closed)
        self.__window.btn_delete_post.clicked.connect(self.delete_post_clicked)
        self.__window.btn_add_new_post.clicked.connect(self.add_new_post_clicked)

        self.__window.btn_backed.clicked.connect(self.btn_back_clicked)


    def show(self):
        self.__window.show()
        self.__window.raise_()
        self.__window.activateWindow()

    def hide(self):
        self.__window.hide()




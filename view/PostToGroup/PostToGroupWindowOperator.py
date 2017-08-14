from PyQt5.QtCore import QObject,pyqtSignal,QSize,Qt
from PyQt5.QtWidgets import QListWidgetItem
from model.MyListWidgetItem.MyListWidgetItem import MyListWidgetItem
from view.PostToGroup.PostToGroupWindow import PostToGroupWindow


class PostToGroupWindowOperator(QObject):


    send_posts_signal = pyqtSignal(list,list)
    search_groups_signal = pyqtSignal(str)
    btn_edit_post_clicked = pyqtSignal()
    btn_read_all_records_clicked = pyqtSignal()
    btn_helper_clicked = pyqtSignal()
    btn_back_clicked = pyqtSignal()
    btn_recover_actions_clicked = pyqtSignal()

    btn_change_account_pressed = pyqtSignal()

    def __init__(self,view):
        super(PostToGroupWindowOperator, self).__init__()
        self.__window = view
        self.__previous_text = ""
        self.snapping_internal_signals()

    def snapping_internal_signals(self):
        self.__window.list_post_widget.itemPressed.connect(self.toggle_post_list_checked)

        self.__window.list_group_widget.itemPressed.connect(self.toggle_group_list_checked)
        self.__window.btn_search_groups.clicked.connect(self.search_groups_clicked)

        self.__window.btn_start_spam.clicked.connect(self.deactivate_send_posts)
        self.__window.btn_start_spam.clicked.connect(self.post_to_group_clicked)

        self.__window.btn_edit_post.clicked.connect(self.btn_edit_post_clicked)
        self.__window.btn_read_all_records.clicked.connect(self.btn_read_all_records_clicked)
        self.__window.btn_help.clicked.connect(self.btn_helper_clicked)
        self.__window.check_box_all_ticks_groups.stateChanged.connect(self.toggle_all_ticks_groups)
        self.__window.btn_back.clicked.connect(self.btn_back_clicked)
        self.__window.btn_recover_actions.clicked.connect(self.btn_recover_actions_clicked)


    @property
    def previous_text(self):
        return self.__previous_text

    @previous_text.setter
    def previous_text(self,new_text):
        if(isinstance(new_text,str)):
            self.__previous_text = new_text

    def toggle_all_ticks_groups(self,state):
        if(state):
            self.remove_all_ticks()
        else:
            self.add_all_ticks()

    def remove_all_ticks(self):
        i = 0
        while (i < len(self.__window.list_group_widget)):
            self.__window.list_group_widget.item(i).setCheckState(Qt.Unchecked)
            i += 1

    def add_all_ticks(self):
        i = 0
        while (i < len(self.__window.list_group_widget)):
            self.__window.list_group_widget.item(i).setCheckState(Qt.Checked)
            i += 1

    def toggle_post_list_checked(self):
        item = self.__window.list_post_widget.currentItem()
        if item.checkState():
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)

        self.activate_send_posts()

    def toggle_group_list_checked(self):
        item = self.__window.list_group_widget.currentItem()
        if item.checkState():
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)

    def remove_items_from_post_list_widget(self,posts):
        i = 0
        texts_to_delete = [post.text for post in posts]
        while(i < len(self.__window.list_post_widget)):
            if self.__window.list_post_widget.item(i).whatsThis() in texts_to_delete:
                self.__window.list_post_widget.takeItem(i)
            else:
                i+=1

    def remove_items_from_group_list_widget(self,groups):
        gids_to_delete = [str(group.gid) for group in groups]
        i = 0
        while (i < len(self.__window.list_group_widget) ):
            if self.__window.list_group_widget.item(i).whatsThis() in gids_to_delete:
                self.__window.list_group_widget.takeItem(i)
            else:
                i += 1

    def add_item_to_post_list_widget(self,text,list_of_photos):
        item = QListWidgetItem()
        item.setSizeHint(QSize(200, 100))
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(0)
        l = MyListWidgetItem(text, list_of_photos, 5, 10)
        self.__window.list_post_widget.addItem(item)
        self.__window.list_post_widget.setItemWidget(item, l)
        item.setWhatsThis(text)

    def update_amount_of_actions(self,action_have_done,actions_remainded,actions_failed):
        text = self.__window.lable_amount_actions.text().split("=")
        text[1] = " " + str(action_have_done) + "/" + str(actions_remainded  + action_have_done) + '/' + str(actions_failed)
        text = "=".join(text)
        self.__window.lable_amount_actions.setText(text)

    def add_item_to_group_list_widget(self,title,photo,gid):

        item = QListWidgetItem()
        item.setSizeHint(QSize(200, 100))
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(2)
        l = MyListWidgetItem(title,photo, 5, 10)
        self.__window.list_group_widget.addItem(item)
        self.__window.list_group_widget.setItemWidget(item, l)
        item.setWhatsThis(str(gid))

    def add_items_to_group_list_widget(self,groups):

        for group in groups:
            self.add_item_to_group_list_widget(group.title,[group.photo],group.gid)

    def add_items_to_post_list_widget(self,posts):
        for post in posts:
            self.add_item_to_post_list_widget(post.text,post.list_of_photos)

    def fill_posts_list_widget(self,list_of_posts):

        self.__window.list_post_widget.clear()
        self.add_items_to_post_list_widget(list_of_posts)

    def fill_groups_list_widget(self,list_of_groups):

        self.__window.list_post_widget.clear()
        self.add_items_to_group_list_widget(list_of_groups)

    def clear_posts_list_widget(self):
        self.__window.list_post_widget.clear()

    def clear_groups_list_widget(self):
        self.__window.list_group_widget.clear()

    def search_groups_clicked(self):
        self.search_groups_signal.emit(self.__window.line_post_name.text())

        if not self.compare_new_with_previous_text(self.__window.line_post_name.text()):
            self.activate_send_posts()

    def find_togged_posts(self):
        list_posts_ids = []
        for i in range(len(self.__window.list_post_widget)):
            if self.__window.list_post_widget.item(i).checkState():
                list_posts_ids.append(self.__window.list_post_widget.item(i).whatsThis())
        return list_posts_ids

    def find_togged_groups(self):
        list_of_texts = []
        for i in range(len(self.__window.list_group_widget)):
            if self.__window.list_group_widget.item(i).checkState():
                list_of_texts.append(self.__window.list_group_widget.item(i).whatsThis())
        return list_of_texts

    def post_to_group_clicked(self):
        self.send_posts_signal.emit(self.find_togged_posts(),self.find_togged_groups())

    def compare_new_with_previous_text(self,new_text):
        result = (self.__previous_text == new_text)
        self.previous_text = new_text

        if result:
            return True
        return False

    def deactivate_send_posts(self):
        self.__window.btn_start_spam.setEnabled(False)

    def activate_send_posts(self):
        self.__window.btn_start_spam.setEnabled(True)


    ###########################

    def show(self):
        self.__window.show()

    def hide(self):
        self.__window.hide()



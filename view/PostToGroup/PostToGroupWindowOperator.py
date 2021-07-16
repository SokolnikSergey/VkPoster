from PyQt5.QtCore import QObject,pyqtSignal,QSize,Qt
from PyQt5.QtWidgets import QListWidgetItem
from model.MyListWidgetItem.MyListWidgetItem import MyListWidgetItem

class PostToGroupWindowOperator(QObject):


    send_posts_signal = pyqtSignal(list,list)
    search_groups_signal = pyqtSignal(str)
    btn_edit_post_clicked = pyqtSignal()
    btn_read_all_records_clicked = pyqtSignal()
    btn_helper_clicked = pyqtSignal()
    btn_back_clicked = pyqtSignal()
    btn_recover_actions_clicked = pyqtSignal()
    btn_make_resendings = pyqtSignal()

    btn_change_account_pressed = pyqtSignal()
    find_resend_post_by_text = pyqtSignal(str)

    def __init__(self,view):
        super(PostToGroupWindowOperator, self).__init__()
        self.__window = view
        self.__previous_text = ""
        self.snapping_internal_signals()

        self.__last_cleared_groups = []
        self.__last_group_states = []
        self.__last_scroll_state = None
        self.__disabled_resend_post_buttons_txts = []

    def snapping_internal_signals(self):
        self.__window.list_post_widget.itemPressed.connect(self.toggle_post_list_checked)

        self.__window.list_group_widget.itemPressed.connect(self.toggle_group_list_checked)
        self.__window.btn_search_groups.clicked.connect(self.search_groups_clicked)
        self.__window.btn_start_spam.clicked.connect(self.post_to_group_clicked)

        self.__window.btn_edit_post.clicked.connect(self.btn_edit_post_clicked)
        self.__window.btn_read_all_records.clicked.connect(self.btn_read_all_records_clicked)
        self.__window.btn_help.clicked.connect(self.btn_helper_clicked)
        self.__window.check_box_all_ticks_groups.stateChanged.connect(self.toggle_all_ticks_groups)
        self.__window.btn_back.clicked.connect(self.btn_back_clicked)
        self.__window.btn_recover_actions.clicked.connect(self.btn_recover_actions_clicked)
        self.__window.btn_make_resendings_clicked.connect(self.btn_make_resendings)
        self.__window.btn_make_resendings_clicked.connect(self.disable_hint_about_resendings)
        self.__window.btn_make_resendings_clicked.connect(self.store_btn_resend_disabled)

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
        item = self.current_post_item()
        if item.checkState():
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)

        self.find_resend_post_by_text.emit(item.whatsThis())
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

    def add_item_to_group_list_widget(self,title,photo,gid, widget_checked_state):

        item = QListWidgetItem()
        item.setSizeHint(QSize(200, 100))
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(widget_checked_state)
        l = MyListWidgetItem(title,photo, 5, 10)
        self.__window.list_group_widget.addItem(item)
        self.__window.list_group_widget.setItemWidget(item, l)
        item.setWhatsThis(str(gid))

    def add_items_to_group_list_widget(self, groups):
        counter = 0
        the_same_groups = self.is_the_same_groups(groups)
        for group in groups:
            state = self.__last_group_states[counter] if the_same_groups else Qt.Checked
            self.add_item_to_group_list_widget(group.title,[group.photo],group.gid, state)
            counter += 1
        if the_same_groups and self.__last_scroll_state is not None:
            self.__window.list_group_widget.verticalScrollBar().setValue(self.__last_scroll_state)
        if not the_same_groups:
            self.__window.check_box_all_ticks_groups.setChecked(False)
            self.add_all_ticks()
        self.activate_btn_search_groups()

    def add_items_to_post_list_widget(self,posts):
        for post in posts:
            self.add_item_to_post_list_widget(post.text,post.list_of_photos)

    def fill_posts_list_widget(self,list_of_posts):

        self.__window.list_post_widget.clear()
        self.add_items_to_post_list_widget(list_of_posts)

    def is_the_same_groups(self, new_groups):
        current_gids = []
        for group in new_groups:
            current_gids.append(group.gid)

        return self.__last_cleared_groups == current_gids

    def fill_groups_list_widget(self,list_of_groups):
        self.__window.list_post_widget.clear()
        self.add_items_to_group_list_widget(list_of_groups)

    def clear_posts_list_widget(self):
        self.__window.list_post_widget.clear()

    def clear_groups_list_widget(self):
        self.__last_cleared_groups = []
        self.__last_group_states = []

        self.__last_scroll_state = self.__window.list_group_widget.verticalScrollBar().value()
        for x in range(self.__window.list_group_widget.count()):
            self.__last_cleared_groups.append(int(self.__window.list_group_widget.item(x).whatsThis()))
            self.__last_group_states.append(self.__window.list_group_widget.item(x).checkState())

        self.__window.list_group_widget.clear()

    def search_groups_clicked(self):
        self.search_groups_signal.emit(self.__window.line_post_name.text())
        self.deactivate_btn_search_groups()

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

    def deactivate_btn_search_groups(self):
        self.__window.btn_search_groups.setEnabled(False)

    def activate_send_posts(self):
        self.__window.btn_start_spam.setEnabled(True)

    def activate_btn_search_groups(self):
        self.__window.btn_search_groups.setEnabled(True)

    def show_upload_image_text(self):
        self.__window.blinking_label.info_label.show()
        self.__window.blinking_label.start_blinking()

    def hide_upload_image_text(self):
        self.__window.blinking_label.info_label.hide()

    def show_hint_about_resendings(self, text_to_show, post_text):
        self.__window.append_resending_button(text_to_show, post_text not in self.__disabled_resend_post_buttons_txts)

    def hide_hint_about_resendings(self):
        self.__window.remove_resending_button()

    def disable_hint_about_resendings(self):
        self.__window.btn_make_resendings.setEnabled(False)

    def current_post_item(self):
        return self.__window.list_post_widget.currentItem()

    def store_btn_resend_disabled(self):
        current_post_item = self.current_post_item()
        self.__disabled_resend_post_buttons_txts.append(current_post_item.whatsThis())


    ###########################

    def show(self):
        self.__window.show()
        self.__window.raise_()
        self.__window.activateWindow()

    def hide(self):
        self.__window.hide()



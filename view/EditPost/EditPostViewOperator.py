from PyQt5.QtCore import QObject,pyqtSignal
from view.EditPost.MyFileDialog import MyFileDialog
from model.PhotoConvertionOperations.PhotoConvertionOperations import PhotoConvertionOperations

class EditPostViewOperator(QObject):

    save_changes_signal = pyqtSignal(str,list)
    edit_post_closed = pyqtSignal()

    def __init__(self,window):
        super(EditPostViewOperator, self).__init__()
        self.__window = window
        self.file_dialog = MyFileDialog()
        self.snapping_internal_signals()


    def save_changes(self):
        self.save_changes_signal.emit(self.__window.text_edit.toPlainText(),self.__window.widget_for_photos.list_pictures)

    def fill_text(self,new_text):
        if isinstance(new_text,str):
            self.__window.text_edit.setText(new_text)

    def fill_list_of_photos(self,list_of_photos):
        self.__window.widget_for_photos.list_pictures = list_of_photos.copy()

    def add_photos(self,photos):
        self.__window.widget_for_photos.list_pictures.extend(photos)
        self.__window.my_resize()
        self.__window.repaint()

    def remove_photo(self):
        if len(self.__window.widget_for_photos.list_pictures):
            self.__window.widget_for_photos.list_pictures.pop(
                self.__window.widget_for_photos.picture_offset)
            self.__window.repaint()

    def clear_list_of_photos(self):
        self.__window.widget_for_photos.list_pictures = []
        self.__window.repaint()

    def processing_file_dialog(self):
        self.file_dialog.show()
        if self.file_dialog.exec_():
            self.add_photos(PhotoConvertionOperations.convert_paths_to_QImages(self.file_dialog.selectedFiles()))


    def show(self):
        self.__window.show()

    def hide(self):
        self.__window.hide()

    def snapping_internal_signals(self):
        self.__window.widget_for_buttons.btn_delete_all_photos.clicked.connect(self.clear_list_of_photos)
        self.__window.widget_for_buttons.btn_del_photo.clicked.connect(self.remove_photo)
        self.__window.widget_for_buttons.btn_add_new_photos.clicked.connect(self.processing_file_dialog)
        self.__window.widget_for_buttons.btn_save_post.clicked.connect(self.save_changes)

        self.__window.edit_post_closed.connect(self.edit_post_closed)


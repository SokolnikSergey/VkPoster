from view.EditPost.EditPostViewOperator import EditPostViewOperator
from PyQt5.QtCore import QObject,pyqtSignal
from view.EditPost.EditPostWindow import EditPostWindow
from controller.EditPost.EditPostController import EditPostController
from model.EditPost.EditPostBinder import EditPostBinder
from model.PhotoConvertionOperations.PhotoConvertionOperations import PhotoConvertionOperations
from model.DBOperations.DBOperations import DBOperations

class EditPostModel(QObject):

    post_changed = pyqtSignal(str,str,list) #source_text,new_text,list_of_photos
    edit_post_closed = pyqtSignal()
    post_added = pyqtSignal(str,list)

    occured_warning = pyqtSignal(str,object,tuple) ##signal to fill warning pop-up message
                                                    #(str = text,object = fix method
                                                    # tuple = params for fix method)
    def __init__(self, db):
        super(EditPostModel, self).__init__()
        self.__source_text = ""
        self.__source_list_of_photos = []
        self.__view_operator = None
        self.create_view()
        self.__db = db
        self.__binder = EditPostBinder(self,self.__view_operator)

    def save_changed_post(self,text,list_of_photos):
        path_new_images = PhotoConvertionOperations.convert_QImages_to_paths(list_of_photos)

        is_allowed_pictutes = EditPostController.is_allowed_to_add_photos(list_of_photos)
        is_allowed_text = EditPostController.is_allowed_text(text)
        is_post_changed = EditPostController.is_post_changed(self.__source_text,text,self.__source_list_of_photos,list_of_photos)

        texts = []
        for record in DBOperations.read_all_records(self.__db):
            texts.append(record[0].strip())
        text_for_post_is_uniq = text.strip() not in texts

        if is_allowed_pictutes and is_allowed_text and is_post_changed and text_for_post_is_uniq:
            if self.__source_list_of_photos == [] and self.__source_text == "":
                self.post_added.emit(text, path_new_images)
            else:
                self.post_changed.emit(self.__source_text, text, path_new_images)

        else:
            if not is_allowed_pictutes:
                self.occured_warning.emit("Too many pictures"
                                      "Should be less than 10!",None,())

            if not is_allowed_text:
                self.occured_warning.emit("There is no text, please input text!",None,())

            if not is_post_changed:
                self.occured_warning.emit("There are no changes compared to the previous",
                                          None,())

            if not text_for_post_is_uniq:
                self.occured_warning.emit("The post with the text is already exists. Text should be uniq",
                                          None, ())

    def create_view(self):
        self.__view_operator = EditPostViewOperator(EditPostWindow())

    def update_view(self,text = "" ,list_of_photos = None):

        if not list_of_photos :
            list_of_photos = []

        self.__source_text = text
        self.__source_list_of_photos = list_of_photos

        self.__view_operator.fill_text(text)
        self.__view_operator.fill_list_of_photos(list_of_photos)

    def show(self):
        self.__view_operator.show()

    def hide(self):
        self.__view_operator.hide()
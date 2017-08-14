from model.Enums.ActionsEnum import ActionsEnum
from model.ActionExecturors.ExecuteAble import ExecuteAble
from model.DBOperations.DBOperations import DBOperations
from model.DBDataConvertions.DBDataConvertions import DBDataConvertions

class StorageOperator(ExecuteAble):
    def __init__(self,logger,post_container,db):
        self.__db = db
        self.__post_container = post_container
        self.__logger = logger

    def execute(self,cmd,data):

        if ActionsEnum.EDIT_POST == cmd:
            try:
                self.edit_post(*data)
                self.__logger.change_name(self.__class__.__name__)
                self.__logger.info("Post has edited")
            except Exception as ex:
                self.__logger.change_name(self.__class__.__name__)
                self.__logger.exception(ex)

        elif ActionsEnum.READ_ALL_RECORDS_FROM_DB == cmd:

            try:
                self.read_all_records_from_db()
                self.__logger.change_name(self.__class__.__name__)
                self.__logger.info("All records was read from file")
            except Exception as ex:
                self.__logger.change_name(self.__class__.__name__)
                self.__logger.exception(ex)

        elif ActionsEnum.REMOVE_POST == cmd:

            try:
                self.delete_post(data)
                self.__logger.change_name(self.__class__.__name__)
                self.__logger.info("Post has removed")
            except Exception as ex:
                self.__logger.change_name(self.__class__.__name__)
                self.__logger.exception(ex)


        elif ActionsEnum.ADD_POST == cmd:

            try:
                self.add_new_post(*data)
                self.__logger.change_name(self.__class__.__name__)
                self.__logger.info("Post has added")
            except Exception as ex:
                self.__logger.change_name(self.__class__.__name__)
                self.__logger.exception(ex)

    def delete_post(self,text):
        DBOperations.delete_record(self.__db,text)
        self.__post_container.remove_post_by_text(text)

    def edit_post(self,old_text,new_text,new_list_of_photos):
        DBOperations.delete_record(self.__db,old_text)
        DBOperations.add_new_record(self.__db,new_text,new_list_of_photos)

        self.__post_container.remove_post_by_text(old_text)
        self.__post_container.add(DBDataConvertions.convert_record_to_post(new_text,new_list_of_photos))

    def add_new_post(self,text,list_of_photos):
        DBOperations.add_new_record(self.__db,text,list_of_photos)
        self.__post_container.add(DBDataConvertions.convert_record_to_post(text, list_of_photos))

    def read_all_records_from_db(self):
            self.__post_container.clear()
            records = DBOperations.read_all_records(self.__db)
            [self.__post_container.add(DBDataConvertions.convert_record_to_post(*record))
                                                                for record  in records]


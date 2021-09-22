import pickle,os

class PhotoDBOperations:

    @staticmethod
    def update_db(db,compliences):
        file = open(db, "wb")
        pickle.dump(compliences,file,protocol=4)
        file.close()

    @staticmethod
    def check_existance(file_name):
        if not os.path.exists(file_name):
            file = open(file_name,'wb')
            pickle.dump({},file)
            file.close()



    @staticmethod
    def read_compliences(db):
        PhotoDBOperations.check_existance(db)

        file = open(db, "rb")
        compliances = pickle.load(file)
        file.close()
        return compliances
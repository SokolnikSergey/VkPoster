class DBOperations:

    @staticmethod
    def read_all_records(db):
        items = db.items()
        lst = []
        [lst.append(item) for item in items]
        return lst

    @staticmethod
    def add_new_record(db, key, value):
        db[key] = value

    @staticmethod
    def delete_record(db, key_for_del):
        if db.pop(key_for_del):
            return True
        else:
            return False

    @staticmethod
    def edit_key_of_record(db, key=None, new_key=None):
        items = db.items()
        temp = None
        for i in items:
            for z in i:
                if z == key:
                    temp = i
        if temp:
            temp_val = temp[1]
            db.pop(temp[0])
            db[new_key] = temp_val
            return True
        else:
            return False

    @staticmethod
    def edit_value_of_record(db,key,new_value):
        db[key] = new_value

    @staticmethod
    def clear_db(db):
        db.clear()

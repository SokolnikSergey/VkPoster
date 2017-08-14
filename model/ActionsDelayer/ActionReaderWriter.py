import pickle,os
class ActionReadWrite:

    @staticmethod
    def read_actions_from_file(file_name):
        if (os.path.isfile(file_name)):
            with open(file_name,"rb") as file:
                actions = pickle.load(file)
            os.remove(file_name)
            return actions
        return None

    @staticmethod
    def write_actions_to_file(file_name,actions):
        with open(file_name,'wb') as file:
            pickle.dump(actions,file)


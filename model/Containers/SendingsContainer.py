import marshal, os, hashlib
from datetime import datetime

class SendingsContainer:
    def __init__(self, current_file_timestamp, path_to_container = '../AuxElements/sendings'):
        self.__path_to_container = path_to_container
        self.__current_start_timestamp = current_file_timestamp
        self.create_file_if_absent()

    def create_file_if_absent(self):
        if not os.path.exists(self.__path_to_container):
            marshal.dump({}, open(self.__path_to_container, 'wb'))

    def append_sending_to_file(self, text, images, group_id):
        sendings_data = marshal.load(open(self.__path_to_container, 'rb'))
        key =  self.get_key(text, images)
        if key in sendings_data:
            current_start_sendings = []
            for sending in sendings_data[key]['sendings']:
                if sending['timestamp'] > self.__current_start_timestamp:
                    current_start_sendings.append(sending)
            sendings_data[key]['sendings'] = current_start_sendings
        else:
            sendings_data[key] = {
                'sendings': [],
                # 'text': text,
                # 'images': images
            }

        sendings_data[key]['sendings'].append({
            'timestamp': str(int(datetime.timestamp(datetime.now()))),
            'group_id': group_id
        })
        marshal.dump(sendings_data, open(self.__path_to_container,'wb'))


    def get_key(self, text, images):
        return hashlib.md5((text.strip() + ','.join(images)).encode("utf-8")).hexdigest()


    def get_sendings_for_post(self,text, images):
        sendings_data = marshal.load(open(self.__path_to_container, 'rb'))
        key = self.get_key(text, images)
        if key in sendings_data:
            if 'sendings' in sendings_data[key]:
                return sendings_data[key]['sendings']




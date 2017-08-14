import os,struct

class ReadWriteToken:
    """This is class for search token to authorization on the  site
    to achieve your aim in future without any questions about authorization
    (if your are entering not first time) write and read file with token """
    @staticmethod
    # This method allows to search existing token
    def search_avaliable_token(file_name):
        if os.path.exists(file_name) and os.path.getsize(file_name):
            with open(file_name,"rb") as token_file:
                size_of_file = os.path.getsize(file_name)
                bytes_info = token_file.read()
                info = struct.unpack(str(size_of_file) + "s",bytes_info)[0].decode('utf-8')
                token_file.close()
                if not len(info) :
                    return None
                return info
        else:
            return None

    @staticmethod
    #This method write token which you have recieved
    def write_token_to_file(path_to_file,token):
        bytes_token = bytes(token.encode())
        format_for_pack = str(len(token))  + 's'
        token_file = open(path_to_file,"wb")
        token_file.write( struct.pack(format_for_pack,bytes_token))
        token_file.close()

import requests,json, re

class DataUploadingVkOperations:


    @staticmethod
    def  upload_photo_to_vk(vk_api,url,bytes_of_photo):
        file = open("../AuxElements/temp_file.png","wb")
        file.write(bytes_of_photo)
        file.close()

        data = {'file1': open("../AuxElements/temp_file.png",'rb')}
        req = requests.post(url, files=data)

        json_req = json.loads(req.text)
        server, list_photos, aid, hashe = json_req['server'], json_req['photos_list'],\
                                          json_req['aid'], json_req['hash']
        save = vk_api.photos.save(server=server, album_id=aid, hash=hashe, photos_list=list_photos, v='5.83')

        mid = re.search(r'mid=(\d+)', url ) # photo_id = page id (not album id) + photo id
        photo_id = "photo" + str(mid.group(1)) + "_" + str(save[0]["id"])
        return photo_id

    @staticmethod
    def getUploadURL(vk_api, album_id):
        return vk_api.photos.getUploadServer(album_id=album_id, v='5.73')["upload_url"]

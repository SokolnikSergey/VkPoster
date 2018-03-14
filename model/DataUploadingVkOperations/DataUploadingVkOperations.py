import requests,json

class DataUploadingVkOperations:

    ALBUM_ID = 244600823

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
        save = vk_api.photos.save(server=server, album_id=aid, hash=hashe, photos_list=list_photos)
        photo_id = "photo235374879" + "_" + str(save[0]["id"])
        return photo_id
    @staticmethod
    def getUploadURL(vk_api):
        return vk_api.photos.getUploadServer(album_id=DataUploadingVkOperations.ALBUM_ID)["upload_url"]

vk_api_version = "5,73"
import json


class VkOperations:

    logger = None

    @staticmethod
    def search_groups_by_key_word(vk_api,key_word,max_amount,country_id,min_amount_users):
        try:
            list_avaliable_groups = []
            offset = 0
            while ( len(list_avaliable_groups) < max_amount):
                list_recieved_groups = VkOperations.get_group_with_offset(vk_api,key_word,100,offset,country_id)
                print(list_recieved_groups)
                if list_recieved_groups is not None:
                    if not len(list_recieved_groups):
                        break

                for group in list_recieved_groups:
                    if VkOperations.check_valid_of_group(group,min_amount_users):
                        list_avaliable_groups.append((group['id'],group['name'],group['photo_50']))
                        if(len(list_avaliable_groups) >= max_amount):
                            break
                offset += 100
            VkOperations.logger.change_name(VkOperations.__name__)
            VkOperations.logger.info("Groups have founded")
            return list_avaliable_groups
        except Exception as ex:
            VkOperations.logger.change_name(VkOperations.__name__)
            VkOperations.logger.exception(ex)




    @staticmethod
    def get_group_with_offset(vk_api,key_word,amount,offset,country_id):
        try:

            groups_list = vk_api.groups.search(q=key_word, count=amount, fields=['can_post','members_count'],offset = offset,
                                               country_id=country_id,v=vk_api_version)['items']
            VkOperations.logger.change_name(VkOperations.__name__)
            VkOperations.logger.info("Groups have got")
            return groups_list
        except Exception as ex:
            print(ex)
            VkOperations.logger.change_name(VkOperations.__name__)
            VkOperations.logger.exception(ex)

    @staticmethod
    def check_valid_of_group(group,min_amount_of_users):
        if (( group['type'] == "page" or  group['can_post']) and  not group['is_closed'] and group['members_count'] >= min_amount_of_users):
            return True
        return False

    @staticmethod
    def  send_post_to_group(vk_api,text,list_of_photos,gid):
        photos_id = ''
        for id_of_photo in list_of_photos:
            print(id_of_photo)
            photos_id += id_of_photo+","
        print(photos_id)

        try:

            vk_api.wall.post(owner_id = str(gid * -1),message = text,attachments = photos_id[:-1])
            VkOperations.logger.change_name(VkOperations.__name__)
            VkOperations.logger.info("Post has sent to group (id)->" + str(gid))
        except Exception as ex:
            VkOperations.logger.change_name(VkOperations.__name__)
            VkOperations.logger.exception(ex)
            raise ex

    @staticmethod
    def send_post_to_group_each_to_each(vk_api, text, list_of_photos, gid):
        photos_id = ''
        for id_of_photo in list_of_photos:
            photos_id += id_of_photo + ","
        try:
            vk_api.wall.post(owner_id=str(gid * -1), message=text, attachments=photos_id[:-1])
            VkOperations.logger.change_name(VkOperations.__name__)
            VkOperations.logger.info("Post has sent to group (id) e_to_e ->", str(gid))
        except Exception as ex:
            VkOperations.logger.change_name(VkOperations.__name__)
            VkOperations.logger.exception(ex)

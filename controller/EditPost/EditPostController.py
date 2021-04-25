class EditPostController:

    LIMITED_AMOUNT_OF_PHOTOS = 10

    @staticmethod
    def is_post_changed(source_text,new_text,source_photos,new_photos):
        if source_text != new_text or len(source_photos)!= len(new_photos) or  source_photos != new_photos:
            return True
        return False

    @staticmethod
    def is_allowed_to_add_photos(list_of_photos_to_add):
        if(len(list_of_photos_to_add) > EditPostController.LIMITED_AMOUNT_OF_PHOTOS):
            return False
        return True

    @staticmethod
    def is_allowed_text(text):
        if not (len(text.strip())):
            return False
        return True



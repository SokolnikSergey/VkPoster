from model.Containers.PostContainer.Post import Post


class DBDataConvertions:

    @staticmethod
    def convert_record_to_post(text,list_of_photos):
        return Post(list_of_photos,text)

    @staticmethod
    def convert_post_to_record(post):
        return post.list_of_photos,post.text


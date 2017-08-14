from PyQt5.QtGui import QImage

class PhotoConvertionOperations():

    @staticmethod
    def convert_paths_to_QImages(list_of_paths):
        list_of_images = []
        for path in list_of_paths:
            image = QImage(path)
            image.setText(path,'')
            list_of_images.append(image)
        return list_of_images

    @staticmethod
    def convert_QImages_to_paths(list_of_QImages):
        list_of_paths = []
        for image in list_of_QImages:
            path = image.textKeys()[0]
            list_of_paths.append(path)
        return list_of_paths

    @staticmethod
    def convert_byte_array_to_image(bytes_of_photo):
        image = QImage()
        image.loadFromData(bytes_of_photo,"PNG")
        return image

    @staticmethod
    def convert_image_to_byte_array(image,photo_buffer):
        image.save(photo_buffer, "PNG")
        byte_array = photo_buffer.data()
        photo_buffer.reset()
        return byte_array

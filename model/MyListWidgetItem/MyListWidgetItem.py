from PyQt5.QtWidgets import QLabel,QWidget
from PyQt5.QtGui import QPainter
from PyQt5.Qt import QRect,Qt


class MyListWidgetItem(QLabel):
    """This class   contains text and photo, which painted by paintEvent
    wheelEvent allow change images by the wheel on mouse
    """
    def __init__(self,text,photos,margin_photo,margin_text):
        super(MyListWidgetItem, self).__init__()

        self.set_data(text,photos)
        self.set_margins(margin_photo,margin_text)
        self.set_auxiliary_elements()

        self.create_painter()

    def set_data(self,text,photos):
        self.text = text
        self.images = photos

    def set_margins(self,margin_photo,margin_text):
        self.margin_photo = margin_photo
        self.margin_text = margin_text

    def set_auxiliary_elements(self):
        self.num_image_to_view = 0

    def change_number_photo(self,up=False,down=False):
        if up and self.num_image_to_view < len(self.images)-1:
            self.num_image_to_view += 1

        else:
            if down and (self.num_image_to_view > 0):
                self.num_image_to_view -= 1

        self.repaint()

    def check_position_under_image(self,x,y):
        if(x > self.size().width() - self.margin_photo - self.size().height() and (y > 0 and y < self.size().height())):
            return True

    def wheelEvent(self,eventWheel):
        position = eventWheel.pos()
        if(self.check_position_under_image(position.x() ,position.y())):
            if eventWheel.angleDelta().y() > 0:
                self.change_number_photo(up = True,down= False )
            else:
                self.change_number_photo(down=True, up=False)
        else:
            return QWidget.wheelEvent(self,eventWheel)


    def create_painter(self):
        self.painter = QPainter()

    def paintEvent(self, QPaintEvent):
        self.painter.begin(self)
        if len(self.images):
            self.draw_images(self.images[self.num_image_to_view])
        self.draw_text(self.text)
        self.painter.end()

    def draw_images(self,image):
        photo_pos_x = self.size().width() - self.margin_photo -self.size().height()
        photo_width_height = self.size().height()- self.margin_photo * 2
        self.painter.drawImage(QRect(photo_pos_x,self.margin_photo,photo_width_height,photo_width_height),image)

    def draw_text(self,text):
        space_between_photo_and_text = self.size().width() - self.margin_photo*3 - self.size().height()
        self.painter.drawText(QRect( self.margin_text,self.margin_text, space_between_photo_and_text,
                                     self.size().height()-self.margin_text), Qt.TextWordWrap,text)



from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRect, Qt
from view.EditPost.MyWheelScroller import MyWheelScroller

class MyPicturesWidget(QWidget):
    """This is custom class , which allow draw pictures at any position
     on this widget . Picture offset is give you a possibility to scroll pictures
     by cyclic shift"""

    def __init__(self,width,height,list_of_pictures,margin = 5 ,picture_offset = 0):
        super(MyPicturesWidget, self).__init__()
        self.__list_pictures = list_of_pictures
        self.setting_window(width,height)
        self.__margin = margin
        self.__painter = QPainter()
        self.__picture_offset = picture_offset
        self.first_picture_size = QRect()
        self.__my_wheel_scroller = MyWheelScroller()
        self.bind_wheel_scroll_signals()

    @property
    def picture_offset(self):
        return self.__picture_offset % len(self.__list_pictures)

    @picture_offset.setter
    def picture_offset(self,new_offset):
        if(isinstance(new_offset,int)):
            self.__picture_offset = new_offset

    @property
    def list_pictures(self):
        return self.__list_pictures

    @list_pictures.setter
    def list_pictures(self,new_list_of_pictures):
        if(isinstance(new_list_of_pictures,list)):
            self.__list_pictures = new_list_of_pictures

    @property
    def margin(self):
        return self.__margin

    @margin.setter
    def  margin(self,new_margin):
        if(isinstance(new_margin,int)):
            self.__margin = new_margin

    @property
    def painter(self):
        return self.__painter

    def bind_wheel_scroll_signals(self):
        self.__my_wheel_scroller.decrement_offset.connect(self.decrement_picture_offset)
        self.__my_wheel_scroller.increment_offset.connect(self.increment_picture_offset)

    def set_images_according_to_offset(self):
        pictures = self.__list_pictures
        ordered_pictures = []
        i = 0
        offset = self.__picture_offset
        pictures_lenght = len(pictures)

        while i < pictures_lenght:
            ordered_pictures.append(pictures[(i + offset) % pictures_lenght ] )
            i += 1

        self.__picture_offset = 0
        self.__list_pictures = ordered_pictures

    def setting_window(self, w, h):
        self.setGeometry(0, 0, w, h)

    def increment_picture_offset(self):
        self.__picture_offset += 1
        self.repaint()

    def decrement_picture_offset(self):
        if self.picture_offset:
            self.__picture_offset -= 1
        else:
            self.__picture_offset = len(self.list_pictures) - 1
        self.repaint()

    def calculate_position(self,offset):
        return offset % len(self.__list_pictures)

    def set_first_picture_size(self,x,y,w,h):
        self.first_picture_size = QRect(x,y,w,h)

    def get_first_picture_size(self):
        return self.first_picture_size

    def wheelEvent(self, eventWheel):
        if len(self.list_pictures) > 1:
            if eventWheel.angleDelta().y() > 0:
                self.__my_wheel_scroller.prepend_new_scroll_action(MyWheelScroller.UP_WHEEL_ACTION)
            else:
                self.__my_wheel_scroller.prepend_new_scroll_action(MyWheelScroller.DOWN_WHEEN_ACTION)

    def draw_pictures(self):
        x, y, counter = 0, 0, 0

        if len(self.__list_pictures):
            first_image = self.__list_pictures[self.calculate_position(self.picture_offset)]
            first_image_scaled = first_image.scaled(self.first_picture_size.size().height(), self.first_picture_size.size().width(), Qt.KeepAspectRatio)

            deltaX = (self.first_picture_size.size().width() - first_image_scaled.size().width()) / 2
            deltaY = (self.first_picture_size.size().height() - first_image_scaled.size().height()) / 2

            self.painter.drawImage(QRect(0 + deltaX, 0 + deltaY, first_image_scaled.size().width(), first_image_scaled.size().height()), first_image_scaled)


            x+= self.height() + self.margin ## add width of big picture + margin

            for i in range(1,len(self.__list_pictures)):

                pictures_count  = (len(self.__list_pictures) + 1) / 2
                if (((self.width() - self.height()) / pictures_count) >= (self.height() / 2)):
                    w_h = self.height() / 2 - self.margin
                else:
                    w_h = (self.width() - self.height() -(pictures_count * self.__margin) ) / pictures_count
                if (i % 2):
                    y = self.__margin
                else:
                    y = self.__margin + w_h + self.__margin ## add height of small pictute

                if (counter > 0 and not counter % 2) :
                    x += w_h + self.__margin ## add width of small picture + margin

                scaled_image = self.__list_pictures[self.calculate_position(i + self.__picture_offset)].scaled(w_h,w_h, Qt.KeepAspectRatio)

                deltaX = (w_h - scaled_image.size().width()) / 2
                deltaY = (w_h - scaled_image.size().height()) / 2

                self.painter.drawImage(QRect(x + deltaX, y + deltaY, scaled_image.size().width(), scaled_image.size().height()), scaled_image)

                counter +=1

    def paintEvent(self, QPaintEvent):
        self.__painter.begin(self)
        self.set_first_picture_size(0, 0, self.height() - self.__margin,self.height() - self.__margin)
        self.draw_pictures()
        self.__painter.end()

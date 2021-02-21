from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRect
import time

class MyPicturesWidget(QWidget):
    """This is custom class , which allow draw pictures at any position
     on this widget . Picture offset is give you a possibility to scroll pictures
     by cyclic shift"""

    def __init__(self,width,height,list_of_pictures,margin = 5 ,picture_offset = 0):
        super(MyPicturesWidget, self).__init__()
        self.setting_window(width,height)
        self.__list_pictures = list_of_pictures
        self.__margin = margin
        self.__painter = QPainter()
        self.__picture_offset = picture_offset
        self.first_picture_size = QRect()

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

    def setting_window(self, w, h):
        self.setGeometry(0, 0, w, h)

    def increment_picture_offset(self):
        self.__picture_offset += 1

    def decrement_picture_offset(self):
        if self.picture_offset:
            self.__picture_offset -= 1
        else:
            self.__picture_offset = len(self.list_pictures) - 1

    def calculate_position(self,offset):
        return offset % len(self.__list_pictures)

    def scroll_picture(self,up=False, down=False):
        if up and not down:
            self.increment_picture_offset()
        elif not up and down:
            self.decrement_picture_offset()

    def set_first_picture_size(self,x,y,w,h):
        self.first_picture_size = QRect(x,y,w,h)

    def get_first_picture_size(self):
        return self.first_picture_size

    def wheelEvent(self, eventWheel):
        if len(self.list_pictures) > 1:
            if eventWheel.angleDelta().y() > 0:
                self.scroll_picture(up=True, down=False)
            else:
                self.scroll_picture(down=True, up=False)
        self.repaint()
        time.sleep(0.5)

    def draw_pictures(self):
        x, y, counter = 0, 0, 0

        if len(self.__list_pictures):
            self.painter.drawImage(self.first_picture_size, self.__list_pictures[self.calculate_position(self.picture_offset)])

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
                self.painter.drawImage(QRect(x, y, w_h ,w_h),
                                       self.__list_pictures[self.calculate_position(i + self.__picture_offset)])
                counter +=1

    def paintEvent(self, QPaintEvent):
        self.__painter.begin(self)
        self.set_first_picture_size(0, 0, self.height() - self.__margin,self.height() - self.__margin)
        self.draw_pictures()
        self.__painter.end()

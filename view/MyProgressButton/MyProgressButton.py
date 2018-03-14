from PyQt5.QtWidgets import QApplication,QPushButton
from PyQt5.QtGui import QPainter,QBrush
from PyQt5.Qt import Qt

class MyProgressButton(QPushButton):
    def __init__(self,text,parent,done = 0 ,remainded = 0,fail = 0,color = Qt.green):
        super(MyProgressButton, self).__init__(parent)
        self.create_and_set_painter()
        self.__text = text
        self.__amount_done = done
        self.__amount_remainded = remainded
        self.__amount_failed = fail
        self.__progress = None
        self.__failgress = None


    @property
    def amount_done (self):
        return self.__amount_done

    @amount_done.setter
    def amount_done(self,new_amount_done):
        if(isinstance(new_amount_done,int)):
            self.__amount_done = new_amount_done
            self.determine_progress()
            self.repaint()

    @property
    def amount_remainded(self):
        return self.__amount_remainded

    @amount_remainded.setter
    def amount_remainded(self, new_amount_remainded):
        if (isinstance(new_amount_remainded, int)):
            self.__amount_remainded = new_amount_remainded
            self.determine_progress()
            self.repaint()

    @property
    def amount_failed(self):
        return self.__amount_failed

    @amount_failed.setter
    def amount_failed(self,new_amount_failed):
        if (isinstance(new_amount_failed,int)):
            self.__amount_failed = new_amount_failed
            self.determine_progress()
            self.repaint()

    def create_and_set_painter(self,color = Qt.green):
        self.__painter = QPainter()

    def paintEvent(self, QPaintEvent):
        QPushButton.paintEvent(self, QPaintEvent)
        self.__painter.begin(self)
        self.__painter.setBrush(QBrush(Qt.green))
        self.draw_progress_rect()
        self.draw_failgress_rect()
        self.draw_text()
        self.__painter.end()

    def determine_progress(self):
        try:
            self.__progress = (100 - 100 * ((self.__amount_remainded + self.__amount_failed) / (self.__amount_done + self.__amount_remainded + self.__amount_failed)))
            self.__failgress = (100 - 100 * ((self.__amount_remainded + self.__amount_done) / (self.__amount_done + self.__amount_remainded + self.__amount_failed)))
        except Exception as ex:
            print(ex)

    def draw_progress_rect(self):
        if(self.__amount_remainded or self.__amount_done):
            if self.__progress:
                self.__painter.drawRect(0,0, self.width() * self.__progress / 100 , self.height())
            else:
                if ( not self.__amount_remainded   and not  self.__amount_failed):
                    self.__painter.drawRect(0, 0,self.width(), self.height())


    def draw_failgress_rect(self):

        if(self.__amount_remainded or self.__amount_failed):
            self.__painter.setBrush(Qt.red)
            if self.__failgress:
                self.__painter.drawRect((self.width() * self.__progress / 100),0,self.width() * self.__failgress / 100, self.height())
            else:
                if ( not self.__amount_remainded   and not  self.__amount_done):
                    self.__painter.drawRect(0, 0,self.width(), self.height())

    def draw_text(self):
        text = self.__text
        if self.__progress is not None:
            if(self.__progress != 100.0):
                text += '(' + str(self.__amount_done) + "/" + str(self.__amount_remainded + self.__amount_done + self.__amount_failed) + "/" + str(self.__amount_failed) + ')'
            else:
                text += '(has done)'

        self.__painter.drawText(self.rect(),Qt.AlignCenter,text)

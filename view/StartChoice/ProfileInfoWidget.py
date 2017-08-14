from  PyQt5.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QLabel,QSizePolicy


class ProfileInfoWidget(QWidget):
    def __init__(self,parent = None,f_n = "No First Name",l_n = "No Last Name"):##first_name,last_name
        super(ProfileInfoWidget, self).__init__(parent)
        self.create_labels(f_n,l_n)
        self.create_pictures()
        self.set_layouts()
        self.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)

    @property
    def first_name_lbl(self):
        return self.__first_name_lbl

    @property
    def last_name_lbl(self):
        return self.__last_name_lbl

    @property
    def pict_lbl (self):
        return self.__pict_lable

    @pict_lbl.setter
    def pict_lbl(self,new_pict):
        self.__pict_lable = new_pict


    def create_labels(self,first_name,last_name):
        self.__first_name_lbl  = QLabel(first_name,self)
        self.__last_name_lbl = QLabel(last_name,self)

    def create_pictures(self):
        self.__pict_lable = QLabel(self)


    def set_layouts(self):

        qh_photo_data = QHBoxLayout(self)

        qv_info = QVBoxLayout(self)
        qv_info.addWidget(self.__first_name_lbl)
        qv_info.addWidget(self.__last_name_lbl)

        qh_photo_data.addWidget(self.__pict_lable)
        qh_photo_data.addLayout(qv_info)

        self.setLayout(qv_info)

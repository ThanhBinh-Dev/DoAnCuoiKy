# Form implementation generated from reading ui file 'D:\DTB\uel\HK1\tu duy lap trinh\DuongThanhBinh_K244060766_Module28\DoAnCuoiKi\Ui\ui_DatHen\DatHen.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 700))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 1211, 781))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("background-color: rgb(218, 241, 249);\n"
"border:None;\n"
"font: 16pt \"Sitka Heading\";\n"
"font-weight:700px;\n"
"color: rgb(0, 0, 0);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 240, 1081, 361))
        self.groupBox_2.setStyleSheet("background-color: rgb(250, 227, 140);\n"
"border-radius:30px;\n"
"border: None;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 0, 1081, 361))
        self.groupBox_3.setStyleSheet("background-color: rgb(250, 227, 140);\n"
"border-radius:30px;\n"
"border: None;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.groupBox_3)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 10, 1061, 341))
        self.groupBox_6.setStyleSheet("\n"
"background-color: rgb(255,255,255);\n"
"border-radius:30px;\n"
"border: None;")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.lineEdit_HovaTen = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.lineEdit_HovaTen.setGeometry(QtCore.QRect(60, 30, 431, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_HovaTen.sizePolicy().hasHeightForWidth())
        self.lineEdit_HovaTen.setSizePolicy(sizePolicy)
        self.lineEdit_HovaTen.setTabletTracking(False)
        self.lineEdit_HovaTen.setAutoFillBackground(False)
        self.lineEdit_HovaTen.setStyleSheet("QLineEdit {\n"
"    border:1px solid#00007f ;\n"
"    color: rgb(0, 0, 127);\n"
"    border-radius: 15px;        \n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"    background-color: #fbf9f8;     \n"
"    padding-left: 20px; \n"
"    padding-right: 20px;\n"
"    qproperty-wordWrap: true;        \n"
"}\n"
"\n"
"")
        self.lineEdit_HovaTen.setText("")
        self.lineEdit_HovaTen.setCursorPosition(0)
        self.lineEdit_HovaTen.setDragEnabled(False)
        self.lineEdit_HovaTen.setPlaceholderText("")
        self.lineEdit_HovaTen.setClearButtonEnabled(False)
        self.lineEdit_HovaTen.setObjectName("lineEdit_HovaTen")
        self.lineEdit_SDT = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.lineEdit_SDT.setGeometry(QtCore.QRect(580, 30, 431, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_SDT.sizePolicy().hasHeightForWidth())
        self.lineEdit_SDT.setSizePolicy(sizePolicy)
        self.lineEdit_SDT.setTabletTracking(False)
        self.lineEdit_SDT.setStyleSheet("QLineEdit {\n"
"    border:1px solid#00007f ;\n"
"    color: rgb(0, 0, 127);\n"
"    border-radius: 15px;        \n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"    background-color: #fbf9f8;     \n"
"    padding-left: 20px; \n"
"    padding-right: 20px;\n"
"    qproperty-wordWrap: true;        \n"
"}\n"
"\n"
"")
        self.lineEdit_SDT.setText("")
        self.lineEdit_SDT.setCursorPosition(0)
        self.lineEdit_SDT.setDragEnabled(False)
        self.lineEdit_SDT.setPlaceholderText("")
        self.lineEdit_SDT.setClearButtonEnabled(False)
        self.lineEdit_SDT.setObjectName("lineEdit_SDT")
        self.lineEdit_DiaChi = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.lineEdit_DiaChi.setGeometry(QtCore.QRect(60, 270, 431, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_DiaChi.sizePolicy().hasHeightForWidth())
        self.lineEdit_DiaChi.setSizePolicy(sizePolicy)
        self.lineEdit_DiaChi.setTabletTracking(False)
        self.lineEdit_DiaChi.setStyleSheet("QLineEdit {\n"
"    border:1px solid#00007f ;\n"
"    color: rgb(0, 0, 127);\n"
"    border-radius: 15px;        \n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"    background-color: #fbf9f8;     \n"
"    padding-left: 20px; \n"
"    padding-right: 20px;\n"
"    qproperty-wordWrap: true;        \n"
"}\n"
"\n"
"\n"
"")
        self.lineEdit_DiaChi.setText("")
        self.lineEdit_DiaChi.setCursorPosition(0)
        self.lineEdit_DiaChi.setDragEnabled(False)
        self.lineEdit_DiaChi.setPlaceholderText("")
        self.lineEdit_DiaChi.setClearButtonEnabled(False)
        self.lineEdit_DiaChi.setObjectName("lineEdit_DiaChi")
        self.radioButton_PhongKham = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.radioButton_PhongKham.setGeometry(QtCore.QRect(110, 190, 141, 41))
        self.radioButton_PhongKham.setStyleSheet("background-color: None;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"qproperty-wordWrap: true;\n"
"color: rgb(0, 0, 127);")
        self.radioButton_PhongKham.setObjectName("radioButton_PhongKham")
        self.radioButton_KhamTaiGia = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.radioButton_KhamTaiGia.setGeometry(QtCore.QRect(290, 190, 141, 41))
        self.radioButton_KhamTaiGia.setStyleSheet("background-color: None;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"qproperty-wordWrap: true;\n"
"color: #00007f;")
        self.radioButton_KhamTaiGia.setObjectName("radioButton_KhamTaiGia")
        self.lineEdit_ThongTinThem = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.lineEdit_ThongTinThem.setGeometry(QtCore.QRect(580, 270, 431, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ThongTinThem.sizePolicy().hasHeightForWidth())
        self.lineEdit_ThongTinThem.setSizePolicy(sizePolicy)
        self.lineEdit_ThongTinThem.setTabletTracking(False)
        self.lineEdit_ThongTinThem.setStyleSheet("QLineEdit {\n"
"    border:1px solid#00007f ;\n"
"    color: rgb(0, 0, 127);\n"
"    border-radius: 15px;        \n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"    background-color: #fbf9f8;     \n"
"    padding-left: 20px; \n"
"    padding-right: 20px;\n"
"    qproperty-wordWrap: true;        \n"
"}\n"
"")
        self.lineEdit_ThongTinThem.setText("")
        self.lineEdit_ThongTinThem.setCursorPosition(0)
        self.lineEdit_ThongTinThem.setDragEnabled(False)
        self.lineEdit_ThongTinThem.setClearButtonEnabled(False)
        self.lineEdit_ThongTinThem.setObjectName("lineEdit_ThongTinThem")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_8.setGeometry(QtCore.QRect(380, 10, 311, 311))
        self.label_8.setStyleSheet("\n"
"font: 63 26pt \"Sitka Small Semibold\";")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\DoAnCuoiKi\\Ui\\ui_DatHen\\../../Images/Images_DatHen/Dog.png"))
        self.label_8.setObjectName("label_8")
        self.comboBox_DichVuKham = QtWidgets.QComboBox(parent=self.groupBox_6)
        self.comboBox_DichVuKham.setGeometry(QtCore.QRect(580, 190, 431, 41))
        self.comboBox_DichVuKham.setStyleSheet("QComboBox {\n"
"    border-radius:15px;\n"
"background-color: #fbf9f8;\n"
"border:1px solid#00007f ;\n"
"font: 13pt \"MS Shell Dlg 2\";\n"
"padding-left: 20px; \n"
"padding-right: 20px;\n"
"qproperty-wordWrap: true;\n"
"}\n"
"QComboBox::drop-down {\n"
"    width: 20px; /* Giảm độ rộng của phần dropdown */\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"")
        self.comboBox_DichVuKham.setObjectName("comboBox_DichVuKham")
        self.comboBox_NgayKham = QtWidgets.QComboBox(parent=self.groupBox_6)
        self.comboBox_NgayKham.setGeometry(QtCore.QRect(60, 110, 431, 41))
        self.comboBox_NgayKham.setStyleSheet("QComboBox {\n"
"    border-radius:15px;\n"
"background-color: #fbf9f8;\n"
"border:1px solid#00007f ;\n"
"font: 13pt \"MS Shell Dlg 2\";\n"
"padding-left: 20px; \n"
"padding-right: 20px;\n"
"qproperty-wordWrap: true;\n"
"}\n"
"QComboBox::drop-down {\n"
"    width: 20px; /* Giảm độ rộng của phần dropdown */\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"")
        self.comboBox_NgayKham.setObjectName("comboBox_NgayKham")
        self.comboBox_GioKham = QtWidgets.QComboBox(parent=self.groupBox_6)
        self.comboBox_GioKham.setGeometry(QtCore.QRect(580, 110, 431, 41))
        self.comboBox_GioKham.setStyleSheet("QComboBox {\n"
"    border-radius:15px;\n"
"background-color: #fbf9f8;\n"
"border:1px solid#00007f ;\n"
"font: 13pt \"MS Shell Dlg 2\";\n"
"padding-left: 20px; \n"
"padding-right: 20px;\n"
"qproperty-wordWrap: true;\n"
"}\n"
"QComboBox::drop-down {\n"
"    width: 20px; /* Giảm độ rộng của phần dropdown */\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"")
        self.comboBox_GioKham.setObjectName("comboBox_GioKham")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_2.setGeometry(QtCore.QRect(910, 310, 311, 311))
        self.label_2.setStyleSheet("\n"
"background-color: rgba(255, 255, 255,100);\n"
"border-radius:0px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_9.setGeometry(QtCore.QRect(70, -10, 181, 51))
        self.label_9.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_10.setGeometry(QtCore.QRect(590, -10, 181, 51))
        self.label_10.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_11.setGeometry(QtCore.QRect(70, 70, 181, 51))
        self.label_11.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_12.setGeometry(QtCore.QRect(590, 70, 181, 51))
        self.label_12.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_13.setGeometry(QtCore.QRect(70, 150, 181, 51))
        self.label_13.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_14.setGeometry(QtCore.QRect(70, 230, 271, 51))
        self.label_14.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_15.setGeometry(QtCore.QRect(590, 150, 181, 51))
        self.label_15.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_16.setGeometry(QtCore.QRect(590, 230, 181, 51))
        self.label_16.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_17.setGeometry(QtCore.QRect(60, 10, 16, 16))
        self.label_17.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;\n"
"color: rgb(255, 0, 4);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_18.setGeometry(QtCore.QRect(60, 170, 16, 16))
        self.label_18.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;\n"
"color: rgb(255, 0, 4);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_19.setGeometry(QtCore.QRect(60, 90, 16, 16))
        self.label_19.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;\n"
"color: rgb(255, 0, 4);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_20.setGeometry(QtCore.QRect(580, 10, 16, 16))
        self.label_20.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;\n"
"color: rgb(255, 0, 4);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_21.setGeometry(QtCore.QRect(580, 170, 16, 16))
        self.label_21.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;\n"
"color: rgb(255, 0, 4);")
        self.label_21.setObjectName("label_21")
        self.label_23 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_23.setGeometry(QtCore.QRect(580, 90, 16, 16))
        self.label_23.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;\n"
"color: rgb(255, 0, 4);")
        self.label_23.setObjectName("label_23")
        self.label_22 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_22.setGeometry(QtCore.QRect(460, 120, 20, 20))
        self.label_22.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;")
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\DoAnCuoiKi\\Ui\\ui_DatHen\\../../Images/Images_DatHen/down.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.label_24 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_24.setGeometry(QtCore.QRect(980, 200, 20, 20))
        self.label_24.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;")
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\DoAnCuoiKi\\Ui\\ui_DatHen\\../../Images/Images_DatHen/down.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_25.setGeometry(QtCore.QRect(980, 120, 20, 20))
        self.label_25.setStyleSheet("qproperty-wordWrap: true;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color:None;")
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\DoAnCuoiKi\\Ui\\ui_DatHen\\../../Images/Images_DatHen/down.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.label_8.raise_()
        self.lineEdit_HovaTen.raise_()
        self.lineEdit_SDT.raise_()
        self.lineEdit_DiaChi.raise_()
        self.radioButton_PhongKham.raise_()
        self.radioButton_KhamTaiGia.raise_()
        self.lineEdit_ThongTinThem.raise_()
        self.comboBox_DichVuKham.raise_()
        self.comboBox_NgayKham.raise_()
        self.comboBox_GioKham.raise_()
        self.label_2.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_23.raise_()
        self.label_22.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.pushButton_DatHen = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_DatHen.setGeometry(QtCore.QRect(440, 600, 191, 51))
        self.pushButton_DatHen.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_DatHen.setStyleSheet("QPushButton {background-color: rgb(250, 227, 140);\n"
"font:  20pt \"Sitka Display Semibold\";\n"
"border-radius:20px;\n"
"border: None;\n"
"color: rgb(214, 47, 55);\n"
"font-weight:bold;\n"
"padding:5px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 193, 92);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\DoAnCuoiKi\\Ui\\ui_DatHen\\../../Images/Images_DatHen/HEALTH.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_DatHen.setIcon(icon)
        self.pushButton_DatHen.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_DatHen.setObjectName("pushButton_DatHen")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 180, 201, 41))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(3, 175, 88);\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    border-radius:20px;\n"
"    border: None;\n"
"    color: #ffffff;\n"
"    font-weight:bold;\n"
"    padding2px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(19, 186, 30);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\DoAnCuoiKi\\Ui\\ui_DatHen\\../../Images/Images_DatHen/calling.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(60, 20, 171, 161))
        self.label.setStyleSheet("border-radius:100%;\n"
"background-color:None;\n"
"setMask:(mask);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\DoAnCuoiKi\\Ui\\ui_DatHen\\../../Images/Images_DatHen/logo.png"))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(250, 10, 851, 101))
        self.label_3.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 36pt \"MS Reference Sans Serif\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(440, -40, 411, 141))
        self.label_4.setStyleSheet("background-color: None;\n"
"border-bottom:3px solid  rgb(94, 99, 101) ;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(290, 110, 731, 91))
        self.label_5.setStyleSheet("font: 75 italic 16pt \"Sitka Display\";\n"
"qproperty-wordWrap: true;\n"
"background-color:None;")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(0, 660, 1091, 31))
        self.label_6.setStyleSheet("font: 75 italic 16pt \"Sitka Display\";\n"
"qproperty-wordWrap: true;\n"
"color: rgb(85, 85, 85);\n"
"background-color: None;\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(950, 110, 121, 111))
        self.label_7.setStyleSheet("\n"
"font: 63 26pt \"Sitka Small Semibold\";")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\DoAnCuoiKi\\Ui\\ui_DatHen\\../../Images/Images_DatHen/Dogs.png"))
        self.label_7.setObjectName("label_7")
        self.pushButton_caution = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_caution.setGeometry(QtCore.QRect(10, 10, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_caution.sizePolicy().hasHeightForWidth())
        self.pushButton_caution.setSizePolicy(sizePolicy)
        self.pushButton_caution.setStyleSheet("QPushButton {background:transparent;\n"
"border:None}\n"
"QPushButton:pressed{background-color: rgb(193, 193, 193);}")
        self.pushButton_caution.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\DoAnCuoiKi\\Ui\\ui_DatHen\\../../Images/Images_DatHen/back.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_caution.setIcon(icon2)
        self.pushButton_caution.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_caution.setObjectName("pushButton_caution")
        self.label_7.raise_()
        self.groupBox_2.raise_()
        self.pushButton_DatHen.raise_()
        self.pushButton_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.pushButton_caution.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Đặt Lịch Hẹn"))
        self.radioButton_PhongKham.setText(_translate("MainWindow", "Phòng Khám"))
        self.radioButton_KhamTaiGia.setText(_translate("MainWindow", "Khám Tại Gia"))
        self.lineEdit_ThongTinThem.setPlaceholderText(_translate("MainWindow", "Tình Trạng Thú Cưng,..."))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Họ và tên: </span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Số điện thoại: </span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Ngày khám: </span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Giờ khám: </span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Nơi khám: </span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Địa chỉ (nếu khám tại gia): </span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Dịch vụ khám: </span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Thông tin thêm: </span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">*</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">*</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">*</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">*</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">*</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">*</span></p></body></html>"))
        self.pushButton_DatHen.setText(_translate("MainWindow", "Đặt Hẹn"))
        self.pushButton_2.setText(_translate("MainWindow", "0968686868"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">DR.PET’S HOUSE - ĐẶT HẸN TRỰC TUYẾN</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Chào mừng đến với Phòng khám thú y Dr . Pet’s House! Đặt hẹn trực tuyến để nhận dịch vụ chăm sóc thú cưng toàn diện, từ kiểm tra sức khỏe đến phẫu thuật. Hãy đặt hẹn ngay hôm nay! 🐾"))
        self.label_6.setText(_translate("MainWindow", "Cảm ơn quý khách đã tin tưởng và sử dụng dịch vụ đặt lịch hẹn của Dr. Pet’s House"))

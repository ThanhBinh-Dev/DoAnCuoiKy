# Form implementation generated from reading ui file 'D:\DTB\uel\HK1\tu duy lap trinh\DuongThanhBinh_K244060766_Module28\DoAnCuoiKi\Ui\ui_QuanLyKhachHang\QLKH.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 703)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1100, 700))
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\DoAnCuoiKi\\Ui\\ui_QuanLyKhachHang\\../../Images/Images_QLKH/nen_qlkh.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEditTimKiem = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditTimKiem.setGeometry(QtCore.QRect(10, 110, 241, 31))
        self.lineEditTimKiem.setTabletTracking(False)
        self.lineEditTimKiem.setAutoFillBackground(False)
        self.lineEditTimKiem.setStyleSheet("QLineEdit {\n"
"    border:1px solid#00007f ;\n"
"    color: rgb(0, 0, 127);\n"
"    border-radius: 15px;        \n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"    background-color: #fbf9f8;     \n"
"    padding-left: 35px; \n"
"    padding-right: 5px;        \n"
"}")
        self.lineEditTimKiem.setDragEnabled(False)
        self.lineEditTimKiem.setReadOnly(False)
        self.lineEditTimKiem.setClearButtonEnabled(True)
        self.lineEditTimKiem.setObjectName("lineEditTimKiem")
        self.pushButtonSearch = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSearch.setGeometry(QtCore.QRect(10, 110, 31, 31))
        self.pushButtonSearch.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;                     \n"
"    padding: 5px 10px;        \n"
"    text-decoration: underline;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(208, 209, 208);\n"
"}\n"
"")
        self.pushButtonSearch.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\DoAnCuoiKi\\Ui\\ui_QuanLyKhachHang\\../../Images/Images_QLKH/ic_search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSearch.setIcon(icon)
        self.pushButtonSearch.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.pushButtonAdd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(340, 110, 31, 31))
        self.pushButtonAdd.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;                     \n"
"    padding: 5px 10px;        \n"
"    text-decoration: underline;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(195, 195, 195);\n"
"}\n"
"")
        self.pushButtonAdd.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\DoAnCuoiKi\\Ui\\ui_QuanLyKhachHang\\../../Images/Images_QLKH/ic_add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonAdd.setIcon(icon1)
        self.pushButtonAdd.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.labelHoTen = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelHoTen.setGeometry(QtCore.QRect(580, 30, 331, 51))
        self.labelHoTen.setStyleSheet("font: 18pt \"Courier New\";\n"
"color: rgb(0, 0, 0);")
        self.labelHoTen.setObjectName("labelHoTen")
        self.labelSDT = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelSDT.setGeometry(QtCore.QRect(580, 70, 281, 21))
        self.labelSDT.setStyleSheet("font: 16pt \"Courier New\";\n"
"color: rgb(138, 138, 138);")
        self.labelSDT.setObjectName("labelSDT")
        self.lineEditNgayKham = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditNgayKham.setGeometry(QtCore.QRect(470, 230, 261, 31))
        self.lineEditNgayKham.setStyleSheet("QLineEdit {\n"
"    border:1px solid#00007f ;\n"
"    color: rgb(0, 0, 127);\n"
"    border-radius: 15px;        \n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"    background-color: #fbf9f8;\n"
"    padding-left: 10px; \n"
"    padding-right: 10px;\n"
"}")
        self.lineEditNgayKham.setReadOnly(True)
        self.lineEditNgayKham.setPlaceholderText("")
        self.lineEditNgayKham.setObjectName("lineEditNgayKham")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(560, 150, 391, 51))
        self.label_5.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 8pt \"Candara\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(480, 210, 91, 21))
        self.label_6.setStyleSheet("color: rgb(115, 115, 115);")
        self.label_6.setObjectName("label_6")
        self.lineEditGioKham = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditGioKham.setGeometry(QtCore.QRect(750, 230, 301, 31))
        self.lineEditGioKham.setStyleSheet("QLineEdit {\n"
"    border:1px solid#00007f ;\n"
"    color: rgb(0, 0, 127);\n"
"    border-radius: 15px;        \n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"    background-color: #fbf9f8;\n"
"    padding-left: 10px; \n"
"    padding-right: 10px;\n"
"}")
        self.lineEditGioKham.setReadOnly(True)
        self.lineEditGioKham.setPlaceholderText("")
        self.lineEditGioKham.setObjectName("lineEditGioKham")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(760, 210, 91, 21))
        self.label_7.setStyleSheet("color: rgb(115, 115, 115);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(480, 280, 101, 21))
        self.label_8.setStyleSheet("color: rgb(115, 115, 115);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(760, 280, 101, 21))
        self.label_9.setStyleSheet("color: rgb(115, 115, 115);")
        self.label_9.setObjectName("label_9")
        self.lineEditThongTinThem = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditThongTinThem.setGeometry(QtCore.QRect(470, 370, 581, 61))
        self.lineEditThongTinThem.setStyleSheet("QLineEdit {\n"
"    border:1px solid#00007f ;\n"
"    color: rgb(0, 0, 127);\n"
"    border-radius: 15px;        \n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"    background-color: #fbf9f8;\n"
"    padding-left: 10px; \n"
"    padding-right: 10px;\n"
"}")
        self.lineEditThongTinThem.setReadOnly(False)
        self.lineEditThongTinThem.setPlaceholderText("")
        self.lineEditThongTinThem.setObjectName("lineEditThongTinThem")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(480, 350, 121, 21))
        self.label_10.setStyleSheet("color: rgb(115, 115, 115);")
        self.label_10.setObjectName("label_10")
        self.lineEditBacSi = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditBacSi.setGeometry(QtCore.QRect(750, 540, 301, 31))
        self.lineEditBacSi.setStyleSheet("QLineEdit {\n"
"    border:1px solid#00007f ;\n"
"    color: rgb(0, 0, 127);\n"
"    border-radius: 15px;        \n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"    background-color: #fbf9f8;\n"
"    padding-left: 10px; \n"
"    padding-right: 10px; \n"
"}")
        self.lineEditBacSi.setReadOnly(True)
        self.lineEditBacSi.setPlaceholderText("")
        self.lineEditBacSi.setObjectName("lineEditBacSi")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(480, 520, 101, 21))
        self.label_11.setStyleSheet("color: rgb(115, 115, 115);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(760, 450, 101, 21))
        self.label_12.setStyleSheet("color: rgb(115, 115, 115);")
        self.label_12.setObjectName("label_12")
        self.lineEditDiaChi = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditDiaChi.setGeometry(QtCore.QRect(750, 470, 301, 31))
        self.lineEditDiaChi.setStyleSheet("QLineEdit {\n"
"    border:1px solid#00007f ;\n"
"    color: rgb(0, 0, 127);\n"
"    border-radius: 15px;        \n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"    background-color: #fbf9f8;\n"
"    padding-left: 10px; \n"
"    padding-right: 10px;\n"
"}")
        self.lineEditDiaChi.setReadOnly(False)
        self.lineEditDiaChi.setPlaceholderText("")
        self.lineEditDiaChi.setObjectName("lineEditDiaChi")
        self.lineEditSDTBacSi = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditSDTBacSi.setGeometry(QtCore.QRect(470, 540, 261, 31))
        self.lineEditSDTBacSi.setStyleSheet("QLineEdit {\n"
"    border:1px solid#00007f ;\n"
"    color: rgb(0, 0, 127);\n"
"    border-radius: 15px;        \n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"    background-color: #fbf9f8;\n"
"    padding-left: 10px; \n"
"    padding-right: 10px; \n"
"}")
        self.lineEditSDTBacSi.setReadOnly(True)
        self.lineEditSDTBacSi.setPlaceholderText("")
        self.lineEditSDTBacSi.setObjectName("lineEditSDTBacSi")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(760, 520, 141, 21))
        self.label_13.setStyleSheet("color: rgb(115, 115, 115);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(480, 450, 141, 21))
        self.label_14.setStyleSheet("color: rgb(115, 115, 115);")
        self.label_14.setObjectName("label_14")
        self.lineEditTinhTrang = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditTinhTrang.setGeometry(QtCore.QRect(470, 470, 261, 31))
        self.lineEditTinhTrang.setStyleSheet("QLineEdit {\n"
"    border:1px solid#00007f ;\n"
"    color: rgb(0, 0, 127);\n"
"    border-radius: 15px;        \n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"    background-color: #fbf9f8;\n"
"    padding-left: 10px; \n"
"    padding-right: 10px; \n"
"}")
        self.lineEditTinhTrang.setReadOnly(True)
        self.lineEditTinhTrang.setPlaceholderText("")
        self.lineEditTinhTrang.setObjectName("lineEditTinhTrang")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(460, 20, 101, 91))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\DoAnCuoiKi\\Ui\\ui_QuanLyKhachHang\\../../Images/Images_QLKH/ic_user-square.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.pushButtonDangXuat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonDangXuat.setGeometry(QtCore.QRect(940, 80, 121, 41))
        self.pushButtonDangXuat.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(255, 98, 93);\n"
"    border-radius: 15px;       \n"
"    color: black;               \n"
"    padding: 5px 10px;        \n"
"    font: 14pt \"Sitka Display\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(255, 61, 61)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgb(255, 61, 61)\n"
"}")
        self.pushButtonDangXuat.setObjectName("pushButtonDangXuat")
        self.pushButtonHuongDan = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonHuongDan.setGeometry(QtCore.QRect(940, 30, 121, 41))
        self.pushButtonHuongDan.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color:rgb(199, 224, 235);\n"
"    border-radius: 15px;       \n"
"    color: black;               \n"
"    padding: 5px 10px;        \n"
"    font: 14pt \"Sitka Display\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(119, 174, 232);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(119, 174, 232);\n"
"}\n"
"")
        self.pushButtonHuongDan.setObjectName("pushButtonHuongDan")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 160, 411, 511))
        self.scrollArea.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Display\"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 409, 509))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButtonSave = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSave.setGeometry(QtCore.QRect(380, 110, 31, 31))
        self.pushButtonSave.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;                     \n"
"    padding: 5px 10px;        \n"
"    text-decoration: underline;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(195, 195, 195);\n"
"}\n"
"")
        self.pushButtonSave.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\DoAnCuoiKi\\Ui\\ui_QuanLyKhachHang\\../../Images/Images_QLKH/ic_save.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSave.setIcon(icon2)
        self.pushButtonSave.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonPrint = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonPrint.setGeometry(QtCore.QRect(300, 110, 31, 31))
        self.pushButtonPrint.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;                     \n"
"    padding: 5px 10px;        \n"
"    text-decoration: underline;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(195, 195, 195);\n"
"}\n"
"")
        self.pushButtonPrint.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\DoAnCuoiKi\\Ui\\ui_QuanLyKhachHang\\../../Images/Images_QLKH/ic_payment.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonPrint.setIcon(icon3)
        self.pushButtonPrint.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonPrint.setObjectName("pushButtonPrint")
        self.comboBox_DichVu = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_DichVu.setGeometry(QtCore.QRect(470, 300, 261, 31))
        self.comboBox_DichVu.setStyleSheet("QComboBox {\n"
"    border:1px solid#00007f ;\n"
"    color: rgb(0, 0, 127);\n"
"    border-radius: 15px;        \n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"    background-color: #fbf9f8;     \n"
"    padding-left: 10px; \n"
"    padding-right: 10px; \n"
"}")
        self.comboBox_DichVu.setObjectName("comboBox_DichVu")
        self.comboBox_NoiKham = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_NoiKham.setGeometry(QtCore.QRect(750, 300, 301, 31))
        self.comboBox_NoiKham.setStyleSheet("QComboBox {\n"
"    border:1px solid#00007f ;\n"
"    color: rgb(0, 0, 127);\n"
"    border-radius: 15px;        \n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"    background-color: #fbf9f8;     \n"
"    padding-left: 10px; \n"
"    padding-right: 10px; \n"
"}")
        self.comboBox_NoiKham.setObjectName("comboBox_NoiKham")
        self.comboBox_NoiKham.addItem("")
        self.comboBox_NoiKham.setItemText(0, "")
        self.comboBox_NoiKham.addItem("")
        self.comboBox_NoiKham.addItem("")
        self.pushButtonreload = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonreload.setGeometry(QtCore.QRect(260, 110, 31, 31))
        self.pushButtonreload.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;                     \n"
"    padding: 5px 10px;        \n"
"    text-decoration: underline;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(195, 195, 195);\n"
"}\n"
"")
        self.pushButtonreload.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\DoAnCuoiKi\\Ui\\ui_QuanLyKhachHang\\../../Images/Images_QLKH/ic_reload.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonreload.setIcon(icon4)
        self.pushButtonreload.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonreload.setObjectName("pushButtonreload")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEditTimKiem.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lineEditTimKiem.setPlaceholderText(_translate("MainWindow", "  Tìm kiếm"))
        self.labelHoTen.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">NGUYỄN THỊ KIỀU TIÊN</span></p></body></html>"))
        self.labelSDT.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">0935010927</span></p></body></html>"))
        self.lineEditNgayKham.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">THÔNG TIN CHI TIẾT</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Ngày khám: </span></p></body></html>"))
        self.lineEditGioKham.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Giờ khám: </span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Dịch vụ khám:</span></p><p><span style=\" font-size:10pt; font-weight:600;\"/></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nơi khám:</span></p><p><br/></p></body></html>"))
        self.lineEditThongTinThem.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Thông tin thêm:</span></p><p><br/></p></body></html>"))
        self.lineEditBacSi.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Bác sĩ khám:</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Địa Chỉ:</span></p></body></html>"))
        self.lineEditDiaChi.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lineEditSDTBacSi.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Số điện thoại bác sĩ: </span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tình trạng:</span></p></body></html>"))
        self.lineEditTinhTrang.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButtonDangXuat.setText(_translate("MainWindow", "Đăng xuất"))
        self.pushButtonHuongDan.setText(_translate("MainWindow", "Hướng dẫn"))
        self.comboBox_NoiKham.setItemText(1, _translate("MainWindow", "Phòng Khám"))
        self.comboBox_NoiKham.setItemText(2, _translate("MainWindow", "Khám Tại Gia"))

# Form implementation generated from reading ui file 'C:\Users\thain\PycharmProjects\K24406H\DoAnCuoiKi\Ui\ui_PhieuXacNhan\PhieuXacNhan.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\thain\\PycharmProjects\\K24406H\\DoAnCuoiKi\\Ui\\ui_PhieuXacNhan\\../../../../../.designer/backup/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1100, 700))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\thain\\PycharmProjects\\K24406H\\DoAnCuoiKi\\Ui\\ui_PhieuXacNhan\\../../Images/Images_PhieuXacNhan/gxn.png"))
        self.label.setObjectName("label")
        self.label_26 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(470, 640, 401, 51))
        self.label_26.setStyleSheet("font: 12pt \"Sitka Display\";\n"
"color: rgb(255, 0, 0);")
        self.label_26.setObjectName("label_26")
        self.pushButtonThanhToan = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonThanhToan.setGeometry(QtCore.QRect(890, 540, 201, 61))
        self.pushButtonThanhToan.setStyleSheet("QPushButton {\n"
"    background-color: #fae38c;\n"
"    border-radius: 15px;\n"
"    color: black;\n"
"    padding: 5px 10px;\n"
"    font: 14pt \"Sitka Display\";\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #eeba4a;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  #eeba4a;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\thain\\PycharmProjects\\K24406H\\DoAnCuoiKi\\Ui\\ui_PhieuXacNhan\\../../Images/Images_PhieuXacNhan/thanhtoan.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonThanhToan.setIcon(icon1)
        self.pushButtonThanhToan.setIconSize(QtCore.QSize(50, 50))
        self.pushButtonThanhToan.setObjectName("pushButtonThanhToan")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(460, 500, 421, 131))
        self.groupBox.setStyleSheet("background-color: rgb(170, 255, 255,180);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px solid black;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(40, 80, 91, 41))
        self.label_15.setStyleSheet("font: 75 12pt \"Sitka Display\";\n"
"color: rgb(0, 0, 0);\n"
"border: 0px solid black;")
        self.label_15.setObjectName("label_15")
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(30, 50, 131, 31))
        self.label_14.setStyleSheet("font: 75 12pt \"Sitka Display\";\n"
"color: rgb(0, 0, 0);\n"
"border: 0px solid black;")
        self.label_14.setObjectName("label_14")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(130, 10, 181, 31))
        self.label_13.setStyleSheet("font: 75 12pt \"Sitka Display\";\n"
"color: rgb(255, 0, 0);\n"
"\n"
"border: 0px solid black;")
        self.label_13.setObjectName("label_13")
        self.lineEditTenDangNhap = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditTenDangNhap.setGeometry(QtCore.QRect(160, 60, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Sitka Display")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEditTenDangNhap.setFont(font)
        self.lineEditTenDangNhap.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Sitka Display\";\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditTenDangNhap.setText("")
        self.lineEditTenDangNhap.setReadOnly(True)
        self.lineEditTenDangNhap.setObjectName("lineEditTenDangNhap")
        self.lineEditMatKhau = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditMatKhau.setGeometry(QtCore.QRect(160, 90, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Sitka Display")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEditMatKhau.setFont(font)
        self.lineEditMatKhau.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Sitka Display\";\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditMatKhau.setText("")
        self.lineEditMatKhau.setReadOnly(True)
        self.lineEditMatKhau.setObjectName("lineEditMatKhau")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(450, 30, 651, 491))
        self.groupBox_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Sitka Display\";\n"
"border-radius: 10px;\n"
"border: 0px solid black;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEditSoDienThoai = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditSoDienThoai.setGeometry(QtCore.QRect(210, 150, 421, 41))
        self.lineEditSoDienThoai.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Sitka Display\";\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditSoDienThoai.setReadOnly(True)
        self.lineEditSoDienThoai.setObjectName("lineEditSoDienThoai")
        self.lineEditDichVuKham = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditDichVuKham.setGeometry(QtCore.QRect(210, 330, 421, 41))
        self.lineEditDichVuKham.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Sitka Display\";\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditDichVuKham.setReadOnly(True)
        self.lineEditDichVuKham.setObjectName("lineEditDichVuKham")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(20, 390, 181, 41))
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Sitka Display\";")
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 161, 41))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Sitka Display\";")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 330, 171, 41))
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Sitka Display\";")
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 171, 41))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Sitka Display\";")
        self.label_3.setObjectName("label_3")
        self.radioButtonKhamTaiGia = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButtonKhamTaiGia.setGeometry(QtCore.QRect(210, 390, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka Display")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.radioButtonKhamTaiGia.setFont(font)
        self.radioButtonKhamTaiGia.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Sitka Display\";")
        self.radioButtonKhamTaiGia.setCheckable(True)
        self.radioButtonKhamTaiGia.setChecked(False)
        self.radioButtonKhamTaiGia.setObjectName("radioButtonKhamTaiGia")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(430, 270, 61, 41))
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Sitka Display\";")
        self.label_6.setObjectName("label_6")
        self.lineEditDiachi = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditDiachi.setGeometry(QtCore.QRect(210, 210, 421, 41))
        self.lineEditDiachi.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Sitka Display\";\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditDiachi.setReadOnly(True)
        self.lineEditDiachi.setObjectName("lineEditDiachi")
        self.lineEditHovaTen = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditHovaTen.setGeometry(QtCore.QRect(210, 90, 421, 41))
        self.lineEditHovaTen.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Sitka Display\";\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditHovaTen.setReadOnly(True)
        self.lineEditHovaTen.setObjectName("lineEditHovaTen")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 161, 41))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Sitka Display\";")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 161, 41))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Sitka Display\";")
        self.label_2.setObjectName("label_2")
        self.radioButtonPhongKham = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButtonPhongKham.setGeometry(QtCore.QRect(430, 390, 181, 41))
        self.radioButtonPhongKham.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Sitka Display\";")
        self.radioButtonPhongKham.setCheckable(True)
        self.radioButtonPhongKham.setChecked(False)
        self.radioButtonPhongKham.setObjectName("radioButtonPhongKham")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(0, -30, 651, 101))
        self.label_10.setObjectName("label_10")
        self.lineEditNgayKham = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditNgayKham.setGeometry(QtCore.QRect(210, 270, 201, 41))
        self.lineEditNgayKham.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Sitka Display\";\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditNgayKham.setReadOnly(True)
        self.lineEditNgayKham.setObjectName("lineEditNgayKham")
        self.lineEditGio = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditGio.setGeometry(QtCore.QRect(480, 270, 151, 41))
        self.lineEditGio.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Sitka Display\";\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditGio.setReadOnly(True)
        self.lineEditGio.setObjectName("lineEditGio")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 180, 441, 171))
        self.groupBox_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Sitka Display\";\n"
"border-radius: 10px;\n"
"border: 0px solid black;\n"
"")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(0, 10, 441, 71))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(20, 90, 401, 81))
        self.label_12.setObjectName("label_12")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 360, 401, 331))
        self.groupBox_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Sitka Display\";\n"
"border-radius: 10px;\n"
"border: 0px solid black;\n"
"")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_18 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(10, 0, 141, 41))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(10, 20, 301, 51))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(10, 40, 111, 61))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_21.setGeometry(QtCore.QRect(140, 140, 171, 41))
        self.label_21.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_22.setGeometry(QtCore.QRect(60, 90, 311, 31))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(30, 190, 361, 41))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_24.setGeometry(QtCore.QRect(30, 260, 171, 41))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_25.setGeometry(QtCore.QRect(30, 230, 361, 31))
        self.label_25.setObjectName("label_25")
        self.label_27 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_27.setGeometry(QtCore.QRect(30, 300, 171, 31))
        self.label_27.setObjectName("label_27")
        self.pushButton_caution = QtWidgets.QPushButton(parent=self.centralwidget)
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
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\thain\\PycharmProjects\\K24406H\\DoAnCuoiKi\\Ui\\ui_PhieuXacNhan\\../../Images/Images_DangNhap/ic_back .png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_caution.setIcon(icon2)
        self.pushButton_caution.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_caution.setObjectName("pushButton_caution")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditHovaTen, self.lineEditSoDienThoai)
        MainWindow.setTabOrder(self.lineEditSoDienThoai, self.lineEditDiachi)
        MainWindow.setTabOrder(self.lineEditDiachi, self.lineEditNgayKham)
        MainWindow.setTabOrder(self.lineEditNgayKham, self.lineEditGio)
        MainWindow.setTabOrder(self.lineEditGio, self.lineEditDichVuKham)
        MainWindow.setTabOrder(self.lineEditDichVuKham, self.radioButtonKhamTaiGia)
        MainWindow.setTabOrder(self.radioButtonKhamTaiGia, self.radioButtonPhongKham)
        MainWindow.setTabOrder(self.radioButtonPhongKham, self.pushButtonThanhToan)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_26.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sitka Display\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:696; font-style:italic; color:#ff0000;\">*Quý khách vui lòng kiểm tra kĩ lưỡng các thông tin </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:696; font-style:italic; color:#ff0000;\">cần nhập và sử dụng tài khoản được cung cấp để quản lý lịch hẹn.</span></p></body></html>"))
        self.pushButtonThanhToan.setText(_translate("MainWindow", "Thanh Toán"))
        self.label_15.setText(_translate("MainWindow", "Mật khẩu:"))
        self.label_14.setText(_translate("MainWindow", "Tên đăng nhập: "))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Tài khoản đăng nhập</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Nơi Khám:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Ngày Khám:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Dịch Vụ Khám:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Số Điện Thoại:</span></p></body></html>"))
        self.radioButtonKhamTaiGia.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Khám Tại Gia</span></p></body></html>"))
        self.radioButtonKhamTaiGia.setText(_translate("MainWindow", "Khám Tại Gia"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Giờ:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Địa chỉ</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Họ &amp; Tên:</span></p></body></html>"))
        self.radioButtonPhongKham.setText(_translate("MainWindow", "Phòng Khám"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Giấy Xác Nhận</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Phòng khám thú y uy tín, chuyên cung cấp các dịch vụ khám, </span></p><p align=\"center\"><span style=\" font-size:12pt;\">chữa bệnh, chăm sóc sức khỏe và thẩm mỹ cho thú cưng. </span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:696; color:#d62f37;\">“Cam kết mang đến dịch vụ chăm sóc tận tâm, </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:696; color:#d62f37;\">chuyên nghiệp”</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:696; color:#000000;\">Thời gian làm việc:</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:696; color:#000000;\">Mở cửa: 8:00 - 21:00 (Thứ 2 - Chủ Nhật)</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:696; color:#000000;\">Cấp cứu 24/7</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">0968686868</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Mọi thắc mắc xin vui lòng liên hệ Hotline</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p>Số 86, khu phố 6, phường Linh Xuân, TP. Thủ Đức</p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p>www.drpethouse.com</p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p>0968686868 (Hỗ trợ 24/7) </p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p>drpethouse@gmail.com</p></body></html>"))

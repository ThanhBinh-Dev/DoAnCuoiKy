# Form implementation generated from reading ui file 'C:\Users\Kieu Tien\DoAnCuoiKy\DoAnCuoiKi\Ui\ui_DangNhap\login.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1100, 700))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\Kieu Tien\\DoAnCuoiKy\\DoAnCuoiKi\\Ui\\ui_DangNhap\\../../Images/Images_DangNhap/nen_dang_nhap.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEditTenDangNhap = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditTenDangNhap.setGeometry(QtCore.QRect(650, 210, 351, 51))
        self.lineEditTenDangNhap.setStyleSheet("QLineEdit {\n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px;  \n"
"    border-radius: 25px;    \n"
"    font: 13pt \"Arial\";\n"
"    background-color: rgb(232, 231, 231);\n"
"    padding: 5px;\n"
"     padding-left: 60px;\n"
"    padding-right: 60px;            \n"
"}")
        self.lineEditTenDangNhap.setObjectName("lineEditTenDangNhap")
        self.lineEditMatKhau = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditMatKhau.setGeometry(QtCore.QRect(650, 280, 351, 51))
        self.lineEditMatKhau.setStyleSheet("QLineEdit {\n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px;  \n"
"    border-radius: 25px;    \n"
"    font: 13pt \"Arial\";\n"
"    background-color: rgb(232, 231, 231);\n"
"    padding: 5px;\n"
"     padding-left: 60px;\n"
"    padding-right: 60px;            \n"
"}")
        self.lineEditMatKhau.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditMatKhau.setObjectName("lineEditMatKhau")
        self.pushButtonLogin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonLogin.setGeometry(QtCore.QRect(720, 350, 211, 41))
        self.pushButtonLogin.setStyleSheet("QPushButton {\n"
"    background-color: #fae38c; \n"
"    border-radius: 15px;       \n"
"    color: black;               \n"
"    padding: 5px 10px;        \n"
"    font: 16pt \"Sitka Display\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #eeba4a\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #fffaba; \n"
"}\n"
"")
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.pushButtonQuenMatKhau = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonQuenMatKhau.setGeometry(QtCore.QRect(740, 400, 171, 31))
        self.pushButtonQuenMatKhau.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;       \n"
"    color: blue;               \n"
"    padding: 5px 10px;        \n"
"    font: 12pt \"Sitka Display\";\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#f9ffff\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #eaf8fb; \n"
"}")
        self.pushButtonQuenMatKhau.setObjectName("pushButtonQuenMatKhau")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, -30, 451, 341))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 14pt \"Microsoft YaHei\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 220, 491, 161))
        self.label_3.setStyleSheet("font: 14pt \"Microsoft YaHei\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 350, 191, 121))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:\\Users\\Kieu Tien\\DoAnCuoiKy\\DoAnCuoiKi\\Ui\\ui_DangNhap\\../../Images/Images_DangNhap/logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 31, 31))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:\\Users\\Kieu Tien\\DoAnCuoiKy\\DoAnCuoiKi\\Ui\\ui_DangNhap\\../../Images/Images_DangNhap/ic_point.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 31, 31))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:\\Users\\Kieu Tien\\DoAnCuoiKy\\DoAnCuoiKi\\Ui\\ui_DangNhap\\../../Images/Images_DangNhap/ic_point.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(650, 210, 51, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("C:\\Users\\Kieu Tien\\DoAnCuoiKy\\DoAnCuoiKi\\Ui\\ui_DangNhap\\../../Images/Images_DangNhap/ic_user.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(650, 280, 51, 51))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("C:\\Users\\Kieu Tien\\DoAnCuoiKy\\DoAnCuoiKi\\Ui\\ui_DangNhap\\../../Images/Images_DangNhap/ic_lock.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Kieu Tien\\DoAnCuoiKy\\DoAnCuoiKi\\Ui\\ui_DangNhap\\../../Images/Images_DangNhap/ic_back .png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_caution.setIcon(icon)
        self.pushButton_caution.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_caution.setObjectName("pushButton_caution")
        self.pushButtonMatKhau = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonMatKhau.setGeometry(QtCore.QRect(950, 280, 51, 51))
        self.pushButtonMatKhau.setStyleSheet("QPushButton {\n"
"border: 2px;  \n"
"border-radius: 25px;    \n"
"font: 14pt \"Sitka Display\";\n"
"background-color: rgb(232, 231, 231);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(176, 176, 176);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(176, 176, 176); \n"
"}\n"
"")
        self.pushButtonMatKhau.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\Kieu Tien\\DoAnCuoiKy\\DoAnCuoiKi\\Ui\\ui_DangNhap\\../../Images/Images_DangNhap/ic_hidden.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\Kieu Tien\\DoAnCuoiKy\\DoAnCuoiKi\\Ui\\ui_DangNhap\\../../Images/Images_DangNhap/ic_eye_open.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.pushButtonMatKhau.setIcon(icon1)
        self.pushButtonMatKhau.setCheckable(True)
        self.pushButtonMatKhau.setObjectName("pushButtonMatKhau")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Đăng Nhập"))
        self.lineEditTenDangNhap.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lineEditTenDangNhap.setPlaceholderText(_translate("MainWindow", "Nhập tên đăng nhập"))
        self.lineEditMatKhau.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lineEditMatKhau.setPlaceholderText(_translate("MainWindow", "Nhập mật khẩu"))
        self.pushButtonLogin.setText(_translate("MainWindow", "Đăng nhập"))
        self.pushButtonLogin.setShortcut(_translate("MainWindow", "Return"))
        self.pushButtonQuenMatKhau.setText(_translate("MainWindow", "Quên mật khẩu?"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">NỀN TẢNG QUẢN LÝ LỊCH HẸN CỦA PHÒNG KHÁM </span></p><p><span style=\" font-size:12pt; font-weight:600;\">THÚ Y DR. PET\'S HOUSE :</span></p><p><span style=\" font-size:12pt;\"><br/>1. Đăng nhập để </span><span style=\" font-size:12pt; font-weight:600;\">đặt lịch hẹn</span><span style=\" font-size:12pt;\"> nhanh chóng cho thú cưng.</span></p><p><span style=\" font-size:12pt;\">2. </span><span style=\" font-size:12pt; font-weight:600;\">Xem lịch sử khám</span><span style=\" font-size:12pt;\"> để theo dõi tình trạng sức khỏe</span></p><p><span style=\" font-size:12pt;\">3. </span><span style=\" font-size:12pt; font-weight:600;\">Điều chỉnh thông tin lịch hẹn</span><span style=\" font-size:12pt;\"> dễ dàng.</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Thông tin tài khoản đăng nhập quý khách vui </span></p><p><span style=\" font-weight:600;\">lòng xem trong phiếu xác nhận đặt lịch hẹn!</span></p></body></html>"))

# DoAnCuoiKi_ThaiDev
Bổ sung Model/Info_Customer: Thêm Username và password để khi tạo tài khoản từ giao diện phiếu xác nhận có thể lưu lại được
PhieuXacNhanExt : Thêm đầy đủ các tính năng, được đọc và viết lên file "../Dataset/Info_Customer.json
DatHenExt: Bổ sung tính năng khi bấm nút Đặt Hẹn sẽ hiện bảng thông báo xong chuyển sang giao diện PhieuXacNhanExt (Không thay đổi gì, chỉ bổ sung thêm 4 dòng cuối:

        from DoAnCuoiKi.Ui.ui_PhieuXacNhan.PhieuXacNhanExt import PhieuXacNhanExt  # Import muộn để tránh vòng lặp
        self.phieu_xac_nhan_window = PhieuXacNhanExt()
        self.phieu_xac_nhan_window.show()
        self.MainWindow.close()# Đóng giao diện đặt hẹn trước khi mở giao diện mới

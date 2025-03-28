import xlsxwriter as xr


class ExportTool:
    def export_customer_data_to_excel(self, filename, customers, selected_fields):
        if not selected_fields:
            print("Không có trường nào được chọn để xuất.")
            return

        if not customers:
            print("Danh sách khách hàng trống, không có dữ liệu để xuất.")
            return

        workbook = xr.Workbook(filename)
        worksheet = workbook.add_worksheet()

        # Danh sách cột có thể xuất
        columns = {
            "Mã Đơn": "madon",
            "Họ và Tên": "hovaten",
            "Số Điện Thoại Khách hàng": "sdt",
            "Địa Chỉ": "diachi",
            "Nơi khám": "noikham",
            "Ngày khám": "ngaykham",
            "Giờ khám": "giokham",
            "Dịch vụ": "dichvu",
            "Thông tin thêm": "thongtin",
            "Tình trạng": "tinhtrang",
            "Bác sĩ": "bacsi",
            "Số điện thoại bác sĩ": "sdtbacsi",
            "Tên đăng nhập": "tendangnhap",
            "Mật khẩu": "matkhau"
        }

        # Lọc các cột được chọn
        selected_columns = {key: columns[key] for key in selected_fields if key in columns}

        # Thiết lập độ rộng cột
        for idx, col_name in enumerate(selected_columns.keys()):
            worksheet.set_column(idx, idx, 20)

        bold = workbook.add_format({'bold': True})

        # Ghi tiêu đề cột
        for idx, col_name in enumerate(selected_columns.keys()):
            worksheet.write(0, idx, col_name, bold)

        # Ghi dữ liệu vào file
        for row, customer in enumerate(customers, start=1):
            if not isinstance(customer, dict):
                print(f"Dữ liệu không hợp lệ: {customer}")
                continue  # Bỏ qua nếu không phải dictionary

            for col, key in enumerate(selected_columns.values()):
                worksheet.write(row, col, customer.get(key, ""))

        workbook.close()
        print(f"Xuất Excel thành công: {filename}")



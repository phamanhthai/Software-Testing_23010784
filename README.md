# BÀI THỰC HÀNH – KIỂM THỬ HỘP ĐEN / HỘP TRẮNG (Black-box Testing)

> **Môn:** Đánh giá và kiểm định chất lượng phần mềm 
> **Phương pháp:** Kiểm thử hộp đen – Phân lớp tương đương + Phân tích giá trị biên 
>                  Kiểm thử hộp trắng (White-box Testing)   
> **Công cụ:** Java (OpenJDK 21), VSCode

---

## Cấu trúc thư mục

```
BlackBoxTesting/
├── README.md                       ← File hướng dẫn đọc bài tập
├── DanhSachTestCase.docx       ← Danh sách toàn bộ test case
├── KetQuaKiemThu.docx          ← Kết quả chạy kiểm thử (Pass/Fail)
└── MoTaKiemThuHopDen.docx      ← Mô tả cách áp dụng kiểm thử hộp đen
└── MoTaKiemThuHopTrang.docx      ← Mô tả cách áp dụng kiểm thử hộp trắng
└── src/
    ├── Bai1_ChuViHinhChuNhat.java
    ├── Bai2_DienTichHinhChuNhat.java
    ├── Bai3_PhuongTrinhBac2.java
    ├── Bai4_SoNgayCuaThang.java
    ├── Bai5_SoNguyenTo.java
    ├── Bai6_TongXenKe.java
    ├── Bai7_UCLN.java
    └── Bai8_TongGiaiThua.java
```

---

## Hướng dẫn đọc bài tập

### Bước 1 – Đọc mô tả kiểm thử
Mở file `docs/MoTaKiemThuHopDen.docx` để hiểu cách áp dụng 3 kỹ thuật kiểm thử hộp đen, hộp trắng cho từng bài:
- **Phân lớp tương đương** – chia miền đầu vào thành các nhóm xử lý giống nhau
- **Phân tích giá trị biên** – kiểm tra tại các điểm ranh giới
- **Dữ liệu không hợp lệ** – kiểm tra khi chương trình nhận đầu vào sai

### Bước 2 – Xem danh sách test case
Mở file `docs/DanhSachTestCase.docx` để xem toàn bộ các test case được thiết kế:
- Hàng **trắng** = dữ liệu hợp lệ
- Hàng **vàng** = giá trị biên đặc biệt (cần chú ý)
- Hàng **đỏ** = dữ liệu sai / không hợp lệ

### Bước 3 – Xem kết quả chạy kiểm thử
Mở file `docs/KetQuaKiemThu.docx` để xem kết quả thực tế khi chạy từng test case.

### Bước 4 – Đọc mã nguồn
Mở thư mục `src/` trong VSCode. Mỗi file Java tương ứng với một bài toán, bên trong đã bao gồm cả hàm xử lý lẫn các test case trong `main()`.

---

## Cách chạy chương trình trong VSCode

### Cài đặt yêu cầu
- Java JDK 17+ (hoặc OpenJDK 21)
- VSCode với Extension Pack for Java

### Chạy từng bài
Mở file `.java` trong VSCode, nhấn nút **Run** trên thanh công cụ, hoặc dùng terminal:

```bash
# Mở terminal trong VSCode (Ctrl + `)
cd src

javac Bai1_ChuViHinhChuNhat.java && java Bai1_ChuViHinhChuNhat
javac Bai2_DienTichHinhChuNhat.java && java Bai2_DienTichHinhChuNhat
javac Bai3_PhuongTrinhBac2.java && java Bai3_PhuongTrinhBac2
javac Bai4_SoNgayCuaThang.java && java Bai4_SoNgayCuaThang
javac Bai5_SoNguyenTo.java && java Bai5_SoNguyenTo
javac Bai6_TongXenKe.java && java Bai6_TongXenKe
javac Bai7_UCLN.java && java Bai7_UCLN
javac Bai8_TongGiaiThua.java && java Bai8_TongGiaiThua
```

---

## Tóm tắt 8 bài toán

| Bài | Chức năng | Đầu vào | Xử lý dữ liệu sai |
|-----|-----------|---------|-------------------|
| 1 | Chu vi HCN | a, b (double) | Trả -1 nếu a≤0 hoặc b≤0 |
| 2 | Diện tích HCN | a, b (double) | Trả -1 nếu a≤0 hoặc b≤0 |
| 3 | Giải PT bậc 2 | a, b, c (double) | Xử lý TH a=0 riêng |
| 4 | Số ngày tháng | tháng (1-12), năm (>0) | Trả -1 nếu ngoài phạm vi |
| 5 | Kiểm tra SNT | n (int) | Báo lỗi nếu n<0 |
| 6 | Tổng 1-2+3-4…+n | n (int ≥1) | Trả Long.MIN_VALUE nếu n≤0 |
| 7 | Tìm ƯCLN | a, b (int >0) | Trả -1 nếu a≤0 hoặc b≤0 |
| 8 | Tổng giai thừa | n (int ≥1) | Trả Long.MIN_VALUE / -1 |

---

## Kết quả kiểm thử tổng hợp

| Chỉ số | Giá trị |
|--------|---------|
| Tổng số test case | 75 |
| PASS | 75 (100%) |
| FAIL | 0 (0%) |
| Test case hợp lệ | 47 |
| Test case biên đặc biệt | 12 |
| Test case dữ liệu sai / không hợp lệ | 16 |

---

## GitHub Issues

Theo yêu cầu bài thực hành:

- **Issue 1** – Thiết kế và viết test case cho dữ liệu **hợp lệ**
- **Issue 2** – Thiết kế và viết test case cho dữ liệu **không hợp lệ, biên và ngoại lệ**

Mỗi issue được giải quyết bằng một commit riêng tương ứng.

# 📦 Bài Thực Hành: Kiểm Thử Hộp Đen (Black-box Testing)

> **Môn học:** Kiểm thử phần mềm  
> **Ngôn ngữ:** Python 3  
> **Framework kiểm thử:** `unittest` + `pytest`  
> **Kỹ thuật áp dụng:** Phân lớp tương đương · Phân tích giá trị biên · Dữ liệu không hợp lệ

---

## 📋 Nội dung bài tập

Bài gồm **8 chương trình Python**, mỗi chương trình có mã nguồn và test case kiểm thử hộp đen đầy đủ:

| # | Bài toán | File |
|---|----------|------|
| 1 | Tính chu vi hình chữ nhật | `src/bai1_chu_vi_hcn.py` |
| 2 | Tính diện tích hình chữ nhật | `src/bai2_dien_tich_hcn.py` |
| 3 | Giải phương trình bậc 2 | `src/bai3_pt_bac2.py` |
| 4 | Tính số ngày của một tháng | `src/bai4_so_ngay_thang.py` |
| 5 | Kiểm tra số nguyên tố | `src/bai5_nguyen_to.py` |
| 6 | Tính tổng S = 1 - 2 + 3 - 4 + ... + n | `src/bai6_tong_xen_ke.py` |
| 7 | Tìm UCLN của a và b | `src/bai7_ucln.py` |
| 8 | Tính tổng S = 1! + 2! + 3! + ... + n! | `src/bai8_tong_giai_thua.py` |

---

## 📁 Cấu trúc thư mục

```
black-box-testing/
│
├── src/                          # Mã nguồn 8 bài toán + test cases
│   ├── bai1_chu_vi_hcn.py
│   ├── bai2_dien_tich_hcn.py
│   ├── bai3_pt_bac2.py
│   ├── bai4_so_ngay_thang.py
│   ├── bai5_nguyen_to.py
│   ├── bai6_tong_xen_ke.py
│   ├── bai7_ucln.py
│   └── bai8_tong_giai_thua.py
│
├── docs/                         # Tài liệu nộp bài
│   ├── 1_danh_sach_testcase.docx          # Danh sách test case chi tiết
│   ├── 2_ket_qua_kiem_thu.docx            # Kết quả chạy kiểm thử
│   └── 3_mo_ta_kiem_thu_hop_den.docx      # Mô tả cách áp dụng kiểm thử hộp đen
│
└── README.md
```

---

## 🚀 Hướng dẫn chạy kiểm thử

### Yêu cầu
- Python 3.x
- pytest (`pip install pytest`)

### Chạy tất cả test cases

```bash
cd src
python -m pytest -v
```

### Chạy test case của từng bài

```bash
# Ví dụ: chạy riêng bài 3
python -m pytest bai3_pt_bac2.py -v

# Chạy và xem kết quả tóm tắt
python -m pytest --tb=short
```

### Kết quả mong đợi

```
============================= test session starts ==============================
collected 88 items

bai1_chu_vi_hcn.py      9 passed
bai2_dien_tich_hcn.py   9 passed
bai3_pt_bac2.py         9 passed
bai4_so_ngay_thang.py  13 passed
bai5_nguyen_to.py      12 passed
bai6_tong_xen_ke.py    11 passed
bai7_ucln.py           11 passed
bai8_tong_giai_thua.py 14 passed

============================== 88 passed in 3.56s ==============================
```

---

## 📄 Xem tài liệu bài làm

Tất cả tài liệu nằm trong thư mục `docs/`:

| Tài liệu | Nội dung |
|----------|----------|
| [`1_danh_sach_testcase.docx`](docs/1_danh_sach_testcase.docx) | Bảng liệt kê đầy đủ các test case cho cả 8 bài, phân loại theo: hợp lệ, giá trị biên, không hợp lệ |
| [`2_ket_qua_kiem_thu.docx`](docs/2_ket_qua_kiem_thu.docx) | Kết quả chạy kiểm thử thực tế: lệnh chạy, output terminal, bảng tổng hợp và chi tiết từng bài |
| [`3_mo_ta_kiem_thu_hop_den.docx`](docs/3_mo_ta_kiem_thu_hop_den.docx) | Giải thích cách áp dụng phân lớp tương đương, giá trị biên và dữ liệu không hợp lệ cho từng bài |

---

## 🔍 Kỹ thuật kiểm thử hộp đen áp dụng

### 1. Phân lớp tương đương (Equivalence Partitioning)
Chia miền đầu vào thành các lớp có hành vi tương tự nhau. Chọn một đại diện cho mỗi lớp để giảm số lượng test case mà vẫn đảm bảo độ phủ.

**Ví dụ – Bài 5 (Kiểm tra số nguyên tố):**
- Lớp 1: n là số nguyên tố (n=2, n=7, n=97) → kết quả `True`
- Lớp 2: n là hợp số (n=4, n=9) → kết quả `False`
- Lớp 3: n < 2 (n=0, n=1, n=-5) → `ValueError`

### 2. Phân tích giá trị biên (Boundary Value Analysis)
Tập trung kiểm thử tại các giá trị cận biên vì lỗi thường xảy ra ở đây.

**Ví dụ – Bài 4 (Số ngày tháng):**
- Biên tháng: tháng=1, tháng=12
- Biên năm nhuận: năm 1900 (chia 100, không chia 400 → không nhuận), năm 2000 (chia 400 → nhuận)

### 3. Dữ liệu không hợp lệ (Invalid Data Testing)
Đưa vào dữ liệu ngoài miền hợp lệ để kiểm tra khả năng xử lý lỗi: giá trị 0, âm, số thực thay cho nguyên, chuỗi ký tự, None, danh sách.

---

## 📊 Thống kê test cases

| Bài | Hợp lệ | Biên | Không hợp lệ | Tổng |
|-----|--------|------|--------------|------|
| Bài 1 | 4 | 1 | 4 | 9 |
| Bài 2 | 4 | 1 | 4 | 9 |
| Bài 3 | 5 | 1 | 3 | 9 |
| Bài 4 | 4 | 4 | 5 | 13 |
| Bài 5 | 5 | 2 | 5 | 12 |
| Bài 6 | 6 | 1 | 4 | 11 |
| Bài 7 | 6 | 1 | 4 | 11 |
| Bài 8 | 8 | 1 | 5 | 14 |
| **Tổng** | **42** | **12** | **34** | **88** |

---

## 🗂️ GitHub Issues

- **Issue #1 – Test case dữ liệu hợp lệ:** Thiết kế và triển khai 54 test cases (hợp lệ + biên) cho 8 bài toán
- **Issue #2 – Test case dữ liệu không hợp lệ:** Thiết kế và triển khai 34 test cases dữ liệu sai, biên ngoại lệ cho 8 bài toán

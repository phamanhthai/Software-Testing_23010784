"""
Bài 4: Tính số ngày của một tháng
Input: tháng (1-12), năm (số nguyên dương)
Output: số ngày trong tháng đó
  - Tháng 2: 28 hoặc 29 (năm nhuận)
  - Tháng 4,6,9,11: 30 ngày
  - Tháng còn lại: 31 ngày
"""

def so_ngay_trong_thang(thang, nam):
    if not (isinstance(thang, int) and isinstance(nam, int)):
        raise TypeError("Tháng và năm phải là số nguyên!")
    if thang < 1 or thang > 12:
        raise ValueError("Tháng phải trong khoảng 1-12!")
    if nam <= 0:
        raise ValueError("Năm phải là số dương!")

    def la_nam_nhuan(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    if thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    elif thang in [4, 6, 9, 11]:
        return 30
    else:
        return 31


# ===================== TEST CASES =====================
import unittest

class TestSoNgayTrongThang(unittest.TestCase):

    # --- Dữ liệu HỢP LỆ ---
    def test_thang_31_ngay(self):
        """Hợp lệ: tháng 1 → 31 ngày"""
        self.assertEqual(so_ngay_trong_thang(1, 2023), 31)

    def test_thang_30_ngay(self):
        """Hợp lệ: tháng 4 → 30 ngày"""
        self.assertEqual(so_ngay_trong_thang(4, 2023), 30)

    def test_thang2_nam_nhuan(self):
        """Hợp lệ: tháng 2 năm nhuận 2024 → 29 ngày"""
        self.assertEqual(so_ngay_trong_thang(2, 2024), 29)

    def test_thang2_khong_nhuan(self):
        """Hợp lệ: tháng 2 năm thường 2023 → 28 ngày"""
        self.assertEqual(so_ngay_trong_thang(2, 2023), 28)

    def test_thang2_nam_chia_100(self):
        """Biên: năm 1900 chia hết 100 nhưng không chia hết 400 → không nhuận → 28 ngày"""
        self.assertEqual(so_ngay_trong_thang(2, 1900), 28)

    def test_thang2_nam_chia_400(self):
        """Biên: năm 2000 chia hết 400 → nhuận → 29 ngày"""
        self.assertEqual(so_ngay_trong_thang(2, 2000), 29)

    # --- Giá trị biên ---
    def test_boundary_thang_1(self):
        """Biên dưới: tháng 1"""
        self.assertEqual(so_ngay_trong_thang(1, 2023), 31)

    def test_boundary_thang_12(self):
        """Biên trên: tháng 12"""
        self.assertEqual(so_ngay_trong_thang(12, 2023), 31)

    # --- ⚠️ DỮ LIỆU SAI / KHÔNG HỢP LỆ ---
    def test_invalid_thang_0(self):
        """KHÔNG HỢP LỆ: tháng=0 → ValueError"""
        with self.assertRaises(ValueError):
            so_ngay_trong_thang(0, 2023)

    def test_invalid_thang_13(self):
        """KHÔNG HỢP LỆ: tháng=13 → ValueError"""
        with self.assertRaises(ValueError):
            so_ngay_trong_thang(13, 2023)

    def test_invalid_nam_am(self):
        """KHÔNG HỢP LỆ: năm=-1 → ValueError"""
        with self.assertRaises(ValueError):
            so_ngay_trong_thang(5, -1)

    def test_invalid_float(self):
        """KHÔNG HỢP LỆ: tháng=3.5 → TypeError"""
        with self.assertRaises(TypeError):
            so_ngay_trong_thang(3.5, 2023)

    def test_invalid_string(self):
        """KHÔNG HỢP LỆ: tháng='abc' → TypeError"""
        with self.assertRaises(TypeError):
            so_ngay_trong_thang("abc", 2023)

if __name__ == "__main__":
    unittest.main(verbosity=2)

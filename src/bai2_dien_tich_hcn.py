"""
Bài 2: Tính diện tích hình chữ nhật
Input: chiều dài (a), chiều rộng (b) - số thực dương
Output: diện tích = a * b
"""

def tinh_dien_tich(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Đầu vào phải là số!")
    if a <= 0 or b <= 0:
        raise ValueError("Chiều dài và chiều rộng phải là số dương!")
    return a * b


# ===================== TEST CASES =====================
import unittest

class TestDienTichHCN(unittest.TestCase):

    # --- Dữ liệu HỢP LỆ ---
    def test_valid_normal(self):
        """Hợp lệ: a=5, b=3 → DT=15"""
        self.assertEqual(tinh_dien_tich(5, 3), 15)

    def test_valid_float(self):
        """Hợp lệ: a=2.5, b=4.0 → DT=10.0"""
        self.assertAlmostEqual(tinh_dien_tich(2.5, 4.0), 10.0)

    def test_valid_square(self):
        """Hợp lệ: hình vuông a=b=6 → DT=36"""
        self.assertEqual(tinh_dien_tich(6, 6), 36)

    def test_valid_large(self):
        """Hợp lệ: số lớn a=1000, b=2000 → DT=2000000"""
        self.assertEqual(tinh_dien_tich(1000, 2000), 2000000)

    # --- Giá trị biên ---
    def test_boundary_very_small(self):
        """Biên dưới: a=0.01, b=0.01 → DT=0.0001"""
        self.assertAlmostEqual(tinh_dien_tich(0.01, 0.01), 0.0001, places=6)

    # --- ⚠️ DỮ LIỆU SAI / KHÔNG HỢP LỆ ---
    def test_invalid_zero(self):
        """KHÔNG HỢP LỆ: a=0 → ValueError"""
        with self.assertRaises(ValueError):
            tinh_dien_tich(0, 5)

    def test_invalid_negative(self):
        """KHÔNG HỢP LỆ: a=-2, b=3 → ValueError"""
        with self.assertRaises(ValueError):
            tinh_dien_tich(-2, 3)

    def test_invalid_string(self):
        """KHÔNG HỢP LỆ: b='xyz' → TypeError"""
        with self.assertRaises(TypeError):
            tinh_dien_tich(5, "xyz")

    def test_invalid_none(self):
        """KHÔNG HỢP LỆ: b=None → TypeError"""
        with self.assertRaises(TypeError):
            tinh_dien_tich(5, None)

if __name__ == "__main__":
    unittest.main(verbosity=2)

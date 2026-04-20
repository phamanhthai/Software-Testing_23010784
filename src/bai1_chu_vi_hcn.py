"""
Bài 1: Tính chu vi hình chữ nhật
Input: chiều dài (a), chiều rộng (b) - số thực dương
Output: chu vi = 2 * (a + b)
"""

def tinh_chu_vi(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Đầu vào phải là số!")
    if a <= 0 or b <= 0:
        raise ValueError("Chiều dài và chiều rộng phải là số dương!")
    return 2 * (a + b)


# ===================== TEST CASES =====================
import unittest

class TestChuViHCN(unittest.TestCase):

    # --- Dữ liệu HỢP LỆ ---
    def test_valid_normal(self):
        """Hợp lệ: a=5, b=3 → CV=16"""
        self.assertEqual(tinh_chu_vi(5, 3), 16)

    def test_valid_square(self):
        """Hợp lệ: hình vuông a=b=4 → CV=16"""
        self.assertEqual(tinh_chu_vi(4, 4), 16)

    def test_valid_float(self):
        """Hợp lệ: số thực a=2.5, b=1.5 → CV=8.0"""
        self.assertAlmostEqual(tinh_chu_vi(2.5, 1.5), 8.0)

    def test_valid_large(self):
        """Hợp lệ: số lớn a=1000, b=500 → CV=3000"""
        self.assertEqual(tinh_chu_vi(1000, 500), 3000)

    # --- Giá trị biên ---
    def test_boundary_small_positive(self):
        """Biên dưới: a=0.001, b=0.001 → CV=0.004"""
        self.assertAlmostEqual(tinh_chu_vi(0.001, 0.001), 0.004, places=5)

    # --- ⚠️ DỮ LIỆU SAI / KHÔNG HỢP LỆ ---
    def test_invalid_zero_a(self):
        """KHÔNG HỢP LỆ: a=0 → ValueError"""
        with self.assertRaises(ValueError):
            tinh_chu_vi(0, 5)

    def test_invalid_negative_b(self):
        """KHÔNG HỢP LỆ: b=-3 → ValueError"""
        with self.assertRaises(ValueError):
            tinh_chu_vi(5, -3)

    def test_invalid_string_input(self):
        """KHÔNG HỢP LỆ: a='abc' → TypeError"""
        with self.assertRaises(TypeError):
            tinh_chu_vi("abc", 3)

    def test_invalid_none(self):
        """KHÔNG HỢP LỆ: a=None → TypeError"""
        with self.assertRaises(TypeError):
            tinh_chu_vi(None, 3)

if __name__ == "__main__":
    unittest.main(verbosity=2)

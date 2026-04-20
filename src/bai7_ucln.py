"""
Bài 7: Tìm UCLN (Ước Chung Lớn Nhất) của a và b
Input: a, b (số nguyên dương)
Output: UCLN(a, b)
"""

def tinh_ucln(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("a và b phải là số nguyên!")
    if a <= 0 or b <= 0:
        raise ValueError("a và b phải là số nguyên dương!")
    
    while b != 0:
        a, b = b, a % b
    return a


# ===================== TEST CASES =====================
import unittest

class TestUCLN(unittest.TestCase):

    # --- Dữ liệu HỢP LỆ ---
    def test_ucln_normal(self):
        """Hợp lệ: UCLN(12, 8) = 4"""
        self.assertEqual(tinh_ucln(12, 8), 4)

    def test_ucln_coprime(self):
        """Hợp lệ: UCLN(7, 13) = 1 (nguyên tố cùng nhau)"""
        self.assertEqual(tinh_ucln(7, 13), 1)

    def test_ucln_same(self):
        """Hợp lệ: UCLN(5, 5) = 5"""
        self.assertEqual(tinh_ucln(5, 5), 5)

    def test_ucln_one(self):
        """Hợp lệ: UCLN(1, 9) = 1"""
        self.assertEqual(tinh_ucln(1, 9), 1)

    def test_ucln_large(self):
        """Hợp lệ: UCLN(100, 75) = 25"""
        self.assertEqual(tinh_ucln(100, 75), 25)

    def test_ucln_swapped(self):
        """Hợp lệ: UCLN(8, 12) = UCLN(12, 8) = 4"""
        self.assertEqual(tinh_ucln(8, 12), 4)

    # --- Giá trị biên ---
    def test_boundary_a1(self):
        """Biên: a=1 → UCLN=1"""
        self.assertEqual(tinh_ucln(1, 1), 1)

    # --- ⚠️ DỮ LIỆU SAI / KHÔNG HỢP LỆ ---
    def test_invalid_zero_a(self):
        """KHÔNG HỢP LỆ: a=0 → ValueError"""
        with self.assertRaises(ValueError):
            tinh_ucln(0, 5)

    def test_invalid_negative(self):
        """KHÔNG HỢP LỆ: b=-4 → ValueError"""
        with self.assertRaises(ValueError):
            tinh_ucln(8, -4)

    def test_invalid_float(self):
        """KHÔNG HỢP LỆ: a=3.5 → TypeError"""
        with self.assertRaises(TypeError):
            tinh_ucln(3.5, 5)

    def test_invalid_string(self):
        """KHÔNG HỢP LỆ: a='abc' → TypeError"""
        with self.assertRaises(TypeError):
            tinh_ucln("abc", 5)

if __name__ == "__main__":
    unittest.main(verbosity=2)

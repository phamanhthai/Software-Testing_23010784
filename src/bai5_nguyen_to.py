"""
Bài 5: Kiểm tra n có phải là số nguyên tố hay không
Input: n (số nguyên)
Output: True/False + thông báo
"""

def kiem_tra_nguyen_to(n):
    if not isinstance(n, int):
        raise TypeError("n phải là số nguyên!")
    if n < 2:
        raise ValueError("Số nguyên tố phải >= 2!")
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# ===================== TEST CASES =====================
import unittest

class TestKiemTraNguyenTo(unittest.TestCase):

    # --- Dữ liệu HỢP LỆ ---
    def test_so_nguyen_to_2(self):
        """Hợp lệ: 2 là số nguyên tố"""
        self.assertTrue(kiem_tra_nguyen_to(2))

    def test_so_nguyen_to_7(self):
        """Hợp lệ: 7 là số nguyên tố"""
        self.assertTrue(kiem_tra_nguyen_to(7))

    def test_khong_nguyen_to_4(self):
        """Hợp lệ: 4 không phải số nguyên tố"""
        self.assertFalse(kiem_tra_nguyen_to(4))

    def test_khong_nguyen_to_1_composite(self):
        """Hợp lệ: 9 không phải số nguyên tố"""
        self.assertFalse(kiem_tra_nguyen_to(9))

    def test_so_nguyen_to_lon(self):
        """Hợp lệ: 97 là số nguyên tố"""
        self.assertTrue(kiem_tra_nguyen_to(97))

    # --- Giá trị biên ---
    def test_boundary_2(self):
        """Biên dưới: n=2 → nguyên tố"""
        self.assertTrue(kiem_tra_nguyen_to(2))

    def test_boundary_3(self):
        """Biên: n=3 → nguyên tố"""
        self.assertTrue(kiem_tra_nguyen_to(3))

    # --- ⚠️ DỮ LIỆU SAI / KHÔNG HỢP LỆ ---
    def test_invalid_less_than_2(self):
        """KHÔNG HỢP LỆ: n=1 → ValueError"""
        with self.assertRaises(ValueError):
            kiem_tra_nguyen_to(1)

    def test_invalid_zero(self):
        """KHÔNG HỢP LỆ: n=0 → ValueError"""
        with self.assertRaises(ValueError):
            kiem_tra_nguyen_to(0)

    def test_invalid_negative(self):
        """KHÔNG HỢP LỆ: n=-5 → ValueError"""
        with self.assertRaises(ValueError):
            kiem_tra_nguyen_to(-5)

    def test_invalid_float(self):
        """KHÔNG HỢP LỆ: n=3.14 → TypeError"""
        with self.assertRaises(TypeError):
            kiem_tra_nguyen_to(3.14)

    def test_invalid_string(self):
        """KHÔNG HỢP LỆ: n='7' → TypeError"""
        with self.assertRaises(TypeError):
            kiem_tra_nguyen_to("7")

if __name__ == "__main__":
    unittest.main(verbosity=2)

"""
Bài 8: Tính tổng S = 1! + 2! + 3! + ... + n!
Input: n (số nguyên dương)
Output: tổng S, sử dụng hàm tính giai thừa riêng
"""

def tinh_giai_thua(k):
    """Hàm tính giai thừa của k"""
    if k == 0 or k == 1:
        return 1
    result = 1
    for i in range(2, k + 1):
        result *= i
    return result


def tinh_tong_giai_thua(n):
    if not isinstance(n, int):
        raise TypeError("n phải là số nguyên!")
    if n <= 0:
        raise ValueError("n phải là số nguyên dương (>= 1)!")
    
    S = 0
    for i in range(1, n + 1):
        S += tinh_giai_thua(i)
    return S


# ===================== TEST CASES =====================
import unittest

class TestTongGiaiThua(unittest.TestCase):

    # --- Kiểm tra hàm giai thừa riêng ---
    def test_giai_thua_0(self):
        """Hàm giai thừa: 0! = 1"""
        self.assertEqual(tinh_giai_thua(0), 1)

    def test_giai_thua_1(self):
        """Hàm giai thừa: 1! = 1"""
        self.assertEqual(tinh_giai_thua(1), 1)

    def test_giai_thua_5(self):
        """Hàm giai thừa: 5! = 120"""
        self.assertEqual(tinh_giai_thua(5), 120)

    # --- Dữ liệu HỢP LỆ (tổng) ---
    def test_n1(self):
        """Hợp lệ: n=1 → S=1!=1"""
        self.assertEqual(tinh_tong_giai_thua(1), 1)

    def test_n2(self):
        """Hợp lệ: n=2 → S=1!+2!=1+2=3"""
        self.assertEqual(tinh_tong_giai_thua(2), 3)

    def test_n3(self):
        """Hợp lệ: n=3 → S=1!+2!+3!=1+2+6=9"""
        self.assertEqual(tinh_tong_giai_thua(3), 9)

    def test_n4(self):
        """Hợp lệ: n=4 → S=1+2+6+24=33"""
        self.assertEqual(tinh_tong_giai_thua(4), 33)

    def test_n5(self):
        """Hợp lệ: n=5 → S=1+2+6+24+120=153"""
        self.assertEqual(tinh_tong_giai_thua(5), 153)

    # --- Giá trị biên ---
    def test_boundary_n1(self):
        """Biên dưới: n=1"""
        self.assertEqual(tinh_tong_giai_thua(1), 1)

    # --- ⚠️ DỮ LIỆU SAI / KHÔNG HỢP LỆ ---
    def test_invalid_zero(self):
        """KHÔNG HỢP LỆ: n=0 → ValueError"""
        with self.assertRaises(ValueError):
            tinh_tong_giai_thua(0)

    def test_invalid_negative(self):
        """KHÔNG HỢP LỆ: n=-1 → ValueError"""
        with self.assertRaises(ValueError):
            tinh_tong_giai_thua(-1)

    def test_invalid_float(self):
        """KHÔNG HỢP LỆ: n=2.5 → TypeError"""
        with self.assertRaises(TypeError):
            tinh_tong_giai_thua(2.5)

    def test_invalid_string(self):
        """KHÔNG HỢP LỆ: n='three' → TypeError"""
        with self.assertRaises(TypeError):
            tinh_tong_giai_thua("three")

    def test_invalid_list(self):
        """KHÔNG HỢP LỆ: n=[3] → TypeError"""
        with self.assertRaises(TypeError):
            tinh_tong_giai_thua([3])

if __name__ == "__main__":
    unittest.main(verbosity=2)

"""
Bài 6: Tính tổng S = 1 - 2 + 3 - 4 + ... + n
Input: n (số nguyên dương)
Output: tổng S
"""

def tinh_tong_xen_ke(n):
    if not isinstance(n, int):
        raise TypeError("n phải là số nguyên!")
    if n <= 0:
        raise ValueError("n phải là số nguyên dương (>= 1)!")
    
    S = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            S += i
        else:
            S -= i
    return S


# ===================== TEST CASES =====================
import unittest

class TestTongXenKe(unittest.TestCase):

    # --- Dữ liệu HỢP LỆ ---
    def test_n1(self):
        """Hợp lệ: n=1 → S=1"""
        self.assertEqual(tinh_tong_xen_ke(1), 1)

    def test_n2(self):
        """Hợp lệ: n=2 → S=1-2=-1"""
        self.assertEqual(tinh_tong_xen_ke(2), -1)

    def test_n3(self):
        """Hợp lệ: n=3 → S=1-2+3=2"""
        self.assertEqual(tinh_tong_xen_ke(3), 2)

    def test_n4(self):
        """Hợp lệ: n=4 → S=1-2+3-4=-2"""
        self.assertEqual(tinh_tong_xen_ke(4), -2)

    def test_n5(self):
        """Hợp lệ: n=5 → S=1-2+3-4+5=3"""
        self.assertEqual(tinh_tong_xen_ke(5), 3)

    def test_large_n(self):
        """Hợp lệ: n=100 → S=-50 (n chẵn → S=-n/2)"""
        self.assertEqual(tinh_tong_xen_ke(100), -50)

    # --- Giá trị biên ---
    def test_boundary_n1(self):
        """Biên dưới: n=1"""
        self.assertEqual(tinh_tong_xen_ke(1), 1)

    # --- ⚠️ DỮ LIỆU SAI / KHÔNG HỢP LỆ ---
    def test_invalid_zero(self):
        """KHÔNG HỢP LỆ: n=0 → ValueError"""
        with self.assertRaises(ValueError):
            tinh_tong_xen_ke(0)

    def test_invalid_negative(self):
        """KHÔNG HỢP LỆ: n=-3 → ValueError"""
        with self.assertRaises(ValueError):
            tinh_tong_xen_ke(-3)

    def test_invalid_float(self):
        """KHÔNG HỢP LỆ: n=3.5 → TypeError"""
        with self.assertRaises(TypeError):
            tinh_tong_xen_ke(3.5)

    def test_invalid_string(self):
        """KHÔNG HỢP LỆ: n='five' → TypeError"""
        with self.assertRaises(TypeError):
            tinh_tong_xen_ke("five")

if __name__ == "__main__":
    unittest.main(verbosity=2)

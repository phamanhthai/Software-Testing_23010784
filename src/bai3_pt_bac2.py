"""
Bài 3: Giải phương trình bậc 2
Input: a, b, c (số thực), a ≠ 0
Output: nghiệm của ax² + bx + c = 0
  - Vô nghiệm nếu delta < 0
  - Nghiệm kép nếu delta = 0
  - 2 nghiệm phân biệt nếu delta > 0
"""

import math

def giai_pt_bac2(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("a, b, c phải là số!")
    if a == 0:
        raise ValueError("a phải khác 0 (phương trình bậc 2)!")
    
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b / (2*a)
        return f"Nghiệm kép: x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Hai nghiệm: x1 = {x1}, x2 = {x2}"


# ===================== TEST CASES =====================
import unittest

class TestGiaiPTBac2(unittest.TestCase):

    # --- Dữ liệu HỢP LỆ ---
    def test_two_roots(self):
        """Hợp lệ: x²-5x+6=0 → x1=3, x2=2"""
        result = giai_pt_bac2(1, -5, 6)
        self.assertIn("3.0", result)
        self.assertIn("2.0", result)

    def test_double_root(self):
        """Hợp lệ: x²-2x+1=0 → nghiệm kép x=1"""
        result = giai_pt_bac2(1, -2, 1)
        self.assertIn("Nghiệm kép", result)
        self.assertIn("1.0", result)

    def test_no_root(self):
        """Hợp lệ: x²+1=0 → vô nghiệm"""
        result = giai_pt_bac2(1, 0, 1)
        self.assertIn("vô nghiệm", result)

    def test_negative_a(self):
        """Hợp lệ: a âm: -x²+2x-1=0 → nghiệm kép x=1"""
        result = giai_pt_bac2(-1, 2, -1)
        self.assertIn("Nghiệm kép", result)

    def test_float_coefficients(self):
        """Hợp lệ: hệ số thực 0.5x²-x+0.5=0 → nghiệm kép"""
        result = giai_pt_bac2(0.5, -1, 0.5)
        self.assertIn("Nghiệm kép", result)

    # --- Giá trị biên ---
    def test_boundary_delta_zero(self):
        """Biên: delta=0 → nghiệm kép"""
        result = giai_pt_bac2(1, 2, 1)
        self.assertIn("Nghiệm kép", result)

    # --- ⚠️ DỮ LIỆU SAI / KHÔNG HỢP LỆ ---
    def test_invalid_a_zero(self):
        """KHÔNG HỢP LỆ: a=0 → ValueError"""
        with self.assertRaises(ValueError):
            giai_pt_bac2(0, 2, 1)

    def test_invalid_string(self):
        """KHÔNG HỢP LỆ: a='x' → TypeError"""
        with self.assertRaises(TypeError):
            giai_pt_bac2("x", 1, 1)

    def test_invalid_none(self):
        """KHÔNG HỢP LỆ: b=None → TypeError"""
        with self.assertRaises(TypeError):
            giai_pt_bac2(1, None, 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)

public class Bai8_TongGiaiThua {

    /**
     * Tính giai thừa n!
     * @param n số nguyên không âm
     * @return n!
     */
    public static long giaiThua(int n) {
        if (n < 0) return -1; // Không hợp lệ
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    /**
     * Tính tổng S = 1! + 2! + 3! + ... + n!
     * @param n số hạng cuối (n >= 1)
     * @return tổng S, hoặc -1 nếu không hợp lệ
     */
    public static long tinhTong(int n) {
        if (n < 1) return Long.MIN_VALUE; // Không hợp lệ
        long s = 0;
        for (int i = 1; i <= n; i++) {
            s += giaiThua(i);
        }
        return s;
    }

    public static void main(String[] args) {
        System.out.println("=== BÀI 8: TỔNG S = 1! + 2! + 3! + ... + n! ===");

        // --- HỢP LỆ ---
        // TC1: n=1 → 1! = 1
        System.out.println("TC1 n=1: " + tinhTong(1));   // 1

        // TC2: n=2 → 1! + 2! = 1 + 2 = 3
        System.out.println("TC2 n=2: " + tinhTong(2));   // 3

        // TC3: n=3 → 1! + 2! + 3! = 1 + 2 + 6 = 9
        System.out.println("TC3 n=3: " + tinhTong(3));   // 9

        // TC4: n=4 → 9 + 24 = 33
        System.out.println("TC4 n=4: " + tinhTong(4));   // 33

        // TC5: n=5 → 33 + 120 = 153
        System.out.println("TC5 n=5: " + tinhTong(5));   // 153

        // TC6: n=10
        System.out.println("TC6 n=10: " + tinhTong(10)); // 4037913

        // Kiểm thử riêng hàm giaiThua
        System.out.println("\n--- Kiểm thử hàm giaiThua ---");
        System.out.println("0! = " + giaiThua(0)); // 1 (theo định nghĩa)
        System.out.println("1! = " + giaiThua(1)); // 1
        System.out.println("5! = " + giaiThua(5)); // 120

        // --- BIÊN / KHÔNG HỢP LỆ ---
        // TC7: n = 0 trong tinhTong → KHÔNG HỢP LỆ [BIÊN]
        System.out.println("\nTC7 n=0  [KO HỢP LỆ tinhTong]: " + tinhTong(0));   // MIN_VALUE

        // TC8: n âm → KHÔNG HỢP LỆ [DỮ LIỆU SAI]
        System.out.println("TC8 n=-1 [KO HỢP LỆ tinhTong]: " + tinhTong(-1));   // MIN_VALUE

        // TC9: giaiThua(-3) → KHÔNG HỢP LỆ [DỮ LIỆU SAI]
        System.out.println("TC9 giaiThua(-3) [KO HỢP LỆ]: " + giaiThua(-3));    // -1
    }
}

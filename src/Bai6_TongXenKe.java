public class Bai6_TongXenKe {

    /**
     * Tính tổng S = 1 - 2 + 3 - 4 + ... + n
     * Số dương: vị trí lẻ (1, 3, 5,...), số âm: vị trí chẵn (2, 4, 6,...)
     * @param n số hạng cuối (n >= 1)
     * @return tổng S, hoặc Integer.MIN_VALUE nếu không hợp lệ
     */
    public static long tinhTong(int n) {
        if (n < 1) {
            return Long.MIN_VALUE; // Không hợp lệ
        }
        long s = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 1) s += i;  // Số lẻ: cộng
            else             s -= i;  // Số chẵn: trừ
        }
        return s;
    }

    public static void main(String[] args) {
        System.out.println("=== BÀI 6: TỔNG S = 1 - 2 + 3 - 4 + ... + n ===");

        // --- HỢP LỆ ---
        System.out.println("TC1 n=1: " + tinhTong(1));   // 1
        System.out.println("TC2 n=2: " + tinhTong(2));   // 1-2 = -1
        System.out.println("TC3 n=3: " + tinhTong(3));   // 1-2+3 = 2
        System.out.println("TC4 n=4: " + tinhTong(4));   // 1-2+3-4 = -2
        System.out.println("TC5 n=5: " + tinhTong(5));   // 1-2+3-4+5 = 3
        System.out.println("TC6 n=10: " + tinhTong(10)); // -5
        System.out.println("TC7 n=100: " + tinhTong(100)); // -50

        // --- BIÊN / KHÔNG HỢP LỆ ---
        // TC8: n = 0 → KHÔNG HỢP LỆ [BIÊN]
        System.out.println("TC8 n=0  [KO HỢP LỆ]: " + tinhTong(0));   // MIN_VALUE

        // TC9: n âm → KHÔNG HỢP LỆ [DỮ LIỆU SAI]
        System.out.println("TC9 n=-3 [KO HỢP LỆ]: " + tinhTong(-3));  // MIN_VALUE
    }
}

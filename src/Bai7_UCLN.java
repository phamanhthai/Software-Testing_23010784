public class Bai7_UCLN {

    /**
     * Tìm ƯCLN của a và b bằng thuật toán Euclid
     * @param a số nguyên dương
     * @param b số nguyên dương
     * @return ƯCLN(a, b), hoặc -1 nếu không hợp lệ
     */
    public static int ucln(int a, int b) {
        if (a <= 0 || b <= 0) {
            return -1; // Không hợp lệ
        }
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public static void main(String[] args) {
        System.out.println("=== BÀI 7: TÌM ƯCLN ===");

        // --- HỢP LỆ ---
        System.out.println("TC1 (12, 8):   " + ucln(12, 8));    // 4
        System.out.println("TC2 (36, 24):  " + ucln(36, 24));   // 12
        System.out.println("TC3 (7, 5):    " + ucln(7, 5));     // 1 (nguyên tố cùng nhau)
        System.out.println("TC4 (100, 10): " + ucln(100, 10));  // 10
        System.out.println("TC5 (5, 5):    " + ucln(5, 5));     // 5 (a == b)
        System.out.println("TC6 (1, 1):    " + ucln(1, 1));     // 1 (biên nhỏ nhất hợp lệ)
        System.out.println("TC7 (15, 1):   " + ucln(15, 1));    // 1

        // --- BIÊN / KHÔNG HỢP LỆ ---
        // TC8: a = 0 → KHÔNG HỢP LỆ [DỮ LIỆU SAI]
        System.out.println("TC8 (0, 5)   [KO HỢP LỆ]: " + ucln(0, 5));   // -1

        // TC9: b âm → KHÔNG HỢP LỆ [DỮ LIỆU SAI]
        System.out.println("TC9 (6, -3)  [KO HỢP LỆ]: " + ucln(6, -3)); // -1

        // TC10: cả hai âm → KHÔNG HỢP LỆ
        System.out.println("TC10 (-4, -8) [KO HỢP LỆ]: " + ucln(-4, -8)); // -1
    }
}

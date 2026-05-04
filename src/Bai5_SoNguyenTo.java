public class Bai5_SoNguyenTo {

    /**
     * Kiểm tra n có phải là số nguyên tố hay không
     * Số nguyên tố: n > 1 và chỉ chia hết cho 1 và chính nó
     * @param n số cần kiểm tra
     * @return true nếu là số nguyên tố, false nếu không phải, null nếu không hợp lệ
     */
    public static String kiemTraNguyenTo(int n) {
        if (n < 0) return "Không hợp lệ (n < 0)";
        if (n < 2) return n + " KHÔNG là số nguyên tố";
        if (n == 2) return n + " LÀ số nguyên tố";
        if (n % 2 == 0) return n + " KHÔNG là số nguyên tố";

        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) return n + " KHÔNG là số nguyên tố";
        }
        return n + " LÀ số nguyên tố";
    }

    public static void main(String[] args) {
        System.out.println("=== BÀI 5: KIỂM TRA SỐ NGUYÊN TỐ ===");

        // --- HỢP LỆ ---
        System.out.println("TC1 n=2:  " + kiemTraNguyenTo(2));    // LÀ (số nguyên tố nhỏ nhất)
        System.out.println("TC2 n=3:  " + kiemTraNguyenTo(3));    // LÀ
        System.out.println("TC3 n=7:  " + kiemTraNguyenTo(7));    // LÀ
        System.out.println("TC4 n=97: " + kiemTraNguyenTo(97));   // LÀ
        System.out.println("TC5 n=1:  " + kiemTraNguyenTo(1));    // KHÔNG (theo định nghĩa)
        System.out.println("TC6 n=4:  " + kiemTraNguyenTo(4));    // KHÔNG
        System.out.println("TC7 n=9:  " + kiemTraNguyenTo(9));    // KHÔNG (3*3)
        System.out.println("TC8 n=100:" + kiemTraNguyenTo(100));  // KHÔNG

        // --- BIÊN / KHÔNG HỢP LỆ ---
        // TC9: n = 0 → không phải nguyên tố [BIÊN]
        System.out.println("TC9  n=0  [BIÊN]: " + kiemTraNguyenTo(0));     // KHÔNG

        // TC10: n âm → KHÔNG HỢP LỆ [DỮ LIỆU SAI]
        System.out.println("TC10 n=-5 [KO HỢP LỆ]: " + kiemTraNguyenTo(-5)); // Không hợp lệ
    }
}

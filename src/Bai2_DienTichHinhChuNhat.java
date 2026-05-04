public class Bai2_DienTichHinhChuNhat {

    /**
     * Tính diện tích hình chữ nhật
     * Công thức: S = a * b
     * @param a chiều dài (> 0)
     * @param b chiều rộng (> 0)
     * @return diện tích, hoặc -1 nếu không hợp lệ
     */
    public static double tinhDienTich(double a, double b) {
        if (a <= 0 || b <= 0) {
            return -1;
        }
        return a * b;
    }

    public static void main(String[] args) {
        System.out.println("=== BÀI 2: DIỆN TÍCH HÌNH CHỮ NHẬT ===");

        // --- HỢP LỆ ---
        System.out.println("TC1 (a=5, b=3): " + tinhDienTich(5, 3));         // Kỳ vọng: 15.0
        System.out.println("TC2 (a=4, b=4): " + tinhDienTich(4, 4));         // Kỳ vọng: 16.0
        System.out.println("TC3 (a=2.5, b=4): " + tinhDienTich(2.5, 4));     // Kỳ vọng: 10.0
        System.out.println("TC4 (a=0.1, b=0.1): " + tinhDienTich(0.1, 0.1)); // Kỳ vọng: 0.01

        // --- KHÔNG HỢP LỆ / BIÊN ---
        // TC5: a = 0 → KHÔNG HỢP LỆ
        System.out.println("TC5 (a=0, b=5) [KO HỢP LỆ]: " + tinhDienTich(0, 5));    // Kỳ vọng: -1

        // TC6: b âm → KHÔNG HỢP LỆ
        System.out.println("TC6 (a=3, b=-4) [KO HỢP LỆ]: " + tinhDienTich(3, -4));  // Kỳ vọng: -1

        // TC7: cả hai = 0 → KHÔNG HỢP LỆ
        System.out.println("TC7 (a=0, b=0) [KO HỢP LỆ]: " + tinhDienTich(0, 0));    // Kỳ vọng: -1
    }
}

public class Bai1_ChuViHinhChuNhat {

    /**
     * Tính chu vi hình chữ nhật
     * Công thức: C = 2 * (a + b)
     * @param a chiều dài (> 0)
     * @param b chiều rộng (> 0)
     * @return chu vi hình chữ nhật, hoặc -1 nếu đầu vào không hợp lệ
     */
    public static double tinhChuVi(double a, double b) {
        if (a <= 0 || b <= 0) {
            return -1; // Dữ liệu không hợp lệ
        }
        return 2 * (a + b);
    }

    public static void main(String[] args) {
        // --- TEST CASES HỢP LỆ ---
        System.out.println("=== BÀI 1: CHU VI HÌNH CHỮ NHẬT ===");

        // TC1: chiều dài và rộng bình thường
        System.out.println("TC1 (a=5, b=3): " + tinhChuVi(5, 3));         // Kỳ vọng: 16.0

        // TC2: hình vuông (a == b)
        System.out.println("TC2 (a=4, b=4): " + tinhChuVi(4, 4));         // Kỳ vọng: 16.0

        // TC3: giá trị thực
        System.out.println("TC3 (a=2.5, b=1.5): " + tinhChuVi(2.5, 1.5)); // Kỳ vọng: 8.0

        // TC4: một cạnh rất lớn
        System.out.println("TC4 (a=1000, b=1): " + tinhChuVi(1000, 1));   // Kỳ vọng: 2002.0

        // --- TEST CASES KHÔNG HỢP LỆ / BIÊN ---
        // TC5: a = 0 → KHÔNG HỢP LỆ
        System.out.println("TC5 (a=0, b=3) [KO HỢP LỆ]: " + tinhChuVi(0, 3));     // Kỳ vọng: -1

        // TC6: b âm → KHÔNG HỢP LỆ
        System.out.println("TC6 (a=5, b=-2) [KO HỢP LỆ]: " + tinhChuVi(5, -2));   // Kỳ vọng: -1

        // TC7: cả hai âm → KHÔNG HỢP LỆ
        System.out.println("TC7 (a=-1, b=-3) [KO HỢP LỆ]: " + tinhChuVi(-1, -3)); // Kỳ vọng: -1
    }
}

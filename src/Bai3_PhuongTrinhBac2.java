public class Bai3_PhuongTrinhBac2 {

    /**
     * Giải phương trình bậc 2: ax² + bx + c = 0
     * @return mảng kết quả dạng String mô tả nghiệm
     */
    public static String giai(double a, double b, double c) {
        if (a == 0) {
            // Không phải phương trình bậc 2
            if (b == 0) {
                if (c == 0) return "Phương trình vô số nghiệm";
                else        return "Phương trình vô nghiệm";
            }
            return "Phương trình bậc 1: x = " + (-c / b);
        }

        double delta = b * b - 4 * a * c;

        if (delta < 0) {
            return "Phương trình vô nghiệm (delta = " + delta + ")";
        } else if (delta == 0) {
            double x = -b / (2 * a);
            return "Nghiệm kép: x = " + x;
        } else {
            double x1 = (-b + Math.sqrt(delta)) / (2 * a);
            double x2 = (-b - Math.sqrt(delta)) / (2 * a);
            return "Hai nghiệm phân biệt: x1 = " + x1 + ", x2 = " + x2;
        }
    }

    public static void main(String[] args) {
        System.out.println("=== BÀI 3: GIẢI PHƯƠNG TRÌNH BẬC 2 ===");

        // --- HỢP LỆ ---
        // TC1: Delta > 0, hai nghiệm phân biệt (1x²-5x+6=0 → x1=3, x2=2)
        System.out.println("TC1 (1,-5,6): " + giai(1, -5, 6));

        // TC2: Delta = 0, nghiệm kép (x²-2x+1=0 → x=1)
        System.out.println("TC2 (1,-2,1): " + giai(1, -2, 1));

        // TC3: Delta < 0, vô nghiệm (x²+x+1=0)
        System.out.println("TC3 (1,1,1): " + giai(1, 1, 1));

        // TC4: a âm (−x²+3x−2=0 → x1=2, x2=1)
        System.out.println("TC4 (-1,3,-2): " + giai(-1, 3, -2));

        // --- KHÔNG HỢP LỆ / BIÊN ---
        // TC5: a=0, b=0, c=0 → vô số nghiệm [BIÊN ĐẶC BIỆT]
        System.out.println("TC5 (0,0,0) [BIÊN]: " + giai(0, 0, 0));

        // TC6: a=0, b=0, c=5 → vô nghiệm [BIÊN ĐẶC BIỆT]
        System.out.println("TC6 (0,0,5) [BIÊN]: " + giai(0, 0, 5));

        // TC7: a=0, b=2, c=4 → bậc 1 (2x+4=0 → x=-2) [DỮ LIỆU SAI lớp bậc 2]
        System.out.println("TC7 (0,2,4) [DỮ LIỆU SAI]: " + giai(0, 2, 4));
    }
}

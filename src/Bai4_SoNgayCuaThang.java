public class Bai4_SoNgayCuaThang {

    /**
     * Tính số ngày của một tháng trong năm
     * @param thang tháng (1-12)
     * @param nam   năm (> 0)
     * @return số ngày trong tháng, hoặc -1 nếu không hợp lệ
     */
    public static int soNgayCuaThang(int thang, int nam) {
        if (thang < 1 || thang > 12 || nam <= 0) {
            return -1; // Không hợp lệ
        }

        boolean namNhuan = (nam % 4 == 0 && nam % 100 != 0) || (nam % 400 == 0);

        switch (thang) {
            case 1: case 3: case 5: case 7:
            case 8: case 10: case 12:
                return 31;
            case 4: case 6: case 9: case 11:
                return 30;
            case 2:
                return namNhuan ? 29 : 28;
            default:
                return -1;
        }
    }

    public static void main(String[] args) {
        System.out.println("=== BÀI 4: SỐ NGÀY CỦA THÁNG ===");

        // --- HỢP LỆ ---
        System.out.println("TC1 (T1/2023): " + soNgayCuaThang(1, 2023));   // 31
        System.out.println("TC2 (T4/2023): " + soNgayCuaThang(4, 2023));   // 30
        System.out.println("TC3 (T2/2024): " + soNgayCuaThang(2, 2024));   // 29 (năm nhuận)
        System.out.println("TC4 (T2/2023): " + soNgayCuaThang(2, 2023));   // 28
        System.out.println("TC5 (T2/2000): " + soNgayCuaThang(2, 2000));   // 29 (chia hết 400)
        System.out.println("TC6 (T2/1900): " + soNgayCuaThang(2, 1900));   // 28 (chia hết 100 nhưng ko 400)

        // --- KHÔNG HỢP LỆ / BIÊN ---
        // TC7: tháng = 0 → KHÔNG HỢP LỆ
        System.out.println("TC7 (T0/2023) [KO HỢP LỆ]: " + soNgayCuaThang(0, 2023));   // -1

        // TC8: tháng = 13 → KHÔNG HỢP LỆ
        System.out.println("TC8 (T13/2023) [KO HỢP LỆ]: " + soNgayCuaThang(13, 2023)); // -1

        // TC9: năm âm → KHÔNG HỢP LỆ
        System.out.println("TC9 (T5/-1) [KO HỢP LỆ]: " + soNgayCuaThang(5, -1));       // -1

        // TC10: năm = 0 → KHÔNG HỢP LỆ
        System.out.println("TC10 (T5/0) [KO HỢP LỆ]: " + soNgayCuaThang(5, 0));        // -1
    }
}

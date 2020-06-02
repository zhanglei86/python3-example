import java.util.Scanner;

/**
 * 汉诺塔问题
 * 参考-[如何理解汉诺塔的递归？](https://www.zhihu.com/question/24385418)
 */
public class HanoiTest {
    // 序列
    private static int ID = 1;

    /**
     * @param n           个数
     * @param origin      起源 from
     * @param assist      中转 buffer
     * @param destination 目的地 to
     */
    public void hanoi(int n, char origin, char assist, char destination) {
        if (n == 1) {
            move(origin, destination);
        } else {
            hanoi(n - 1, origin, destination, assist);
            move(origin, destination);
            hanoi(n - 1, assist, origin, destination);
        }
    }

    // Print the route of the movement
    private void move(char origin, char destination) {
        System.out.printf("%d: %s --> %s\n", ID, origin, destination);
        ID++;
    }

    public static void main(String[] args) {
        // 实例化
        HanoiTest hanoi = new HanoiTest();

        /*
        InputStream is = System.in;
        BufferedReader br = new BufferedReader(new InputStreamReader(is));
        String inputStr = br.readLine();
        OutputStream os = System.out;
        os.write(inputStr.getBytes());
        n = Integer.parseInt(inputStr);
        */

        // 输入
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入汉诺塔的层数：");
        int n = sc.nextInt();

        // 调用
        hanoi.hanoi(n, 'A', 'B', 'C');
    }
}

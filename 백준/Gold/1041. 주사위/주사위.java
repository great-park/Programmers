import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();
        long[] dice = new long[6];

        for (int i = 0; i < 6; i++) {
            dice[i] = sc.nextLong();
        }

        if (N == 1) {
            long maxValue = Long.MIN_VALUE;
            long sum = 0;
            for (long value : dice) {
                maxValue = Math.max(maxValue, value);
                sum += value;
            }
            System.out.println(sum - maxValue);
        } else {
            long minCorner = Long.MAX_VALUE;
            long minEdge = Long.MAX_VALUE;
            long minFace = Long.MAX_VALUE;

            for (int i = 0; i < 6; i++) {
                for (int j = i + 1; j < 6; j++) {
                    if (j != i && j != 5 - i) {
                        long sum = dice[i] + dice[j];
                        for (int k = 0; k < 6; k++) {
                            if (k != i && k != 5 - i && k != j && k != 5 - j) {
                                sum += dice[k];
                                minCorner = Math.min(minCorner, sum);
                                sum -= dice[k];
                            }
                        }
                        minEdge = Math.min(minEdge, dice[i] + dice[j]);
                    }
                }
                minFace = Math.min(minFace, dice[i]);
            }

            long corners = 4;
            long edges = 4 * (N - 1) + 4 * (N - 2);
            long faces = (N - 2) * (N - 2) + 4 * (N - 2) * (N - 1);
            System.out.println(minCorner * corners + minEdge * edges + minFace * faces);
        }
        sc.close();
    }
}
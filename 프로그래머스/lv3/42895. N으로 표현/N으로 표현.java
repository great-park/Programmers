import java.util.HashSet;
import java.util.Set;
class Solution {
    public static int solution(int N, int number) {
        Set<Integer>[] dp = new Set[9];
        int t = N;
        for (int i = 1; i < 9; i++) {
            dp[i] = new HashSet<>();
            dp[i].add(t);
            t = t * 10 + N;
        }

        for (int i = 1; i < 9; i++) {
            for (int j = 1; j < i; j++) {
                for (Integer a : dp[j]) {
                    for (Integer b : dp[i - j]) {
                        dp[i].add(a + b);
                        dp[i].add(a - b);
                        dp[i].add(a * b);
                        if (b != 0) {
                            dp[i].add(a / b);
                        }
                    }
                }
            }
            if (dp[i].contains(number)) {
                return i;
            }
        }
        return -1;
    }
}
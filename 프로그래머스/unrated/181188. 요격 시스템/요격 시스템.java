import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        Arrays.sort(targets, (a,b) -> Integer.compare(a[1], b[1]));
        
        int last_end = 0;
        for (int i=0; i<targets.length; i++) {
            if(last_end <= targets[i][0]) {
                answer += 1;
                last_end = targets[i][1];
            } else {
                last_end = Math.max(targets[i][0], last_end);
            }
        }
        
        return answer;
    }
}
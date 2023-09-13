import java.util.*;

class Solution {
    static int cur_max_p = 0;
    public int solution(int[] priorities, int location) {
        int answer = 0;
        PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
        
        for(int i=0; i<priorities.length; i++) {
            q.add(priorities[i]);
        }
        
        while(!q.isEmpty()) {
            for(int i=0; i<priorities.length;i++) {
                if(priorities[i] == q.peek()) {
                    if (i == location) {
                        answer++;
                        return answer;
                    }
                    answer++;
                    q.poll();
                }
            }
            
            
        }
        
        
        
        
        
        return answer;
    }
    
}
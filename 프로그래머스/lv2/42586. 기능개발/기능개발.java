import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        ArrayList<Integer> list = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();

        for (int i = 0; i < progresses.length; i++) {
            if ((100 - progresses[i]) % speeds[i] == 0) {
                q.add((100 - progresses[i]) / speeds[i]);
            } else {
                q.add((100 - progresses[i]) / speeds[i] + 1);
            }
        }
        
        // 7, 3, 13
        
        int head_rest_day = q.poll();
        int cnt = 1;
        
        while(!q.isEmpty()) {
            if (q.peek() <= head_rest_day) { // 현재 맨 앞의 작업일 보다 작거나 같으면 같이 배포
                cnt++;
                q.poll();
            }
            else {
                list.add(cnt);
                cnt = 1;
                head_rest_day = q.poll();
            }
            
        }
        list.add(cnt);
        
        
        
        int[] answer = new int[list.size()];
        for (int i=0; i<answer.length; i++){
            answer[i] = list.get(i);
        }

        return answer;
    
    }
}


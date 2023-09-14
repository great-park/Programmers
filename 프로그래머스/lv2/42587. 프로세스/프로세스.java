import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
        
        for(int i=0; i<priorities.length;i++){
            q.offer(priorities[i]);
        }
        
        while(!q.isEmpty()) {
            for(int i=0; i<priorities.length; i++){
                if(!q.isEmpty() && q.peek() == priorities[i]) {
                    q.poll();
                    answer++;
                    if (i == location) {
                        return answer;
                    }
                }
            }
        }
        
        return answer;
    }
}

// import java.util.*;

// class Solution {
//     public int solution(int[] priorities, int location) {
//         int answer = 0;
//         PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
        
//         for(int i=0; i<priorities.length; i++) {
//             q.add(priorities[i]);
//         }
        
//         while(!q.isEmpty()) {
//             for(int i=0; i<priorities.length;i++) {
//                 if(priorities[i] == q.peek()) {
//                     if (i == location) {
//                         answer++;
//                         return answer;
//                     }
//                     answer++;
//                     q.poll();
//                 }
//             }   
//         }
//         return answer;
//     }
// }
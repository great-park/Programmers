import java.util.*;

class Solution {
    class Function {
        int progress;
        int speed;
        Function (int progress, int speed) {
            this.progress = progress;
            this.speed = speed;
        }
        public void develop() {
            this.progress += this.speed;
        }
    }
    
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Function> q = new LinkedList<>();
        List<Integer> list = new ArrayList<>();    
        for (int i=0; i<progresses.length; i++) {
            Function f = new Function(progresses[i], speeds[i]);
            q.offer(f);
        }
        
        while(!q.isEmpty()) {
            for(Function f : q) {
                f.develop();
            }
            
            int this_term_deploy_cnt = 0;
            while(!q.isEmpty() && q.peek().progress >= 100) {
                q.poll();
                this_term_deploy_cnt++;
            }
            if (this_term_deploy_cnt != 0){
                list.add(this_term_deploy_cnt);
            }
        }

        int[] answer = new int[list.size()];
        for(int i=0; i<list.size();i++){
            answer[i] = list.get(i);
        }
        return answer;        
    }
}



// import java.util.*;

// class Solution {
//     public int[] solution(int[] progresses, int[] speeds) {
        
//         ArrayList<Integer> list = new ArrayList<>();
//         Queue<Integer> q = new LinkedList<>();

//         for (int i = 0; i < progresses.length; i++) {
//             if ((100 - progresses[i]) % speeds[i] == 0) {
//                 q.add((100 - progresses[i]) / speeds[i]);
//             } else {
//                 q.add((100 - progresses[i]) / speeds[i] + 1);
//             }
//         }
        
//         int head_rest_day = q.poll();
//         int cnt = 1;
//         while(!q.isEmpty()) {
//             if (q.peek() <= head_rest_day) { // 현재 맨 앞의 작업일 보다 작거나 같으면 같이 배포
//                 cnt++;
//                 q.poll();
//             }
//             else {
//                 list.add(cnt);
//                 head_rest_day = q.poll();
//                 cnt = 1;
//             }
//         }
//         list.add(cnt); // 마지막 배포
        
//         int[] answer = new int[list.size()];
//         for (int i=0; i<answer.length; i++){
//             answer[i] = list.get(i);
//         }
//         return answer;
//     }
// }


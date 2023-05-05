import java.util.LinkedList;
import java.util.Queue;

class Solution {
       public int solution(int[] numbers, int target) {
           int answer = 0;
           Queue<Integer> q = new LinkedList<Integer>();
           q.offer(0); // 깊이
           q.offer(0); // 값
           while(q.peek() != null) {
               int depth = q.poll();
               int value = q.poll();
               
               if (depth ==numbers.length) {
                   if(value == target)
                        answer++;
               } else {
                   q.offer(depth + 1);
                   q.offer(value + numbers[depth]);
                   
                   q.offer(depth + 1);
                   q.offer(value - numbers[depth]);
                   
               }
           }
           return answer;
       } 
}
import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> s = new Stack<>();
        for(int i=0; i<arr.length; i++) {
            int num = arr[i];      
            if (s.isEmpty()) {
                s.push(num);
                continue;
            }
            if (s.peek() == num) {
                continue;
            }
            s.push(num);
        }
        int[] answer = new int[s.size()];
        for(int i=s.size()-1; i>=0; i--) {
            answer[i] = s.pop();
        }
        return answer;
    
    }
}

// import java.util.*;

// public class Solution {
//     public int[] solution(int []arr) {
//         ArrayList<Integer> answerList = new ArrayList<Integer>();
//         int value = -1;
//         for(int i=0; i<arr.length; i++) {
//             if(arr[i] != value) {
//                 answerList.add(arr[i]);
//                 value = arr[i];
//             }
//         }
//         return answerList.stream()
//             .mapToInt(i->i)
//             .toArray();
//     }
// }
// import java.util.*;

// class Solution {
//     boolean solution(String s) {
//         Stack<Boolean> st = new Stack<>();
//         String[] str_arr = s.split("");
//         List<String> str_list = new ArrayList<>();
        
//         for(int i=0; i<str_arr.length; i++) {
//             if (str_arr[i].equals("(")){
//                 st.push(true);
//             }
//             else if (str_arr[i].equals(")")) {
//                 if (st.empty()) { // 스택에서 빼려는데 빈 경우 바로 false
//                     return false;
//                 }
//                 else {
//                     st.pop();
//                 }
//             }
//         }
    
//         if (st.empty()) {
//             return true;
//         }  
//         else {
//             return false;
//         }
//     }
// }

// 시간 초과


import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<Boolean> st = new Stack<>();
        
        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i) == '(') {
                st.push(true);
            } 
            else {
                if (st.isEmpty()) {
                    return false;
                }
                st.pop();
            }
        }
        
        return st.isEmpty();
    }   
}


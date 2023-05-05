import java.util.Queue;
import java.util.LinkedList;

class Solution {
    static boolean[] chk;
    Queue<Integer> q = new LinkedList<Integer>();
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        chk = new boolean[n];
    
        for(int i=0; i<n; i++) {
            if(!chk[i]){
                bfs(computers, i, n);
                answer++;
            }
        }
        return answer;
    }

    void bfs(int[][] computers, int start, int n) {
        
        q.offer(start);
        chk[start] = true;
        
        while(!q.isEmpty()){
            int v = q.poll();
            for(int j = 0; j<n;j++) {
                if(!chk[j]  && computers[v][j] == 1) {
                
                    q.offer(j);
                    chk[j] = true;
                }
            }
        }
        
    }
}
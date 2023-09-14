import java.util.*;

class Solution {
    boolean[] visited;
    Queue<Integer> q = new LinkedList<Integer>();
    int answer = 0;
      
    public int solution(int n, int[][] computers) {
        visited = new boolean[n];
        
        for(int i=0;i<n;i++){
            if(!visited[i]) {
                bfs(i, computers, n);
                answer++;
            } 
        }
        return answer;
    }
    
    public void bfs(int start, int[][] computers, int n) {
        q.offer(start);
        visited[start] = true;
        
        while(!q.isEmpty()) {
            int node = q.poll();
            for (int next=0; next< n; next++) {
                if (!visited[next] && computers[node][next] == 1) {
                    q.offer(next);
                    visited[next] = true;
                }
            }
        }
    }
}